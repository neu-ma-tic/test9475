import APIManager from "../APIManager.js"
import GatewayConnection from "../GatewayConnection.js"
import Cache from "./Cache.js"

export default class EmojiManager extends Cache {
  /**
   * 
   * @param {GatewayConnection} con
   * @param {APIManager} api
   * @param {any} guild
   */
  constructor(con, api, guild) {
    super()
    this.guild = guild
    this.con = con
    this.api = api
  }
  fetchItem(id) {
    return api.sendRequest({
      endpoint: `/guilds/${this.guild.id}/emojis/${id}`,
      method: "GET"
    })
  }

}