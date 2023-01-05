const mySecret = process.env['TOKEN']
const { Client, MessageEmbed } = require('discord.js');
const config = require('./config');
const commands = require('./help');
const botCommands = require('./commands') 
const bot = {
    client: new discord.Client(),
    log: console.log, // eslint-disable-line no-console
    commands: new discord.Collection(),   // <-- this is new
}
let bot = new Client({
  fetchAllMembers: true, // Remove this if the bot is in large guilds.
  presence: {
    status: 'online',
    activity: {
      name: 