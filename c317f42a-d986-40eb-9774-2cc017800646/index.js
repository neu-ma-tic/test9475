const client = require('discord.js')

client.on('ready', () => {
  console.log('Bot Ready!')
})

this.client.token(process.env['TOKEN'])
client.login(process.env['TOKEN'])