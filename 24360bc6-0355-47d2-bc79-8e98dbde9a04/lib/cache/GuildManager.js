import APIManager from "../APIManager.js"
import GatewayConnection from "../GatewayConnection.js"
import Cache from "./Cache.js"
import GuildChannelManager from "./GuildChannelManager.js"
import GuildMemberManager from "./GuildMemberManager.js"
import RoleManager from "./RoleManager.js"

export default class GuildManager extends Cache {
  /**
   * 
   * @param {GatewayConnection} con
   * @param {APIManager} api
   */
  constructor(con, api) {
    super()
    this.con = con
    this.api = api
    if (con.intents.includes(GatewayConnection.INTENT_FLAGS.GUILDS)) {
      con.on("GUILD_CREATE", data => {
        var guild = Guild(data, this.con, this.api, data.channels);
        this.items.set(guild.id, guild)
      })
      con.on("GUILD_UPDATE", data => {
        this.items.set(data.id, {...this.items.get(data.id), ...data})
      })
      con.on("GUILD_DELETE", data => {
        this.items.delete(data.id)
      })
    }
  }
  async fetchItem(id) {
    return Guild(await (await this.api.sendRequest({
      endpoint: `/guilds/${id}`,
      method: "GET"
    })).json(), this.con, this.api)
  }
}
function Guild(data, con, api) {
  var guild = data
  data.channels = data.channels instanceof GuildChannelManager ? data.channels : new GuildChannelManager(con, api, data)
  data.roles = new RoleManager(con, api, data)
  data.members = new GuildMemberManager(con, api, data)
  return guild
}