require('dotenv').config()

const Discord = require("discord.js")

const ytdl = require("ytdl-core")
const token = 'ODI2NTI5Mjg5NDA3MTY4NTcy.YGNzYg.xDLlKIovLBX6tE-wPeSMoEHI_94'
const client = new Discord.Client
const prefix = '.'
var userTickets = new Map();

client.on('ready', () => {
    console.log(`EventHub1 Logged In!`)
    client.user.setActivity('Events', {type: 'PLAYING'}).catch(console.error);
})

client.on('message', message => {
    if (message.channel.id === '826477250975236097') {
        message.react('👍')
        message.react('👎')
    }
})

client.on('message', async message => {
    if(message.author.bot) return
    if(!message.content.startsWith(prefix)) return

    const args = message.content.substring(prefix.length).split(" ")

    if(message.content.startsWith(`.play`)) {
        const voiceChannel = message.member.voice.channel
        if(!voiceChannel) return message.channel.send("You need to be in a voice channel to play music!")

        try {
            var connection = await voiceChannel.join()
        } catch (error) {
            console.log("Error Occured")
        }

        const dispatcher = connection.play(ytdl(args[1]))
        .on('finish', () => {
            voiceChannel.leave()
        })
        .on('error', error => {
            console.log("Error Occured")
        })
        dispatcher.setVolumeLogarithmic(5 / 5)
    } else if (message.content.startsWith(`.stop`)) {
        message.member.voice.channel.leave()
    }
})

client.login(token)