const {Client, RichEmbed } = require('discord.js')

const bot = new Client()

const ping = require('minecraft-server-util')

const token = 'YOUR TOKEN'
'
const PREFIX = '!'

bot.on('ready', () =>{
    console.log('Bot has come online.')
})

bot.on('message', message =>{

    let args = message.content.substring(PREFIX.length).split(' ')

    switch(args[0]){

        case 'mc':

            if(!args[1]) return message.channel.send('HaythemSmp.aternos.me')
            
                        if(!args[2]) return message.channel.send('You must type a minecraft server port')
