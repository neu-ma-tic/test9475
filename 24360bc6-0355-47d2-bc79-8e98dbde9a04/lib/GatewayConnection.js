import { EventEmitter } from "node:events"
import WebSocket from "./ws/WebsocketClient.js"
const BASE_URL = "wss://gateway.discord.gg/"
const VERSION = "10"
const ERROR_WS_CLOSE_CODES = [4004, 4011, 4012, 4014, 4013]
import process from 'process'
const WS_ERRORS = {
  4004: "You specified a invalid token",
  4011: "Sharding is required",
  4012: "The API Version is invalid",
  4013: "The intent bitwise value was caclulated improperly",
  4014: "YOu specified a priviledged intent you aren't whitelisted for or haven't enabled"
}
/**
 * A Gateway connection wtih no sharding
 * @extends EventEmitter
 */
class GatewayConnection extends EventEmitter {
  /**
   * The intents flags documented
   * @typedef {number} IntentFlag
   */
  static INTENT_FLAGS = {
    GUILDS: 1 << 0,
    GUILD_MEMBERS: 1 << 1,
    GUILD_BANS: 1 << 2,
    GUILD_EMOJIS_AND_STICKERS: 1 << 3,
    GUILD_INTERGRATIONS: 1 << 4,
    GUILD_WEBHOOKS: 1 << 5,
    GUILD_INVITES: 1 << 6,
    GUILD_VOICE_STATES: 1 << 7,
    GUILD_PRESENCES: 1 << 8,
    GUILD_MESSAGES: 1 << 9,
    GUILD_MESSAGE_REACTIONS: 1 << 10,
    GUILD_MESSAGE_TYPING: 1 << 11,
    DIRECT_MESSAGES: 1 << 12,
    DIRECT_MESSAGE_REACTIONS: 1 << 13,
    DIRECT_MESSAGE_TYPING: 1 << 14,
    MESSAGE_CONTENT: 1 << 15,
    GUILD_SCHEDULED_EVENTS: 1 << 16,
    AUTO_MODERATION_CONFIGURATION: 1 << 20,
    AUTO_MODERATION_EXECUTION: 1 << 21
  }
  /**
   * The statuses of the GatewayConnection
   * @typedef {string} Status
   */
  static STATUS = {
    /**
     * The connection is connected
     * @type {Status}
     */
    CONNECTED: "CONNECTED",
    /**
     * The connectoin is identifying
     * @type {Status}
     */
    IDENTIFYING: "IDENTIFYING",
    /**
     * The connection has been severed (somehow) but can still resume. It is attempting to reconnect and transmit a RESUME call.
     * @type {Status}
     */
    RECONNECTING: "RECONNECTING",
    /**
     * The connection was not connected.
     * @type {Status}
     */
    DISCONNECTED: "DESTROYED"
  }
  /**
   * The Gateway Opcodes
   * @typedef {number} GatewayOpcode
   */
  static OPCODES = {
    /**
     * Used when the gateway sends the event
     * @type {GatewayOpcode}
     */
    DISPATCH: 0,
    /**
     * When sent by the gateway: You should send a heartbeat immediately
     * This should be sent by the client when the gateway requestss a heartbeat or according the the heartbeat timer
     * @type {GatewayOpcode}
     */
    HEARTBEAT: 1,
    /**
     * Sent by the client to authenticate
     * @type {GatewayOpcode}
     */
    IDENTIFY: 2,
    /**
     * Sent by the client to update their presence
     * @type {GatewayOpcode}
     */
    UPDATE_PRESENCE: 3,
    /**
     * Sent by the client when they want to join a voice channel
     * @type {GatewayOpcode}
     */
    VOICE_STATE_UPDATE: 4,
    /**
     * Sent by the client if they want to resumw
     * @type {GatewayOpcode}
     */
    RESUME: 6,
    /**
     * Sent by the gateway meaning you should reconnect and identify/resume the connection
     * @type {GatewayOpcode}
     */
    RECONNECT: 7,
    /**
     * Sent by the client if they want to request certain guild members
     * @type {GatewayOpcode}
     */
    REQUEST_GUILD_MEMBERS: 8,
    /**
     * Sent by the gateway if they need to reconnect resume/identify
     * @type {GatewayOpcode}
     */
    INVALID_SESSION: 9,
    /**
     * Sent by the gateway to provide the heartbeat timer
     * @type {GatewayOpcode}
     */
    HELLO: 10,
    /**
     * Sent by the gateway when they acknowledge that you sent a heartbeat
     * @type {GatewayOpcode}
     */
    HEARTBEAT_ACK: 11
  }
  /**
   * The statuses to choose when chainging presences
   * @typedef {string} PresenceStatus The presence status
   */
  static PRESENCE_STATUS = {
    /**
     * The user is online
     * @type {PresenceStatus}
     */
    ONLINE: "online",
    /**
     * Do not disturb
     * @type {PresenceStatus}
     */
    DND: "dnd",
    /**
     * The user is afk...
     * @type {PresenceStatus}
     */
    IDLE: "idle",
    /**
     * The user is offline, but isn't actually offline
     * @type {PresenceStatus}
     */
    INVISIBLE: "invisible",
    /**
     * The user is offline
     * @type {PresenceStatus}
     */
    OFFLINE: "offline"
  }
  /**
   * Sends debug info
   * @private
   * @param {string} msg The message to send
   * @returns {void}
   */
  debug(msg) {
    /**
     * Fired when a debug message is sent
     * @event GatewayConnection#debug
     * @param {string} msg The debug message sent
     */
    this.emit("debug", msg)
  }
  /**
   * The bot's activity
   * @typedef {Object} Activity
   * @property {string} name The activity's name
   * @property {number} type The activity type
   * @property {string} [url] The stream url. Is validated when type is 1
   */
  /**
   * The presence of the bot
   * @typedef {Object} Presence
   * @property {?number} since Unix time since the client was idle. Null if it isn't idlle
   * @property {Array<Activity>} activities The user's activities
   * @property {PresenceStatus} status The user's status
   * @property {boolean} afk Whether the client is afk
   */
  /**
   * @param {string} token The token to log in as
   * @param {Object} options Options for connecting
   * @param {Array<IntentFlag>} options.intents The intents for connecting to the gateway
   * @param {Presence} [options.presence={since: null, activities: [], status: "online", afk: false}] The presence to start with.
   * @param {boolean} [options.showSensitiveData=false] Whether to show sensitive data
   */
  constructor(token, options) {
    super()
    // Argument Checks
    if (options.intents == undefined) throw new TypeError("options.intents is required")
    if (!Array.isArray(options.intents)) throw new TypeError("options.intents must be an array")
    var values = Object.values(GatewayConnection.INTENT_FLAGS)
    options.intents.forEach(flag => {
      if (!values.includes(flag)) throw new TypeError("options.intents includes something not listed")
    })
    if (options.presence) {
      if (typeof options.presence.since !== "number" && options.presence.since !== null) throw new TypeError("options.presence.since must be a string")
      if (!Object.values(GatewayConnection.PRESENCE_STATUS).includes(options.presence.status)) throw new TypeError("options.presence.status must be a valid status")
      if (typeof options.presence.afk !== "boolean") throw new TypeError("options.presence.afk must be a boolean")
      if (!Array.isArray(options.presence.activities)) throw new TypeError("options.presence.activities must be an array")
      options.presence.activities.forEach((a, i) => {
        if (a.url !== undefined && typeof a.url !== "string") throw new TypeError("options.presence.activities[" + i + "].url must be an array")
        if (typeof a.type !== "number") throw new TypeError("options.presence.activities[" + i + "].type must be a number")
        if (typeof a.name !== "string") throw new TypeError("options.presence.activities[" + i + "].name must be a string")
      })
    }
    /**
     * The current bot's presence
     * @type {Presence}
     */
    this.presence = options.presence || { since: null, activities: [], status: "online", afk: false }
    /** 
     * The connection the gateway connection is using
     * @type {?WebSocket}
     * @private
     */
    this.con = null
    /**
     * The sequence number of the gateway connection. Used for resuming and heartbeats
     * @type {?number}
     * @private
     */
    this.seq = null
    /**
     * The session id for the gateway connection
     * @type {?string}
     * @private
     */
    this.session_id = null
    /**
     * The status of the Gateway Connection
     * @type {Status}
     */
    this.status = GatewayConnection.STATUS.DISCONNECTED
    /**
     * The client token
     * @type {string}
     */
    this.token = token
    /**
     * The array of Intent Flags sent to the gateway. Changing it will impact the next IDENTIFY Call.
     * @type {Array<IntentFlag>}
     */
    this.intents = options.intents
    /**
     * Whether the gateway acknowledged that we sent a heartbeat
     */
    this.lastHeartbeatAck = false
    /**
     * The time the last heartbeat was sent
     * @private
     * @type {number}
     */
    this.lastHeartbeatTime = null
    /**
     * The latency
     * @type {number}
     */
    this.latency = 0
    /**
     * The applicationID of the client
     * @type {string}
     */
    this.applicationID = null
    /**
     * The bit number of intents
     * @name WebsocketShard#intentBitNumber
     * @readonly
     */
    Object.defineProperty(this, "intentBitNumber", {
      get() {
        var intents = 0
        this.intents.forEach((flag) => {
          intents |= flag
        })
        return intents
      }
    })
    /**
     * The ratelimit queue
     * @private
     */
    this.ratelimit = {
      /**
       * The number of payloads remaining
       * @type {number}
       */
      remaining: 120,
      /** 
       * The payload queue
       * @type {Array<GatewayPayload>}
       */
      queue: [],
      /**
       * The total number of payloads you can send per `time` milliseconds
       * @type {number}
       */
      total: 120,
      /**
       * @type {number}
       */
      time: 60e+3, /* when the scientific notation */
      /**
       * @type {?NodeJS.Timeout}
       */
      timer: null
    }
    /**
     * The heartbeat timer
     * @private
     * @type {?NodeJS.Timeout}
     */
    this.heartbeatTimer = null
    /**
     * Whether to show sensitive data
     * @type {boolean}
     */
    this.showSensitiveData = options.showSensitiveData || false
    /**
     * The guild memebers waiting to be recieved
     * @type {Map<string, Object>}
     */
    this.requestGuildMemberQueue = new Map()
    /**
     * The resume URL of the gateway
     * @type {?string}
     */
    this.resumeURL = null
  }
  /**
   * @private
   * @param {number} interval The heartbeat interval. Set to -1 to clear
   */
  setHeartbeatInterval(interval) {
    if (this.heartbeatTimer) clearInterval(this.heartbeatTimer)

    if (interval == -1) return this.debug("[HEARTBEAT] Clearing heartbeat interval")
    this.debug("[HEARTBEAT] Setting heartbeat interval to " + interval)
    this.heartbeatTimer = setInterval(() => this.sendHeartbeat(), interval).unref()
  }
  /**
   * Sends a heartbeat
   * @param {boolean} [ignoreHeartbeatAck=false] whether to not check Heartbeat ack
   * @private
   */
  sendHeartbeat(ignoreHeartbeatAck = false) {
    if (!ignoreHeartbeatAck && !this.lastHeartbeatAck) {
      this.debug("[HEARTBEAT] Didn't recieve a heartbeat ACK since the last one. DIsconnecting")
      this.disconnect({
        code: 4009,
        reconnect: true
      })
      return;
    }
    this.debug("[HEARTBEAT] Sequence: " + this.seq)
    this.lastHeartbeatTime = Date.now()
    this.lastHeartbeatAck = false
    this.sendMessage({
      op: GatewayConnection.OPCODES.HEARTBEAT,
      d: this.seq
    })
  }
  /**
   * Transmits a identify/resume call 
   * @private
   * @returns {void}
   */
  identify() {
    if (this.session_id) return this.identifyResume()
    this.identifyNew()
  }
  /**
   * Identifies as a brand new session
   * @private
   * @returns {void}
   */
  identifyNew() {
    this.debug(`[IDENTIFY]
  token: ${this.showSensitiveData ? this.token : "xxxxxxxxxx.xxx.xxxxxxxxxx"}
  intents: ${this.intentBitNumber}
  presence: ${JSON.stringify(this.presence, null, 2)}`)
    this.sendMessage({
      op: GatewayConnection.OPCODES.IDENTIFY,
      d: {
        token: this.token,
        properties: {
          os: process.platform,
          version: "nodejs",
          library: "nodejs"
        },
        intents: this.intentBitNumber,
        presence: this.presence
      }
    }, true)
  }
  /**
   * 
   */
  identifyResume() {
    if (!this.session_id) {
      this.debug("[RESUME] No session_id was found, so idenitfying as a brand new connection")
      this.identifyNew()
      return
    }
    this.debug(`[RESUME]
  token: ${this.showSensitiveData ? this.token : "xxxxxxxxxx.xxx.xxxxxxxxxx"}
  session_id: ${this.session_id}
  seq: ${this.seq}`)
    this.sendMessage({
      op: GatewayConnection.OPCODES.RESUME,
      d: {
        token: this.token,
        session_id: this.session_id,
        seq: this.seq
      }
    }, true)
  }
  /**
   * Connects to the gateway
   * @private
   * @returns {void}
   */
  connect() {
    this.debug(`[CONNECTING] Connecting to ${this.resumeURL ? this.resumeURL : BASE_URL}?v=${VERSION}&encoding=json`)
    this.con = new WebSocket((this.resumeURL ? this.resumeURL : BASE_URL) + `?v=${VERSION}&encoding=json`)
    this.con.on("message", this.onWSPacket.bind(this))
    this.con.on("close", this.onClose.bind(this))
    this.con.on("error", e => {
      this.debug("[SOCKET_ERROR] " + e.toString())
    })
  }
  /**
   * Called when the gateway sends a message
   * @param {Buffer} msg The buffer the gateway sent
   */
  onWSPacket(msg) {
    var packet = JSON.parse(msg.toString())
    this.onMessage(packet)
  }
  /**
   * 
   * @param {Presence} presence The presence to set to
   */
  setPresence(presence) {
    this.presence = presence
    this.sendMessage({
      op: GatewayConnection.OPCODES.UPDATE_PRESENCE,
      d: presence
    })
  }
  /**
   * options for disconnect function
   * @typedef {Object} destroyOptions
   * @property {number} [code=1000] The code for closing
   * @property {boolean} [reconnect=false] Whether to reconnect and identify/resume accordingly
   * @property {boolean} [resume=true] Whether to resume/identify after the next connection
   */
  /**
   * disconnects the thing
   * @param {destroyOptions} options 
   */
  disconnect({ code = 1000, reconnect = false, resume = true } = {}) {
    this.debug(`[DISCONNECT]
  code: ${code}
  reconnect: ${reconnect}
  resume: ${resume}`)
    // close the websocket if it's still open
    if (this.con.readyState === WebSocket.OPEN) this.con.close(code)
    this.con = null
    this.setHeartbeatInterval(-1)
    if (this.ratelimit.timer) clearInterval(this.ratelimit.timer)
    this.ratelimit = {
      remaining: 120,
      queue: [],
      total: 120,
      time: 60e+3, /* when the scientific notation */
      timer: null
    }
    if (!resume) {
      this.session_id = null
      this.seq = null
      this.resumeURL = null
    }
    if (reconnect) {
      this.debug("[RECONNECT] Reconnecting")
      this.connect()
    }
  }
  /**
   * Gateway payload format
   * @typedef {Object} GatewayPayload
   * @property {GatewayOpcode} op The opcode for the payoad
   * @property {Object|boolean|number} d Any Object (data to send/recieve from gateway)
   * @property {?number} s Sequence number used for resuming & sending heartbeats. Only present when op is 0
   * @property {?string} t The event name. Only present when op is 0.
   */
  /**
   * Called when the gateway sends a message and it is parsed successfully
   * @private
   * @param {GatewayPayload} msg The message sent
   * @returns {void}
   */
  onMessage(msg) {
    this.debug(this.showSensitiveData ? "[MESSAGE] >> " + JSON.stringify(msg) : ("[MESSAGE] >> " + JSON.stringify(msg)).replace(new RegExp(this.token, "g"), "xxxxxxxxxx.xx.xxxxxxxxxx"))
    switch (msg.t) {
      case "READY":
        this.debug("[READY]")
        this.session_id = msg.d.session_id
        this.resumeURL = msg.d.resume_gateway_url
        this.applicationID = msg.d.application.id
        this.sendHeartbeat(true)
        break;
      case "RESUMED":
        this.sendHeartbeat(true)
        break;
      case "GUILD_MEMBERS_CHUNK":
        if (!this.requestGuildMemberQueue.has(msg.d.nonce)) return;
        var req = this.requestGuildMemberQueue.get(msg.d.nonce)
        console.log(msg.d)
        req.members = req.members.concat(msg.d.members)
        req.presences = req.presences.concat(msg.d.presences == undefined? [] : msg.d.presences)
        if (msg.d.chunk_index == msg.d.chunk_count - 1) return req.resolve({members: req.members, presences: req.presences})
        this.requestGuildMemberQueue.set(msg.d.nonce, req)
    }
    switch (msg.op) {
      case GatewayConnection.OPCODES.DISPATCH:
        this.emit(msg.t, msg.d)
        if (msg.s > this.seq) this.seq = msg.s
        this.debug("[DISPATCH] Event name:" + msg.t)
        break;
      case GatewayConnection.OPCODES.HELLO:
        this.setHeartbeatInterval(msg.d.heartbeat_interval)
        this.identify()
        break;
      case GatewayConnection.OPCODES.HEARTBEAT:
        this.debug("[HEARTBEAT] Discord told us to send one, so we did")
        this.sendHeartbeat(true)
        break;
      case GatewayConnection.OPCODES.HEARTBEAT_ACK:
        this.lastHeartbeatAck = true
        this.latency = Date.now() - this.lastHeartbeatTime
        this.debug("[HEARTBEAT] Heartbeat acknowledged. Latency: " + this.latency.toString() + "ms")
        break;
      case GatewayConnection.OPCODES.INVALID_SESSION:
        this.debug("[INVALID_SESSION] Can resume: " + msg.d)
        this.disconnect({
          code: 4000,
          reconnect: true,
          resume: msg.d
        })
        break;
      case GatewayConnection.OPCODES.RECONNECT:
        this.debug("[RECONNECT] Discord asked us to reconnect, and we did so accordingly")
        this.disconnect({
          code: 4000,
          reconnect: true
        })
        break;
    }
  }
  /**
   * Called when the websocket is closed
   * @private
   * @param {number} code The close code
   * @param {string} reason A more detailed explanation
   * @returns {void}
   */
  onClose({ code, reason }) {
    this.debug(`[CLOSE] Gateway closed
  code: ${code}
  reason: ${reason}`)
    if (ERROR_WS_CLOSE_CODES.includes(code)) return this.emit("error", new Error(WS_ERRORS[code]))
    if (code == 1006) this.connect()
  }
  /**
   * Proceses the ratelimit queue
   * @private
   * @returns {void}
   */
  processQueue() {
    // ratelimit got exceeded
    if (this.ratelimit.remaining === 0) return;
    // it is basically empty
    if (this.ratelimit.queue.length === 0) return;
    if (this.ratelimit.total === this.ratelimit.remaining) {
      this.ratelimit.timer = setTimeout(() => {
        this.ratelimit.remaining = this.ratelimit.total
        this.processQueue()
      }, this.ratelimit.time).unref()
    }
    while (this.ratelimit.remaining > 0 && this.ratelimit.queue.length !== 0) {
      var payload = this.ratelimit.queue.shift()
      this._send(payload)
      this.ratelimit.remaining--
    }
  }
  /**
   * Queues a message to send to the gateway
   * If you are using this command, make sure you know what ur doing.
   * @private
   * @param {GatewayPayload} msg The message to send
   * @param {boolean} [prioritize=false] Whether to send the message first and above anything else
   * @returns {void}
   */
  sendMessage(msg, prioritize = false) {
    this.ratelimit.queue[prioritize ? "unshift" : "push"](msg)
    this.processQueue()
  }
  /**
   * Sends a message to send to the gateway without queuing
   * @private
   * @param {GatewayPayload} msg The message to send
   * @returns {void}
   */
  _send(msg) {
    this.debug(this.showSensitiveData ? "[MESSAGE] << " + JSON.stringify(msg) : ("[MESSAGE] << " + JSON.stringify(msg)).replace(new RegExp(this.token, "g"), "xxxxxxxxxx.xx.xxxxxxxxxx"))
    this.con.send(JSON.stringify(msg))
  }
  /**
   * Options for requesting guild members
   * @typedef {Object} getGuildGuildMembersOptions
   * @property {string} guild_id the guild id to get guild members
   * @property {string} [query=""] Filters out members who don't match that name. user_ids and querys cannot be present at the same time
   * @property {boolean} [showPresences=false] showPressenses Whether to show user pressences.
   * @property {(Array<string>|string)} [user_ids] The user_ids to retrieve. user_ids and querys cannot be present at the same time
   * @property {number} [limit=100] The max numbers of guild members to retrieve
   */

