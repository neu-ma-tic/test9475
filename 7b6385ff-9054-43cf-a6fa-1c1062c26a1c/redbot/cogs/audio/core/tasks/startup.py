import asyncio
import datetime
import itertools
import logging
from pathlib import Path

from typing import Optional

import lavalink

from redbot.core.data_manager import cog_data_path
from redbot.core.i18n import Translator
from redbot.core.utils._internal_utils import send_to_owners_with_prefix_replaced
from redbot.core.utils.dbtools import APSWConnectionWrapper

from ...apis.interface import AudioAPIInterface
from ...apis.playlist_wrapper import PlaylistWrapper
from ...audio_logging import debug_exc_log
from ...utils import task_callback
from ..abc import MixinMeta
from ..cog_utils import _OWNER_NOTIFICATION, _SCHEMA_VERSION, CompositeMetaClass

log = logging.getLogger("red.cogs.Audio.cog.Tasks.startup")
_ = Translator("Audio", Path(__file__))


class StartUpTasks(MixinMeta, metaclass=CompositeMetaClass):
    def start_up_task(self):
        # There has to be a task since this requires the bot to be ready
        # If it waits for ready in startup, we cause a deadlock during initial load
        # as initial load happens before the bot can ever be ready.
        self.cog_init_task = self.bot.loop.create_task(self.initialize())
        self.cog_init_task.add_done_callback(task_callback)

    async def initialize(self) -> None:
        await self.bot.wait_until_red_ready()
        # Unlike most cases, we want the cache to exit before migration.
        try:
            await self.maybe_message_all_owners()
            self.db_conn = APSWConnectionWrapper(
                str(cog_data_path(self.bot.get_cog("Audio")) / "Audio.db")
            )
            self.api_interface = AudioAPIInterface(
                self.bot, self.config, self.session, self.db_conn, self.bot.get_cog("Audio")
            )
            self.playlist_api = PlaylistWrapper(self.bot, self.config, self.db_conn)
            await self.playlist_api.init()
            await self.api_interface.initialize()
            self.global_api_user = await self.api_interface.global_cache_api.get_perms()
            await self.data_schema_migration(
                from_version=await self.config.schema_version(), to_version=_SCHEMA_VERSION
            )
            await self.playlist_api.delete_scheduled()
            await self.api_interface.persistent_queue_api.delete_scheduled()
            self.lavalink_restart_connect()
            self.player_automated_timer_task = self.bot.loop.create_task(
                self.player_automated_timer()
            )
            self.player_automated_timer_task.add_done_callback(task_callback)
        except Exception as err:
            log.exception("Audio failed to start up, please report this issue.", exc_info=err)
            raise err

        self.cog_ready_event.set()

    async def restore_players(self):
        tries = 0
        tracks_to_restore = await self.api_interface.persistent_queue_api.fetch_all()
        await asyncio.sleep(10)
        for guild_id, track_data in itertools.groupby(tracks_to_restore, key=lambda x: x.guild_id):
            await asyncio.sleep(0)
            try:
                player: Optional[lavalink.Player]
                track_data = list(track_data)
                guild = self.bot.get_guild(guild_id)
                persist_cache = self._persist_queue_cache.setdefault(
                    guild_id, await self.config.guild(guild).persist_queue()
                )
                if not persist_cache:
                    await self.api_interface.persistent_queue_api.drop(guild_id)
                    continue
                if self.lavalink_connection_aborted:
                    player = None
                else:
                    try:
                        player = lavalink.get_player(guild_id)
                    except IndexError:
                        player = None
                    except KeyError:
                        player = None

                vc = 0
                if player is None:
                    while tries < 25 and vc is not None:
                        try:
                            vc = guild.get_channel(track_data[-1].room_id)
                            if not vc:
                                break
                            perms = vc.permissions_for(guild.me)
                            if not (perms.connect and perms.speak):
                                vc = None
                                break
                            await lavalink.connect(vc)
                            player = lavalink.get_player(guild.id)
                            player.store("connect", datetime.datetime.utcnow())
                            player.store("guild", guild_id)
                            await self.self_deafen(player)
                            break
                        except IndexError:
                            await asyncio.sleep(5)
                            tries += 1
                        except Exception as exc:
                            debug_exc_log(log, exc, "Failed to restore music voice channel")
                            if vc is None:
                                break

                if tries >= 25 or guild is None or vc is None:
                    await self.api_interface.persistent_queue_api.drop(guild_id)
                    continue

                shuffle = await self.config.guild(guild).shuffle()
                repeat = await self.config.guild(guild).repeat()
                volume = await self.config.guild(guild).volume()
                shuffle_bumped = await self.config.guild(guild).shuffle_bumped()
                player.repeat = repeat
                player.shuffle = shuffle
                player.shuffle_bumped = shuffle_bumped
                if player.volume != volume:
                    await player.set_volume(volume)
                for track in track_data:
                    track = track.track_object
                    player.add(guild.get_member(track.extras.get("requester")) or guild.me, track)
                player.maybe_shuffle()
                if not player.is_playing:
                    await player.play()
            except Exception as err:
                debug_exc_log(log, err, f"Error restoring player in {guild_id}")
                await self.api_interface.persistent_queue_api.drop(guild_id)

    async def maybe_message_all_owners(self):
        current_notification = await self.config.owner_notification()
        if current_notification == _OWNER_NOTIFICATION:
            return
        if current_notification < 1 <= _OWNER_NOTIFICATION:
            msg = _(
                """Hello, this message brings you an important update regarding the core Audio cog:
                
Starting from Audio v2.3.0+ you can take advantage of the **Global Audio API**, a new service offered by the Cog-Creators organization that allows your bot to greatly reduce the amount of requests done to YouTube / Spotify. This reduces the likelihood of YouTube rate-limiting your bot for making requests too often.
See `[p]help audioset globalapi` for more information.
Access to this service is disabled by default and **requires you to explicitly opt-in** to start using it.

An access token is **required** to use this API. To obtain this token you may join <https://discord.gg/red> and run `?audioapi register` in the #testing channel.
Note: by using this service you accept that your bot's IP address will be disclosed to the Cog-Creators organization and used only for the purpose of providing the Global API service.

On a related note, it is highly recommended that you enable your local cache if you haven't yet.
To do so, run `[p]audioset cache 5`. This cache, which stores only metadata, will make repeated audio requests faster and further reduce the likelihood of YouTube rate-limiting your bot. Since it's only metadata the required disk space for this cache is expected to be negligible."""
            )
            await send_to_owners_with_prefix_replaced(self.bot, msg)
            await self.config.owner_notification.set(1)
