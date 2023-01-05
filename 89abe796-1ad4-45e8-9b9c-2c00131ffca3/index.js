const express = require('express')
const app = express();
const port = 3000

app.get('/', (req, res) => res.send('Ready to use'))

app.listen(port, () =>
console.log(`Your app is listening a http://localhost:${port}`)
);

const { Client, Collection } = require('discord.js');
const { TOKEN, PREFIX } = require('./config.json');
const fs = require('fs')
const ms = require("ms")
const fetch = require('node-fetch')
const client = new Client({ // ohh just to show people you guys fixing erirs hmm
  intents: 32767
});


client.commands = new Collection();
client.aliases = new Collection();
client.categories = fs.readdirSync("./Commands");
client.events = new Collection();

module.exports = client;

["Command", "Event"].forEach(handler => {
  require(`./Structures/${handler}`)(client);
});

client.on('ready', () => {
  client.user.setActivity(`${PREFIX}help`, { type: 'PLAYING' })
  console.log(`Registering Commands!`)
  console.log(`Registering Events!`)
  console.log(`Setting up bot status!`)
  console.log(`${client.user.tag} is online`)
})


process.on('unhandledRejection', async (error) => {
  // error checking
  const err = error.stack.split("\n");
  await client.channels.cache.get('932708446170644580').send({
    embeds: [new Discord.MessageEmbed().setTitle(`unhandledRejection`).setDescription(`\`\`\`diff\n- ${err[0]}\n+ ${err[1]}\n\`\`\``).setTimestamp().setColor("GREY")]
  });
});

process.on('uncaughtException', async (error) => {
  const err = error.stack.split("\n");
  await client.channels.cache.get('932708446170644580').send({
    embeds: [new Discord.MessageEmbed().setTitle(`uncaughtException`).setDescription(`\`\`\`diff\n- ${err[0]}\n+ ${err[1]}\n\`\`\``).setTimestamp().setColor("GREY")]
  });
});

process.on("warning", async (info) => {
  await client.channels.cache.get('932708446170644580').send({
    embeds: [new Discord.MessageEmbed().setTitle(`warning`).setDescription(`\`\`\`diff\n+ ${info}\n\`\`\``).setTimestamp().setColor("GREY")]
  });
});

process.on('beforeExit', async () => {
  console.log(figlet(chalk.redBright('Shutting down...')));
  await client.destroy();
});

process.on('exit', async () => {
  console.log(figlet(chalk.redBright('Shut down.')));
});

client.login(process.env.TOKEN)