const enmap = require('enmap');
const addReactions = (message, reactions) => {
  message.react(reactions[0])
  reactions.shift()
  if (reactions.length > 0) {
    setTimeout(() => addReactions(message, reactions), 750)
  }
}

module.exports = async (client, id, text, reactions = [], ticketsysSettings = new enmap({}) ) => {
  const channel = await client.channels.fetch(id)

  channel.messages.fetch().then((messages) => {
    if (messages.size === 0) {
      // Send a new message
      channel.send(text).then((message) => {
        if (ticketsysSettings != null) {
          ticketsysSettings.set(`${message.guild.id}-ticket`, message.id);
        }
        addReactions(message, reactions)
      })
    } else {
      // Edit the existing message
      // i want to edit specific message getting it from its id
      let firstmessage = null
      for (const message of messages) {
        message[1].edit(text)
        if (ticketsysSettings != null) {
          firstmessage = message[1]
        }
        addReactions(message[1], reactions)
      }
      if (ticketsysSettings != null) {
        if (firstmessage) {
          ticketsysSettings.set(`${firstmessage.guild.id}-ticket`, firstmessage.id);
        }
      }
      
    }
  })
}