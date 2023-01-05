import APIManager from "../APIManager.js"
import GatewayConnection from "../GatewayConnection.js"
import FormData from "../utils/FormData.js"
import Cache from "./Cache.js"

export default class MessageManager extends Cache {
  /**
   * 
   * @param {any} channel
   * @param {GatewayConnection} con
   * @param {APIManager} api
   */
  constructor(channel, con, api) {
    super()
    this.channel_id = channel.id
    this.api = api
    this.con = con
    if (con.intents.includes(GatewayConnection.INTENT_FLAGS.GUILD_MESSAGES)) {
      con.on("MESSAGE_CREATE", message => {
        if (message.channel_id !== this.channel_id) return
        this.items.set(message.id, message)
      })
      con.on("MESSAGE_UPDATE", message => {
        if (message.channel_id !== this.channel_id) return
        this.items.set(message.id, { ...this.items.get(message.id), ...message })
      })
      con.on("MESSAGE_DELETE", deleteParams => {
        if (deleteParams.channel_id !== this.channel_id) return
        this.items.delete(deleteParams.id)
      })
      con.on("MESSAGE_DELETE_BULK", deleteParams => {
        if (deleteParams.channel_id !== this.channel_id) return
        this.items.delete(deleteParams.id)
        deleteParams.ids.forEach(a => this.items.delete(a))
      })
    }
  }
  async fetchItem(id) {
    return await (await this.api.sendRequest({
      endpoint: `/channels/${this.channel_id}/messages/${id}`,
      method: "GET"
    })).json()
  }
  async add(options) {
    return await(await this.api.sendRequest({
      endpoint: `/channels/${this.channel_id}/messages`,
      method: "POST",
      payload: options instanceof FormData ? options.data : JSON.stringify(options),
      additionalHeaders: {
        "content-type": options instanceof FormData ? `multipart/form-data; boundary=${options.boundary}` : "application/json"
      }
    })).json()
  }
  async set(id, options) {
    await(await this.api.sendRequest({
      endpoint: `/channels/${this.channel_id}/messages/${id}`,
      method: "PATCH",
      payload: options instanceof FormData ? options.data : JSON.stringify(options),
      additionalHeaders: {
        "content-type": options instanceof FormData ? `multipart/form-data; boundary=${options.boundary}` : "application/json"
      }
    })).json()
  }
  delete(id) {
    return this.api.sendRequest({
      endpoint: `/channels/${this.channel_id}/messages/${id}`,
      method: "DELETE"
    })
  }
}