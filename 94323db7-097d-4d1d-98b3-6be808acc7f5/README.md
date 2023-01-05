const WebSocket = require('ws')
const uuid = require('uuid')
const Discord = require('discord.js');
const client = new Discord.Client();

console.log('Ready. On MineCraft chat, type /connect [ip address]:3000')
const wss = new WebSocket.Server({ port: 3000 })

var globalSocket

wss.on('connection', socket => {
  console.log('Connected')
  globalSocket = socket

  socket.send(JSON.stringify({
    "header": {
      "version": 1,
      "requestId": uuid.v4(),
      "messageType": "commandRequest",
      "messagePurpose": "subscribe"
    },
    "body": {
      "eventName": "PlayerMessage"
    },
  }))

  socket.on('message', packet => {
    const msg = JSON.parse(packet)

    try{
      if(msg.body.properties.Sender != 'External'){
        client.channels.cache.get("824801768343863368").send(msg.body.properties.Sender + ': ' + msg.body.properties.Message)
      }
    }
    catch{}
  })
})

function send(cmd) {
  cmd = 'say ' + cmd

  const msg = JSON.stringify({
    "header": {
      "version": 1,
      "requestId": uuid.v4(),
      "messagePurpose": "commandRequest",
      "messageType": "commandRequest"
    },
    "body": {
      "version": 1,
      "commandLine": cmd,
      "origin": {
        "type": "player"
      }
    }
  })
  globalSocket.send(msg)
}

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
  if(msg.author.bot)
    return

  send(msg.member.displayName + ': ' + msg.content);
});

client.login('ODU3MzgzOTAxODIyMTg5NTg5.YNOy-w.cqMmfAL_batoz7bsQC-OFsJKrmo')