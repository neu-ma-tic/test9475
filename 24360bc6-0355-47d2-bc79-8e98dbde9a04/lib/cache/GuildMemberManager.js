import APIManager from "../APIManager.js"
import GatewayConnection from "../GatewayConnection.js"
import Cache from "./Cache.js"

export default class GuildMemberManager extends Cache {
  /**
   * 
   * @param {APIManager} api
   * @param {GatewayConnection} con
   * @param {object} guild
   */
  constructor(con, api, guild) {
    super()
    this.api = api
    this.con = con
    this.guild_id = guild.id
    if (guild.members) {
      for (let i of guild.members) {
        this.items.set(i.user.id, Member(i, guild))
      }
    }
    if (con.intents.includes(GatewayConnection.INTENT_FLAGS.GUILDS)) {
      this.con.on("GUILD_MEMBER_ADD", data => {
        if (data.guild_id !== this.guild_id) return;
        this.items.set(data.user.id, Member(data, guild))
      })
      this.con.on("GUILD_MEMBER_UPDATE", data => {
        if (data.guild_id !== this.guild_id) return;
        this.items.set(data.user.id, Member(data, guild))
      })
      this.con.on("GUILD_MEMBER_REMOVE", data => {
        if (data.guild_id !== this.guild_id) return;
        this.items.delete(data.user.id)
      })
    }
  }
  async fetchItem(id) {
    return await (await this.api.sendRequest({
      endpoint: `/guilds/${this.guild_id}/members/${id}`,
      method: "GET"
    })).json()
  }
  async delete(id) {
    return await this.api.sendRequest({
      endpoint: `/guilds/${this.guild_id}/members/${id}`,
      method: "DELETE"
    })
  }
}
function computePerms(member, roles, guild_id) {
  var permissions = roles.items.get(guild_id).permissions
  for (let i of member.roles) {
    var role = roles.items.get(i)
    if(role.permissions & 8) return 2**42-1
    permissions |= role.permissions
  }
  return permissions
}
function Member(data, guild) {
  var member = data
  if (!member.hasOwnProperty("permissions")) {
    Object.defineProperty(member, "permissions", {
      get() {
        return computePerms(member, guild.roles, guild.id)
      }
    })
  }
  return member
}