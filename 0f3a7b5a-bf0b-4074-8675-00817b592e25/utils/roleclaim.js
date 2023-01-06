const firstmessage = require('./firstmessage')

module.exports = (client) => {
  const channelId = config.ROLE_CLAIM.channel_ID

  // const getEmoji = (emojiName) => client.emojis.cache.find((emoji) => emoji.name === emojiName)

  const emojisArray = {
    '🇸🇮': 'Slovenia',
    '🇭🇷': 'Croatia',
    '🇧🇦': 'Bosnia',
    '🇷🇸': 'Serbia',
    '🇲🇪': 'Montenegro',
    '🇦🇱': 'Albania',
    '🇲🇰': 'Macedonia',
    '🇬🇷': 'Greece',
    '🇧🇬': 'Bulgaria',
    '🇷🇴': 'Romania',
  }
  

  // :flag_si: :flag_hr: :flag_ba: :flag_rs: :flag_me: :flag_al: :flag_mk: :flag_gr: :flag_bg: :flag_ro: 

  const reactions = []

  let emojiText = 'Please react with the corresponding nationality to unlock your country\'s main chat! (You can change this anythime.)\n@everyone\n\n'
  for (const key in emojisArray) {
    const emoji = key
    reactions.push(emoji)

    const role = emojisArray[key]
    emojiText += `${emoji} = ${role}\n`
  }

  firstmessage(client, channelId, emojiText, reactions, null)

  const handleReaction = (reaction, user, add) => {
    if (user.id === config.BOT_SERVER_ID) {
      return
    }

    const emoji = reaction._emoji.name

    const { guild } = reaction.message

    const roleName = emojisArray[emoji]
    if (!roleName) {
      return
    }

    const role = guild.roles.cache.find((role) => role.name === roleName)
    const member = guild.members.cache.find((member) => member.id === user.id)

    if (add) {
      member.roles.add(role)
    } else {
      member.roles.remove(role)
    }
  }

  client.on('messageReactionAdd', (reaction, user) => {
    if (reaction.message.channel.id === channelId) {
      handleReaction(reaction, user, true)
    }
  })

  client.on('messageReactionRemove', (reaction, user) => {
    if (reaction.message.channel.id === channelId) {
      handleReaction(reaction, user, false)
    }

  })




}