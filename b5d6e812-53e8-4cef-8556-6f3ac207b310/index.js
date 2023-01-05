const Discord = require("discord.js");
require("discord-reply");
const client = new Discord.Client();
const config = require(__dirname+"/config.json");
const fetch = require("node-fetch");
const fetchJson = async (url, options) => new Promise(async (resolve, reject) => {
    fetch(url, options)
        .then(response => response.json())
        .then(json => {
            resolve(json)
        })
        .catch((err) => {
            resolve('err')
        })
});

async function startBot(){
  
  client.on("ready", () => {
    console.log(`${config.botname} ${config.version} is Already!`);
  });
  
  client.on("message", async(message) => {
    if(message.channel.id !== config.channelid) return
    const content = message.content
    if (message.author.bot) return;
    const req = await fetchJson(`http://uptime-glitch-zril.glitch.me/api/simi?text=${encodeURIComponent(content)}`, {method: 'get'});
    if(!req.status) return message.channel.send("Handler Error");
    message.lineReply(req.response);
  });
  
  client.login(config.token);
}
startBot()
