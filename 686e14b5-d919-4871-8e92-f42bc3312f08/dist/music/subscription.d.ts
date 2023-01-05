import { AudioPlayer, VoiceConnection } from '@discordjs/voice';
import { Track } from './track';
/**
 * A MusicSubscription exists for each active VoiceConnection. Each subscription has its own audio player and queue,
 * and it also attaches logic to the audio player and voice connection for error handling and reconnection logic.
 */
export declare class MusicSubscription {
    readonly voiceConnection: VoiceConnection;
    readonly audioPlayer: AudioPlayer;
    queue: Track[];
    queueLock: boolean;
    readyLock: boolean;
    constructor(voiceConnection: VoiceConnection);
    /**
     * Adds a new Track to the queue.
     *
     * @param track The track to add to the queue
     */
    enqueue(track: Track): void;
    /**
     * Stops audio playback and empties the queue
     */
    stop(): void;
    /**
     * Attempts to play a Track from the queue
     */
    private processQueue;
}
//# sourceMappingURL=subscription.d.ts.map