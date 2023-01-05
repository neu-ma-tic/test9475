import Database from "@replit/database"
const emojiRegex = /^<a?:(.+):(\d+)>$/
const unicodeEmojiRegex = /^[\u{1f300}-\u{1f5ff}\u{1f900}-\u{1f9ff}\u{1f600}-\u{1f64f}\u{1f680}-\u{1f6ff}\u{2600}-\u{26ff}\u{2700}-\u{27bf}\u{1f1e6}-\u{1f1ff}\u{1f191}-\u{1f251}\u{1f004}\u{1f0cf}\u{1f170}-\u{1f171}\u{1f17e}-\u{1f17f}\u{1f18e}\u{3030}\u{2b50}\u{2b55}\u{2934}-\u{2935}\u{2b05}-\u{2b07}\u{2b1b}-\u{2b1c}\u{3297}\u{3299}\u{303d}\u{00a9}\u{00ae}\u{2122}\u{23f3}\u{24c2}\u{23e9}-\u{23ef}\u{25b6}\u{23f8}-\u{23fa}$]/u
const messageURLTestRegex = /^https:\/\/discord.com\/channels\/([0-9]+)\/([0-9]+)\/([0-9]+)$/
var messageURLRegex = /https:\/\/discord.com\/channels\/([0-9]+)\/([0-9]+)\/([0-9]+)/
export default async function (interaction, options, { api, con, guilds, database }) {
  messageURLRegex.lastIndex = 0
  console.log(options)
  if (options.subCmdInvoked == "set") {
    console.log(emojiRegex.test(options.options.emoji))
    if (!messageURLTestRegex.test(options.options.message)) return interaction.respond(4, { content: "Message URL is not valid" })
    if (!emojiRegex.test(options.options.emoji) && !unicodeEmojiRegex.test(options.options.emoji)) return interaction.respond(4, { content: "This is not a valid emoji" })
    var matches = messageURLRegex.exec(options.options.message)
    console.log(matches, options.options.message)
    var guildID = matches[1]
    if (guildID !== interaction.guild_id) return interaction.respond(4, { content: "The message must be in the same guild." })
    var channelID = matches[2]
    if (!await (await guilds.get(interaction.guild_id)).channels.get(channelID)) return interaction.respond(4, { content: "The channel is nonexistent" })
    var msgID = matches[3]
    var emoji = getEmoji(options.options.emoji)
    var guildData = await database.get(interaction.guild_id) || {}
    guildData.reactRoles = guildData.reactRoles || []
    guildData.reactRoles = guildData.reactRoles.filter(a => a.msgID !== options.options.message && a.id !== emoji.id && a.name !== emoji.name)
    guildData.reactRoles.push({
      msgID,
      role: options.options.role.id,
      ...emoji
    })
    database.set(interaction.guild_id, guildData)
    interaction.respond(4, { content: "Done!" })
    try {
      await api.sendRequest({
        endpoint: `/channels/${channelID}/messages/${msgID}/reactions/${emoji.id ? `${emoji.name}%3A${emoji.id}` : encodeURIComponent(emoji.name)}/@me`,
        method: "PUT"
      })
    } catch { interaction.createFollowup({content: "The emoji is not available for me"}) }
  } else if (options.subCmdInvoked == "remove") {
    if (!messageURLTestRegex.test(options.options.message)) return interaction.respond(4, { content: "Message URL is not valid" })
    if (!emojiRegex.test(options.options.emoji) && !unicodeEmojiRegex.test(options.options.emoji)) return interaction.respond(4, { content: "This is not a valid emoji" })
    var matches = messageURLRegex.exec(options.options.message)
    var guildID = matches[1]
    if (guildID !== interaction.guild_id) return interaction.respond(4, { content: "The message must be in the same guild." })
    var channelID = matches[2]
    if (!await (await guilds.get(interaction.guild_id)).channels.get(channelID)) return interaction.respond(4, { content: "The channel is nonexistent" })
    var msgID = matches[3]
    var guildData = await database.get(interaction.guild_id) || {}
    guildData.reactRoles = guildData.reactRoles || []
    var emoji = getEmoji(options.options.emoji)
    guildData.reactRoles = guildData.reactRoles.filter(a => a.msgID !== options.options.message && a.id !== emoji.id && a.name !== emoji.name)
    database.set(interaction.guild_id, guildData)
    interaction.respond(4, { content: "Done!" })
    try {
      console.log("requesting")
      await api.sendRequest({
        endpoint: `/channels/${channelID}/messages/${msgID}/reactions/${emoji.id ? `${emoji.name}%3A${emoji.id}` : encodeURIComponent(emoji.name)}/@me`,
        method: "DELETE"
      })
    } catch {}
  }
}
function getEmoji(str) {
  if (!emojiRegex.test(str)) { // It is prob a unicode character
    return {name: str, id: null}
  }
  var results = emojiRegex.exec(str)
  return {name: results[1], id: results[2]}
}