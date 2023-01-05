import Discord, { Interaction, GuildMember, Snowflake } from 'discord.js';
import {
	AudioPlayerStatus,
	AudioResource,
	entersState,
	joinVoiceChannel,
	VoiceConnectionStatus,
} from '@discordjs/voice';
import { Track } from './music/track';
import { MusicSubscription } from './music/subscription';
import yts from 'yt-search';
import keepAlive from "server"
// eslint-disable-next-line @typescript-eslint/no-var-requires, @typescript-eslint/no-require-imports
const { token } = require('../auth.json');

const client = new Discord.Client({ intents: ['GUILD_VOICE_STATES', 'GUILD_MESSAGES', 'GUILDS'] });

client.on('ready', () => console.log('Ready!'));

// This contains the setup code for creating slash commands in a guild. The owner of the bot can send "!deploy" to create them.
client.on('messageCreate', async (message) => {
	if (!message.guild) return;
	if (!client.application?.owner) await client.application?.fetch();

	if (message.content.toLowerCase() === '!khởi tạo' && message.author.id === client.application?.owner?.id) {
		await message.guild.commands.set([
			{
				name: 'play',
				description: 'chơi nhạc',
				options: [
					{
						name: 'song',
						type: 'STRING' as const,
						description: 'Link hoặc tên bài hát',
						required: true,
					},
				],
			},
			{
				name: 'skip',
				description: 'Chuyển bài kế tiếp',
			},
			{
				name: 'queue',
				description: 'Xem danh sách bài hát hiện tại',
			},
			{
				name: 'pause',
				description: 'Tạm dừng chơi nhạc',
			},
			{
				name: 'stop',
				description: 'Dừng chơi nhạc và xóa danh sách',
			},
			{
				name: 'resume',
				description: 'Tiếp tục chơi nhạc',
			},
			{
				name: 'leave',
				description: 'Yêu cầu bot rồi kênh âm thanh',
			},
		]);

		await message.reply('Đã khởi tạo và làm mới lệnh!');
	}
});

/**
 * Maps guild IDs to music subscriptions, which exist if the bot has an active VoiceConnection to the guild.
 */
const subscriptions = new Map<Snowflake, MusicSubscription>();

// Handles slash command interactions
client.on('interactionCreate', async (interaction: Interaction) => {
	if (!interaction.isCommand() || !interaction.guildId) return;
	let subscription = subscriptions.get(interaction.guildId);

	if (interaction.commandName === 'play') {
		await interaction.deferReply();
		console.log(interaction.options);
		// Extract the video URL from the command
		const urlRaw = interaction.options.get('song')!.value! as string;
		let url: string;
		let isLink = false;
		['https://www.youtube.com/', 'youtube.com', 'www.youtube.com/', 'https://m.youtube.com/', 'm.youtube.com/'].forEach(
			(ytlink) => {
				if (urlRaw.startsWith(ytlink)) {
					isLink = true;
				}
			},
		);
		// eslint-disable-next-line @typescript-eslint/no-unnecessary-condition
		if (isLink) url = urlRaw;
		else {
			const videoResult = await yts(urlRaw);
			console.log(videoResult);
			if (videoResult.all.length > 1) url = videoResult.all[0].url;
			else url = urlRaw;
		}

		// If a connection to the guild doesn't already exist and the user is in a voice channel, join that channel
		// and create a subscription.
		if (!subscription) {
			if (interaction.member instanceof GuildMember && interaction.member.voice.channel) {
				const channel = interaction.member.voice.channel;
				subscription = new MusicSubscription(
					joinVoiceChannel({
						channelId: channel.id,
						guildId: channel.guild.id,
						adapterCreator: channel.guild.voiceAdapterCreator,
					}),
				);
				subscription.voiceConnection.on('error', console.warn);
				subscriptions.set(interaction.guildId, subscription);
			}
		}

		// If there is no subscription, tell the user they need to join a channel.
		if (!subscription) {
			await interaction.followUp('Bạn hãy vào 1 kênh âm thanh và thử lại');
			return;
		}

		// Make sure the connection is ready before processing the user's request
		try {
			await entersState(subscription.voiceConnection, VoiceConnectionStatus.Ready, 20e3);
		} catch (error) {
			console.warn(error);
			await interaction.followUp('Failed to join voice channel within 20 seconds, please try again later!');
			return;
		}

		try {
			// Attempt to create a Track from the user's video URL
			const track = await Track.from(url, {
				onStart() {
					interaction.followUp({ content: 'Now playing!', ephemeral: true }).catch(console.warn);
				},
				onFinish() {
					interaction.followUp({ content: 'Now finished!', ephemeral: true }).catch(console.warn);
				},
				onError(error) {
					console.warn(error);
					interaction.followUp({ content: `Error: ${error.message}`, ephemeral: true }).catch(console.warn);
				},
			});
			// Enqueue the track and reply a success message to the user
			subscription.enqueue(track);
			await interaction.followUp(`Enqueued **${track.title}**`);
		} catch (error) {
			console.warn(error);
			await interaction.reply('Failed to play track, please try again later!');
		}
	} else if (interaction.commandName === 'skip') {
		if (subscription) {
			// Calling .stop() on an AudioPlayer causes it to transition into the Idle state. Because of a state transition
			// listener defined in music/subscription.ts, transitions into the Idle state mean the next track from the queue
			// will be loaded and played.
			subscription.audioPlayer.stop();
			await interaction.reply('Skipped song!');
		} else {
			await interaction.reply('Not playing in this server!');
		}
	} else if (interaction.commandName === 'queue') {
		// Print out the current queue, including up to the next 5 tracks to be played.
		if (subscription) {
			const current =
				subscription.audioPlayer.state.status === AudioPlayerStatus.Idle
					? `Nothing is currently playing!`
					: `Playing **${(subscription.audioPlayer.state.resource as AudioResource<Track>).metadata.title}**`;

			const queue = subscription.queue
				.slice(0, 5)
				.map((track, index) => `${index + 1}) ${track.title}`)
				.join('\n');

			await interaction.reply(`${current}\n\n${queue}`);
		} else {
			await interaction.reply('Not playing in this server!');
		}
	} else if (interaction.commandName === 'pause') {
		if (subscription) {
			subscription.audioPlayer.pause();
			await interaction.reply({ content: `Paused!`, ephemeral: true });
		} else {
			await interaction.reply('Not playing in this server!');
		}
	} else if (interaction.commandName === 'stop') {
		if (subscription) {
			subscription.audioPlayer.stop();
			await interaction.reply({ content: `Đã dừng`, ephemeral: true });
		} else {
			await interaction.reply('Not playing in this server!');
		}
	} else if (interaction.commandName === 'resume') {
		if (subscription) {
			subscription.audioPlayer.unpause();
			await interaction.reply({ content: `Unpaused!`, ephemeral: true });
		} else {
			await interaction.reply('Not playing in this server!');
		}
	} else if (interaction.commandName === 'leave') {
		if (subscription) {
			subscription.voiceConnection.destroy();
			subscriptions.delete(interaction.guildId);
			await interaction.reply({ content: `Left channel!`, ephemeral: true });
		} else {
			await interaction.reply('Not playing in this server!');
		}
	} else {
		await interaction.reply('Unknown command');
	}
});

client.on('error', console.warn);
keepAlive();
void client.login(token);
