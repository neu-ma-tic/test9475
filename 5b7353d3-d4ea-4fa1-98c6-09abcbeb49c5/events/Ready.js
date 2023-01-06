const Discord = require("discord.js");
const config = require("../../config.json");

module.exports = async function (client) {
client.on("ready", () => {
    let activities = [
        `${client.guilds.cache.size} servidores!`,
        `${client.users.cache.size} usuários!`,
        'Use !help para ver meus comandos', 
        'Estou sendo Desenvolvido'    
      ],
      i = 0;
    setInterval( () => client.user.setActivity(`${activities[i++ % activities.length]}`), 1000 * 10); 
    client.user
        .setStatus("dnd")
        .catch(console.error);
  console.log(`[API]${client.user.username} está online`)
})};