import fetch from "node-fetch"
const BASE_URL = "https://discord.com/api/v10/"
import EventEmitter from "node:events"
/**
 * An api manager w/ implemented ratelimiting
 */
class APIManager extends EventEmitter {

  /**
   * A request at queue
   * @typedef {Object} Request
   * @property {string} method The method of the request
   * @property {string} endpoint The endpoint to send to
   * @property {Object} payload The payload to JSON.stringfify as
   * @property {Object.<string, string>} additionalHeaders Additional headers for the request
   * @property {Function} resolve The function that resolves the promise
   * @property {Function} reject Rejects a promise
   */
  /**
   * 
   * @param {string} token Your bot's token
   */
  constructor(token) {
    super()
    /**
     * @private
     * @typedef {Object} endpointSpecificRatelimit
     * @property {boolean} ratelimited Whether the specific  group of endpoints are ratelimit
     * @property {Array<Request>} queue The queue of the group of endpoints
     * @property {?NodeJS.Timeout} timer The timer, if applicable
     * @property {boolean} processing Whether the queue is being processed.
    */
    this.token = token
    /**
     * @private
     * A collection of buckets corresponding to a ratelimit
     * @type {Object.<string, endpointSpecificRatelimit>}
     */
    this.bucketRatelimits = {}
    /**
     * Global ratelimit ()
     * @private
     */
    this.globalRatelimit = {
      /**
       * The total amount of requests you can make before having to wait `time` milliseconds
       * @private
       * @readonly
       * @type {number}
       */
      total: 50,
      /**
       * The remaining amount of requests you can make before having to wait `time` milliseconds
       * @private
       * @type{number}
       */
      remaining: 50,
      /**
       * The time the ratelimit resets
       * @type {number}
       * @private
       * @readonly
       */
      time: 1e+3,
      /**
       * The timer to handle ratelimit reset
       * @type {NodeJS.Timeout}
       * @private
       */
      timer: null,
      queue: []
    }
    /**
     * @private
     * @type {Map<string, string>}
     */
    this.endpointBucketMap = new Map()
  }
  /**
   * Sends a request
   * @param {Request} request The request to send
   * @returns {Response}
   */
  sendRequest(request) {
    return new Promise((r, er) => {
      request.resolve = r
      request.reject = er
      this.globalRatelimit.queue.push(request)
      this.processGlobalQueue()
    })
  }
  /**
   * Fires a debug event
   * @param {string} debug The debug message to send
   * @private
   * @fires APIManager#debug
   */
  _debug(debug) {
    /**
     * Debug BS
     * @event APIManager#debug
     * @param {string} debug The debug thing
     */
    this.emit("debug", debug)
  }
  /**
   * Processes the global queue
   * @private
   */
  async processGlobalQueue() {
    if (this.globalRatelimit.remaining == 0) return;
    if (this.globalRatelimit.queue.length == 0) return;
    if (this.globalRatelimit.total == this.globalRatelimit.remaining) {
      if (this.globalRatelimit.timer) clearTimeout(this.globalRatelimit.timer)
      this.timer = setTimeout(() => {
        this.globalRatelimit.remaining = this.globalRatelimit.total
        this.processGlobalQueue()
      })
    }
    while (this.globalRatelimit.remaining > 0 && this.globalRatelimit.queue.length > 0) {
      var request = this.globalRatelimit.queue.shift()
      if (!this.endpointBucketMap.has(request.endpoint)) {
        //console.log("requesting")
        await this._request(request)
        continue;
      }
      this.bucketRatelimits[this.endpointBucketMap.get(request.endpoint)].queue.push(request)
      this.processBucketQueue(this.endpointBucketMap.get(request.endpoint))
      this.globalRatelimit.remaining--
    }
  }
  /**
   * Launches a request to the Discord API
   * @private
   * @param {Request} request
   * @returns {Promise<fetch.Response>} The response from the discord API
   */
  async _request(request) {
    this._debug(`[REQUEST]
  Endpoint: ${request.endpoint}
  Method ${request.method}`)
    var endpoint = ""
    if (request.endpoint.startsWith("/")) { endpoint = request.endpoint.substring(1) }
    var url = new URL(endpoint, BASE_URL)
    if (!request.hasOwnProperty("additionalHeaders")) request.additionalHeaders = {}
    var options = {
      method: request.method,
      headers: {
        Authorization: "Bot " + this.token,
        "User-Agent": "NodeJS (https://nodejs.org, v15)",
        "Content-Type": "application/json",
        ...request.additionalHeaders
      }
    }
    if (request.hasOwnProperty("payload")) options.body = request.payload
    var res1 = await fetch(url.toString(), options)
    var res2 = res1.clone()
    var headers = res1.headers
    if (!res1.ok) {
      if (res1.status == 429) {
        this.onRatelimited({
          retry_after: headers.get("x-ratelimit-reset-after"),
          global: headers.get("x-ratelimit-global") == "true",
          bucket: headers.get("x-ratelimit-bucket"),
          request: request,
          cloudflareBanned: headers.get("content-type").startsWith("text/html")
        })
        return;
      }
      request.reject(new Error(res1.status + ": " + await res1.text()))
    }
    if (!this.endpointBucketMap.has(request.endpoint)) {
      this.endpointBucketMap.set(request.endpoint, headers.get("x-ratelimit-bucket"))
    }
    this.onResponse({
      bucket: headers.get("x-ratelimit-bucket"),
      remaining: headers.get("x-ratelimit-remaining"),
      resetAfter: parseInt(headers.get("x-ratelimit-reset-after"))
    })
    request.resolve(res2)
    return "all clear"
  }
  /**
   * Called when it is ratelimited
   * @param {Object} options The circumstances of the ratelimit
   * @param {number} options.retry_after When to retry retry_after
   * @param {boolean} [options.global=false] When the ratelimit is global. options.bucket will be ignored if this is true
   * @param {string} options.bucket The bucket that is ratellimited, if it isn't global
   * @param {Request} options.request The request
   * @param {boolean} options.cloudflareBanned Whether the request got CF banned
   * @private
   */
  onRatelimited({ retry_after, global = false, bucket, request, cloudflareBanned }) {
    if (cloudflareBanned) {
      this._debug(`[RESPONSE] We got Cloudflare Banned. Should retry in 10 minutes`)
      this.globalRatelimit.remaining = 0
      this.globalRatelimit.queue.push(request)
      if (this.globalRatelimit.timer) clearTimeout(this.globalRatelimit.timer)
      this.globalRatelimit.timer = setTimeout(() => {
        this.globalRatelimit.remaining = this.globalRatelimit.total
        this.processGlobalQueue()
      }, 600000)
      return;
    }
    if (global) {
      this._debug(`[RESPONSE] We got ratelimited globally. Should retry after in ${retry_after} seconds`)
      this.globalRatelimit.remaining = 0
      this.globalRatelimit.queue.push(request)
      if (this.globalRatelimit.timer) clearTimeout(this.globalRatelimit.timer)
      this.globalRatelimit.timer = setTimeout(() => {
        this.globalRatelimit.remaining = this.globalRatelimit.total
        this.processGlobalQueue()
      }, retry_after * 1000 + 100)
      return;
    }
    this._debug(`[RESPONSE] We got ratelimited on that route
  Bucket: ${bucket}
  Retry after in ${retry_after} seconds`)
    this.bucketRatelimits[bucket].ratelimited = true
    if (this.bucketRatelimits[bucket].timer) clearTimeout(this.bucketRatelimits[bucket].timer)
    this.bucketRatelimits[bucket].queue.push(request)
    this.bucketRatelimits[bucket].timer = setTimeout(() => {
      this.bucketRatelimits[bucket].ratelimited = false;
      this.processBucketQueue(bucket)
    }, retry_after * 1000 + 100)
  }
  /**
   * Processes the queue for the specific bucket
   * @param {string} The bucket to do
   * @private
   */
  async processBucketQueue(bucket) {
    //console.log(bucket, this.bucketRatelimits[bucket])
    if (this.bucketRatelimits[bucket].ratelimited || this.bucketRatelimits[bucket].processing)
      return;
    if (this.bucketRatelimits[bucket].queue.length == 0) return;
    this.bucketRatelimits[bucket].processing = true
    while (this.bucketRatelimits[bucket].queue.length > 0 && !this.bucketRatelimits[bucket].ratelimited) {
      //console.log(this.bucketRatelimits[bucket].ratelimited)
      var request = this.bucketRatelimits[bucket].queue.shift()
      await this._request(request)
    }
    //console.log("stopped processing")
    this.bucketRatelimits[bucket].processing = false
  }
  /**
   * Called when a respnose is made
   * @private
   */
  onResponse({ bucket, remaining, resetAfter }) {
    this._debug(`[RESPONSE] Request finished:
  Bucket: ${bucket}
  Remaining amount: ${remaining}
  Ratelimit will reset in ${resetAfter} seconds`)
    if (!this.bucketRatelimits.hasOwnProperty(bucket)) {
      this.bucketRatelimits[bucket] = {
        ratelimited: remaining == 0,
        queue: [],
        timer: remaining == 0 ?  setTimeout(() => {
          //console.log("unratelimited")
          this.bucketRatelimits[bucket].ratelimited = false;
          this.processBucketQueue(bucket)
        }, resetAfter * 1000 + 100).unref() : null,
        processing: false
      }
      return;
    }
    if (remaining == 0) {
      //console.log("get ratelimited lol")
      this.bucketRatelimits[bucket].ratelimited = true
      if (this.bucketRatelimits[bucket].timer) clearTimeout(this.bucketRatelimits[bucket].timer)
      this.bucketRatelimits[bucket].timer = setTimeout(() => {
        //console.log("unratelimited")
        this.bucketRatelimits[bucket].ratelimited = false;
        this.processBucketQueue(bucket)
      }, resetAfter * 1000 + 100).unref()
    }
  }
}
export default APIManager