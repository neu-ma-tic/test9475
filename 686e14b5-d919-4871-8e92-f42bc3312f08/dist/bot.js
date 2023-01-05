"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const discord_js_1 = __importStar(require("discord.js"));
const voice_1 = require("@discordjs/voice");
const track_1 = require("./music/track");
const subscription_1 = require("./music/subscription");
const yt_search_1 = __importDefault(require("yt-search"));
// eslint-disable-next-line @typescript-eslint/no-var-requires, @typescript-eslint/no-require-imports
const { token } = require('../auth.json');
const client = new discord_js_1.default.Client({ intents: ['GUILD_VOICE_STATES', 'GUILD_MESSAGES', 'GUILDS'] });
client.on('ready', () => console.log('Ready!'));
// This contains the setup code for creating slash commands in a guild. The owner of the bot can send "!deploy" to create them.
client.on('messageCreate', async (message) => {
    var _a, _b, _c, _d;
    if (!message.guild)
        return;
    if (!((_a = client.application) === null || _a === void 0 ? void 0 : _a.owner))
        await ((_b = client.application) === null || _b === void 0 ? void 0 : _b.fetch());
    if (message.content.toLowerCase() === '!khởi tạo' && message.author.id === ((_d = (_c = client.application) === null || _c === void 0 ? void 0 : _c.owner) === null || _d === void 0 ? void 0 : _d.id)) {
        await message.guild.commands.set([
            {
                name: 'play',
                description: 'chơi nhạc',
                options: [
                    {
                        name: 'song',
                        type: 'STRING',
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
const subscriptions = new Map();
// Handles slash command interactions
client.on('interactionCreate', async (interaction) => {
    if (!interaction.isCommand() || !interaction.guildId)
        return;
    let subscription = subscriptions.get(interaction.guildId);
    if (interaction.commandName === 'play') {
        await interaction.deferReply();
        console.log(interaction.options);
        // Extract the video URL from the command
        const urlRaw = interaction.options.get('song').value;
        let url;
        let isLink = false;
        ['https://www.youtube.com/', 'youtube.com', 'www.youtube.com/', 'https://m.youtube.com/', 'm.youtube.com/'].forEach((ytlink) => {
            if (urlRaw.startsWith(ytlink)) {
                isLink = true;
            }
        });
        // eslint-disable-next-line @typescript-eslint/no-unnecessary-condition
        if (isLink)
            url = urlRaw;
        else {
            const videoResult = await yt_search_1.default(urlRaw);
            console.log(videoResult);
            if (videoResult.all.length > 1)
                url = videoResult.all[0].url;
            else
                url = urlRaw;
        }
        // If a connection to the guild doesn't already exist and the user is in a voice channel, join that channel
        // and create a subscription.
        if (!subscription) {
            if (interaction.member instanceof discord_js_1.GuildMember && interaction.member.voice.channel) {
                const channel = interaction.member.voice.channel;
                subscription = new subscription_1.MusicSubscription(voice_1.joinVoiceChannel({
                    channelId: channel.id,
                    guildId: channel.guild.id,
                    adapterCreator: channel.guild.voiceAdapterCreator,
                }));
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
            await voice_1.entersState(subscription.voiceConnection, voice_1.VoiceConnectionStatus.Ready, 20e3);
        }
        catch (error) {
            console.warn(error);
            await interaction.followUp('Failed to join voice channel within 20 seconds, please try again later!');
            return;
        }
        try {
            // Attempt to create a Track from the user's video URL
            const track = await track_1.Track.from(url, {
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
        }
        catch (error) {
            console.warn(error);
            await interaction.reply('Failed to play track, please try again later!');
        }
    }
    else if (interaction.commandName === 'skip') {
        if (subscription) {
            // Calling .stop() on an AudioPlayer causes it to transition into the Idle state. Because of a state transition
            // listener defined in music/subscription.ts, transitions into the Idle state mean the next track from the queue
            // will be loaded and played.
            subscription.audioPlayer.stop();
            await interaction.reply('Skipped song!');
        }
        else {
            await interaction.reply('Not playing in this server!');
        }
    }
    else if (interaction.commandName === 'queue') {
        // Print out the current queue, including up to the next 5 tracks to be played.
        if (subscription) {
            const current = subscription.audioPlayer.state.status === voice_1.AudioPlayerStatus.Idle
                ? `Nothing is currently playing!`
                : `Playing **${subscription.audioPlayer.state.resource.metadata.title}**`;
            const queue = subscription.queue
                .slice(0, 5)
                .map((track, index) => `${index + 1}) ${track.title}`)
                .join('\n');
            await interaction.reply(`${current}\n\n${queue}`);
        }
        else {
            await interaction.reply('Not playing in this server!');
        }
    }
    else if (interaction.commandName === 'pause') {
        if (subscription) {
            subscription.audioPlayer.pause();
            await interaction.reply({ content: `Paused!`, ephemeral: true });
        }
        else {
            await interaction.reply('Not playing in this server!');
        }
    }
    else if (interaction.commandName === 'stop') {
        if (subscription) {
            subscription.audioPlayer.stop();
            await interaction.reply({ content: `Đã dừng`, ephemeral: true });
        }
        else {
            await interaction.reply('Not playing in this server!');
        }
    }
    else if (interaction.commandName === 'resume') {
        if (subscription) {
            subscription.audioPlayer.unpause();
            await interaction.reply({ content: `Unpaused!`, ephemeral: true });
        }
        else {
            await interaction.reply('Not playing in this server!');
        }
    }
    else if (interaction.commandName === 'leave') {
        if (subscription) {
            subscription.voiceConnection.destroy();
            subscriptions.delete(interaction.guildId);
            await interaction.reply({ content: `Left channel!`, ephemeral: true });
        }
        else {
            await interaction.reply('Not playing in this server!');
        }
    }
    else {
        await interaction.reply('Unknown command');
    }
});
client.on('error', console.warn);
void client.login(token);
//# sourceMappingURL=bot.js.map