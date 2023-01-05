const Discord = require('discord.js')
const client = new Discord.Client()
const dash = require('./dash/dash.js')(client)

const chalk = require('chalk')

const package = require('./package.json')

client.on('ready', () => {
  console.log(chalk.red(`
  ==========================================================================================
                        ██ ▄█▀ ▒█████   ██▓ ▄████▄   ██░ ██  ██▓
                        ██▄█▒ ▒██▒  ██▒▓██▒▒██▀ ▀█  ▓██░ ██▒▓██▒
                        ▓███▄░ ▒██░  ██▒▒██▒▒▓█    ▄ ▒██▀▀██░▒██▒
                        ▓██ █▄ ▒██   ██░░██░▒▓▓▄ ▄██▒░▓█ ░██ ░██░
                        ▒██▒ █▄░ ████▓▒░░██░▒ ▓███▀ ░░▓█▒░██▓░██░
                        ▒ ▒▒ ▓▒░ ▒░▒░▒░ ░▓  ░ ░▒ ▒  ░ ▒ ░░▒░▒░▓  
  ==========================================================================================
  
  [ # ] = { . . . } => Loading stats...
  [ # ] = { . . . } => Loading data...
  [ ### ] = { . . . } => Making a "Nashe" Tea...
  [ $$$ ] = { = = = } => Bot loaded.
  [ $ ] = Stats = {
    "users": ${client.users.cache.size},
    "guilds": ${client.guilds.cache.size},
    "channels": ${client.channels.cache.size}
  }
  `))
})

client.login(process.env.token)
  .then(() => {
    console.log(`{ $ $ $ } => ${client.user.username} has been logged successfully!`)
  })