import EventEmitter from "node:events"
import APIManager from "./APIManager.js"
import GatewayConnection from "./GatewayConnection.js"
export default class Client extends EventEmitter {
  /**
   * @param {string} token The token to log in as
   * @param {Object} options Options for connecting
   * @param {Array<IntentFlag>} options.intents The intents for connecting to the gateway
   * @param {Presence} [options.presence={since: null, activities: [], status: "online", afk: false}] The presence to start with.
   */
  constructor(token, { intents, presence = { since: null, activities: [], status: "online", afk: false } }) {
    /**
     * @private
     * @type {APIManager}
     */
    this._api = new APIManager(token)
    /**
     * @private
     * @type {GatewayConnection}
     */
    this._con = new GatewayConnection({ intents, presence })
    this._con.connect()
  }
}