//✅》Host do Bot
const express = require('express');
const app = express();
app.get("/", (request, response) => {
  const ping = new Date();
  ping.setHours(ping.getHours() - 3);
  console.log(`Ping recebido às ${ping.getUTCHours()}:${ping.getUTCMinutes()}:${ping.getUTCSeconds()}`);
  response.sendStatus(200);
});
//✅》Variáves de Packages
app.listen(process.env.PORT); // Recebe solicitações que o deixa online
const Discord = require("discord.js"); //Conexão com a livraria Discord.js
const client = new Discord.Client(); //Criação de um novo Client
//✅》Variáves de Arquivos
const config = require("./config.json"); //Pegando o prefixo do bot para respostas de comandos
client.on('message', message => {
     if (message.author.bot) return;
     if (message.channel.type == 'dm') return;
     if (!message.content.toLowerCase().startsWith(config.prefix.toLowerCase())) return;
     if (message.content.startsWith(`<@!${client.user.id}>`) || message.content.startsWith(`<@${client.user.id}>`)) return;

    const args = message.content
        .trim().slice(config.prefix.length)
        .split(/ +/g);
    const command = args.shift().toLowerCase();

    try {
        const commandFile = require(`./commands/${command}.js`)
        commandFile.run(client, message, args);
    } catch (err) {
    console.error('Erro:' + err);
  }
});

//✅》Client
//✅》Rich Presence
//STREAMING
client.on("ready", () => {
  let activities = [
      `Utilize ${config.prefix}help  `,
      `${client.guilds.cache.size} servidores!  `,
      `${client.channels.cache.size} canais! : `,
      `paz no discord : `,
      `${client.users.cache.size} usuários!  `
    ],
    i = 0;
  setInterval( () => client.user.setActivity(`${activities[i++ % activities.length]}`, {
        //type: "WATCHING",
        type: "STREAMING", url: "https://twitch.tv/o_c0de"
      }), 1200 * 60); 
  client.user
      .setStatus("online")
      .catch(console.error);
console.log("[ Minhas atividades estão Online! ]")
});
//WATCHING
client.on("ready", () => {
  let activities = [
      `Utilize ${config.prefix}ajuda para obter ajuda  `,
      `${client.guilds.cache.size} servidores!  `,
      `olhando pessoas usarem o_c0de na loja do fortnite  `,
      `${client.channels.cache.size} canais!`,
      `os outros bots  `,
      `${client.users.cache.size} usuários!  `
    ],
    i = 0;
  setInterval( () => client.user.setActivity(`${activities[i++ % activities.length]}`, {
        type: "WATCHING",
      }), 100 * 60); 
  client.user
      .setStatus("online")
      .catch(console.error);
console.log("Estou Online!")
});

//✅》Console Físico
//Iniciando....
client.on("ready", () => {
  var content = "Iniciando o bot...  ";
  var channel = client.guilds.cache
    .get("741810958057472000")//Guilda
    .channels.cache.get("798285765221154816");//Canal
  channel.send(content);
  console.log("[ Iniciando.... ]");
})


client.login(`Nzk4NjQ4NzYzMzkyMzI3Njkw.X_4Fnw.Jd-qTy9L1q1006D7sDPZnVFNjMM`);