  /**
   * 
   * @param {getGuildGuildMembersOptions} options The options for requesting guild members
   * @returns {Promise<Array<Object>>} An array of guild members
   * @returns {void}
   */
  getGuildMembers({ guild_id, query, showPresences = false, user_ids, limit = 100 }) {
    return new Promise((resolve, reject) => {
      if (typeof guild_id !== "string" && !(guild_id instanceof String)) return reject(new TypeError("guild_id must be a string"))
      if (query && user_ids) return reject(new Error("query and user_ids cannot exist at the same time"))
      if (showPresences && !this.intents.includes(GatewayConnection.INTENT_FLAGS.GUILD_PRESENCES)) console.warn("[WARN] You won't recieve guild presences if you don't have the GUILD_PRESENCES intent")
      var payloadData = {}
      payloadData.guild_id = guild_id
      payloadData.presences = showPresences
      payloadData.nonce = (Date.now() - 1420070400000).toString()
      if (typeof user_ids !== "undefined") {
        if (!Array.isArray(user_ids) && typeof user_ids != "string") throw new TypeError("user_ids must be an array or a string")
        if (Array.isArray(user_ids)) {
          if (user_ids.length > 100) reject(new RangeError("user_ids is limited to below 100 members"))
          user_ids.forEach((v, i) => {
            if (typeof v !== "string" && !(v instanceof String)) throw new TypeError(`options.user_ids[${i.toString()}] must be a string`)
          })
        }
        payloadData.user_ids = user_ids
      } else {
        if (typeof query != "string") return reject(new TypeError("query must be a string"))
        if (query == "" && limit == 0 && !this.intents.includes(GatewayConnection.INTENT_FLAGS.GUILD_MEMBERS)) return reject(new RangeError("You need the GUILD_MEMBERS intent to request all of the members"))
        payloadData.limit = limit
        payloadData.query = query || ""
      }
      this.requestGuildMemberQueue.set(payloadData.nonce, { resolve, reject, showPresences, members: [], presences: [] })
      this.sendMessage({ op: 8, d: payloadData })
    })
  }
}
export default GatewayConnection