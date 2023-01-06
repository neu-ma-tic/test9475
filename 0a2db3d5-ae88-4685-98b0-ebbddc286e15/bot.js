let ws
function connect(){
const WebSocket = require('ws');
     ws =  new WebSocket('wss://613.itzjak.ml')
ws.on('open', function open() { 
  ws.send(JSON.stringify({"method": "handshake", "project_id": "437333010"}));
});
console.log("Connected")
}
connect()
let Discord;
let Database;
if (typeof window !== "undefined") {
    Discord = DiscordJS;
    Database = EasyDatabase;
} else {
    Discord = require("discord.js");
    Database = require("easy-json-database");
}
const delay = (ms) => new Promise((resolve) => setTimeout(() => resolve(), ms));
const s4d = {
    Discord,
    client: null,
    tokenInvalid: false,
    reply: null,
    joiningMember: null,
    database: new Database("./db.json"),
    checkMessageExists() {
        if (!s4d.client) throw new Error('You cannot perform message operations without a Discord.js client')
        if (!s4d.client.readyTimestamp) throw new Error('You cannot perform message operations while the bot is not connected to the Discord API')
    }
};
s4d.client = new s4d.Discord.Client();
s4d.client.on('raw', async (packet) => {
    if (['MESSAGE_REACTION_ADD', 'MESSAGE_REACTION_REMOVE'].includes(packet.t)) {
        const guild = s4d.client.guilds.cache.get(packet.d.guild_id);
        if (!guild) return;
        const member = guild.members.cache.get(packet.d.user_id) || guild.members.fetch(d.user_id).catch(() => {});
        if (!member) return;
        const channel = s4d.client.channels.cache.get(packet.d.channel_id);
        if (!channel) return;
        const message = channel.messages.cache.get(packet.d.message_id) || await channel.messages.fetch(packet.d.message_id).catch(() => {});
        if (!message) return;
        s4d.client.emit(packet.t, guild, channel, message, member, packet.d.emoji.name);
    }
});
s4d.client.login(process.env.TOKEN).catch((e) => s4d.tokenInvalid = true);

s4d.client.on('message', async (s4dmessage) => {
    
    if ((s4dmessage.content) == '!ping') {
        s4dmessage.channel.send(String('pong!'));
         ws.send(JSON.stringify({ "method": "set", "name": "☁ number", "value": "pong" }));
    

    }

});

s4d.client.on('ready', async () => {
    ws.on('message', function incoming(data) {
        var dat = JSON.parse(data)
     s4d.client.channels.cache.find((channel) => channel.name === 'general').send(String(dat.value));
  console.log(dat.value);
    
});
  ws.onclose = function(e) {
    console.log('Socket is closed. Reconnect will be attempted in 1 second.', e.reason);
    setTimeout(function() {
      connect();
    }, 4000);
  };
});

s4d;