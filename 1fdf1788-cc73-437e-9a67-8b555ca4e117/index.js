const commando = require('discord.js-commando')
const path = require('path')
const client = new commando.CommandoClient({
  owner: '800050912776290375',
  commandPrefix: '!'
})

const config = require('./config.json')
const keepAlive = require('./heroku.js')

client.on('ready', () => {
  console.log('The client is ready')

  client.registry.registerGroups([
    ['misc', 'misc commands'],
    ['moderation', 'moderation commands'],
  ]).registerDefaults().registerCommandsIn(path.join(__dirname, 'cmds'))
})

keepAlive();
client.login(config.token)