import { AudioResource } from '@discordjs/voice';
/**
 * This is the data required to create a Track object
 */
export interface TrackData {
    url: string;
    title: string;
    onStart: () => void;
    onFinish: () => void;
    onError: (error: Error) => void;
}
/**
 * A Track represents information about a YouTube video (in this context) that can be added to a queue.
 * It contains the title and URL of the video, as well as functions onStart, onFinish, onError, that act
 * as callbacks that are triggered at certain points during the track's lifecycle.
 *
 * Rather than creating an AudioResource for each video immediately and then keeping those in a queue,
 * we use tracks as they don't pre-emptively load the videos. Instead, once a Track is taken from the
 * queue, it is converted into an AudioResource just in time for playback.
 */
export declare class Track implements TrackData {
    readonly url: string;
    readonly title: string;
    readonly onStart: () => void;
    readonly onFinish: () => void;
    readonly onError: (error: Error) => void;
    private constructor();
    /**
     * Creates an AudioResource from this Track.
     */
    createAudioResource(): Promise<AudioResource<Track>>;
    /**
     * Creates a Track from a video URL and lifecycle callback methods.
     *
     * @param url The URL of the video
     * @param methods Lifecycle callbacks
     * @returns The created Track
     */
    static from(url: string, methods: Pick<Track, 'onStart' | 'onFinish' | 'onError'>): Promise<Track>;
}
//# sourceMappingURL=track.d.ts.map