const discord = require('discord.js');
const fs = require('fs');
const { prefix, token } = require('./config.json');

const client = new discord.Client();
client.commands = new discord.Collection();

const commandFiles = readdirSync('./commands').filter(file => file.endsWith('.js'));

for (const file of commandFiles) {
  const command = require(`./commands./${file}`);
  client.commands.set(command.name, command);
}

client.once('ready', () => {
  console.log('Ready!');
  client.user.setPresence({
    game: {
        name:"Hacking the Government",
        type: 'WATCHING'
      },
    status: 'dnd'
  })
);

client.on('message', message => {
  if (!message.content.startsWith(prefix)) return;
  
}
