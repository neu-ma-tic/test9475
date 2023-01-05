"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Track = void 0;
const ytdl_core_1 = require("ytdl-core");
const voice_1 = require("@discordjs/voice");
const youtube_dl_exec_1 = require("youtube-dl-exec");
// eslint-disable-next-line @typescript-eslint/no-empty-function
const noop = () => { };
/**
 * A Track represents information about a YouTube video (in this context) that can be added to a queue.
 * It contains the title and URL of the video, as well as functions onStart, onFinish, onError, that act
 * as callbacks that are triggered at certain points during the track's lifecycle.
 *
 * Rather than creating an AudioResource for each video immediately and then keeping those in a queue,
 * we use tracks as they don't pre-emptively load the videos. Instead, once a Track is taken from the
 * queue, it is converted into an AudioResource just in time for playback.
 */
class Track {
    constructor({ url, title, onStart, onFinish, onError }) {
        this.url = url;
        this.title = title;
        this.onStart = onStart;
        this.onFinish = onFinish;
        this.onError = onError;
    }
    /**
     * Creates an AudioResource from this Track.
     */
    createAudioResource() {
        return new Promise((resolve, reject) => {
            const process = youtube_dl_exec_1.raw(this.url, {
                o: '-',
                q: '',
                f: 'bestaudio[ext=webm+acodec=opus+asr=48000]/bestaudio',
                r: '100K',
            }, { stdio: ['ignore', 'pipe', 'ignore'] });
            if (!process.stdout) {
                reject(new Error('No stdout'));
                return;
            }
            const stream = process.stdout;
            const onError = (error) => {
                if (!process.killed)
                    process.kill();
                stream.resume();
                reject(error);
            };
            process
                .once('spawn', () => {
                voice_1.demuxProbe(stream)
                    .then((probe) => resolve(voice_1.createAudioResource(probe.stream, { metadata: this, inputType: probe.type })))
                    .catch(onError);
            })
                .catch(onError);
        });
    }
    /**
     * Creates a Track from a video URL and lifecycle callback methods.
     *
     * @param url The URL of the video
     * @param methods Lifecycle callbacks
     * @returns The created Track
     */
    static async from(url, methods) {
        const info = await ytdl_core_1.getInfo(url);
        // The methods are wrapped so that we can ensure that they are only called once.
        const wrappedMethods = {
            onStart() {
                wrappedMethods.onStart = noop;
                methods.onStart();
            },
            onFinish() {
                wrappedMethods.onFinish = noop;
                methods.onFinish();
            },
            onError(error) {
                wrappedMethods.onError = noop;
                methods.onError(error);
            },
        };
        return new Track({
            title: info.videoDetails.title,
            url,
            ...wrappedMethods,
        });
    }
}
exports.Track = Track;
//# sourceMappingURL=track.js.map