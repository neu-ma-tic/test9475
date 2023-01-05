"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.MusicSubscription = void 0;
const voice_1 = require("@discordjs/voice");
const util_1 = require("util");
const wait = util_1.promisify(setTimeout);
/**
 * A MusicSubscription exists for each active VoiceConnection. Each subscription has its own audio player and queue,
 * and it also attaches logic to the audio player and voice connection for error handling and reconnection logic.
 */
class MusicSubscription {
    constructor(voiceConnection) {
        this.queueLock = false;
        this.readyLock = false;
        this.voiceConnection = voiceConnection;
        this.audioPlayer = voice_1.createAudioPlayer();
        this.queue = [];
        this.voiceConnection.on('stateChange', async (_, newState) => {
            if (newState.status === voice_1.VoiceConnectionStatus.Disconnected) {
                if (newState.reason === voice_1.VoiceConnectionDisconnectReason.WebSocketClose && newState.closeCode === 4014) {
                    /*
                        If the WebSocket closed with a 4014 code, this means that we should not manually attempt to reconnect,
                        but there is a chance the connection will recover itself if the reason of the disconnect was due to
                        switching voice channels. This is also the same code for the bot being kicked from the voice channel,
                        so we allow 5 seconds to figure out which scenario it is. If the bot has been kicked, we should destroy
                        the voice connection.
                    */
                    try {
                        await voice_1.entersState(this.voiceConnection, voice_1.VoiceConnectionStatus.Connecting, 5000);
                        // Probably moved voice channel
                    }
                    catch {
                        this.voiceConnection.destroy();
                        // Probably removed from voice channel
                    }
                }
                else if (this.voiceConnection.rejoinAttempts < 5) {
                    /*
                        The disconnect in this case is recoverable, and we also have <5 repeated attempts so we will reconnect.
                    */
                    await wait((this.voiceConnection.rejoinAttempts + 1) * 5000);
                    this.voiceConnection.rejoin();
                }
                else {
                    /*
                        The disconnect in this case may be recoverable, but we have no more remaining attempts - destroy.
                    */
                    this.voiceConnection.destroy();
                }
            }
            else if (newState.status === voice_1.VoiceConnectionStatus.Destroyed) {
                /*
                    Once destroyed, stop the subscription
                */
                this.stop();
            }
            else if (!this.readyLock &&
                (newState.status === voice_1.VoiceConnectionStatus.Connecting || newState.status === voice_1.VoiceConnectionStatus.Signalling)) {
                /*
                    In the Signalling or Connecting states, we set a 20 second time limit for the connection to become ready
                    before destroying the voice connection. This stops the voice connection permanently existing in one of these
                    states.
                */
                this.readyLock = true;
                try {
                    await voice_1.entersState(this.voiceConnection, voice_1.VoiceConnectionStatus.Ready, 20000);
                }
                catch {
                    if (this.voiceConnection.state.status !== voice_1.VoiceConnectionStatus.Destroyed)
                        this.voiceConnection.destroy();
                }
                finally {
                    this.readyLock = false;
                }
            }
        });
        // Configure audio player
        this.audioPlayer.on('stateChange', (oldState, newState) => {
            if (newState.status === voice_1.AudioPlayerStatus.Idle && oldState.status !== voice_1.AudioPlayerStatus.Idle) {
                // If the Idle state is entered from a non-Idle state, it means that an audio resource has finished playing.
                // The queue is then processed to start playing the next track, if one is available.
                oldState.resource.metadata.onFinish();
                void this.processQueue();
            }
            else if (newState.status === voice_1.AudioPlayerStatus.Playing) {
                // If the Playing state has been entered, then a new track has started playback.
                newState.resource.metadata.onStart();
            }
        });
        this.audioPlayer.on('error', (error) => error.resource.metadata.onError(error));
        voiceConnection.subscribe(this.audioPlayer);
    }
    /**
     * Adds a new Track to the queue.
     *
     * @param track The track to add to the queue
     */
    enqueue(track) {
        this.queue.push(track);
        void this.processQueue();
    }
    /**
     * Stops audio playback and empties the queue
     */
    stop() {
        this.queueLock = true;
        this.queue = [];
        this.audioPlayer.stop(true);
    }
    /**
     * Attempts to play a Track from the queue
     */
    async processQueue() {
        // If the queue is locked (already being processed), is empty, or the audio player is already playing something, return
        if (this.queueLock || this.audioPlayer.state.status !== voice_1.AudioPlayerStatus.Idle || this.queue.length === 0) {
            return;
        }
        // Lock the queue to guarantee safe access
        this.queueLock = true;
        // Take the first item from the queue. This is guaranteed to exist due to the non-empty check above.
        const nextTrack = this.queue.shift();
        try {
            // Attempt to convert the Track into an AudioResource (i.e. start streaming the video)
            const resource = await nextTrack.createAudioResource();
            this.audioPlayer.play(resource);
            this.queueLock = false;
        }
        catch (error) {
            // If an error occurred, try the next item of the queue instead
            nextTrack.onError(error);
            this.queueLock = false;
            return this.processQueue();
        }
    }
}
exports.MusicSubscription = MusicSubscription;
//# sourceMappingURL=subscription.js.map