const Discord = require('discord.js');
const rblxbot = require('noblox.js')
const fs = require('fs');
var config = require('./config.json')
const keepAlive = require("./server");

const bot = new Discord.Client();

bot.once('ready', async() => {
    console.log('Bot is online!');
    bot.user.setActivity("the Sandy Hotels community", {type : "WATCHING"})
    await rblxbot.setCookie(process.env.Cookie);
})

async function rank(message, cmd, args) {
    const robloxName = args[0]
    console.log(robloxName)
    const robloxID = await rblxbot.getIdFromUsername(robloxName)
    .then(async (robloxID) => {
        const rank = parseInt(args[1])
        console.log(rank)
        console.log(config.GroupID)  
       await rblxbot.setRank({ group: config.GroupID, target: robloxID, rank: rank})
      .then(async () => {
             message.reply('succesfully ranked **' + robloxName + '** to rank **' + rank + '**')
         })
       .catch(async (err) => {
         const rankNumber = await rblxbot.getRankInGroup(config.GroupID, robloxID)
         const rankName = await rblxbot.getRankNameInGroup(config.GroupID, robloxID)
          message.reply('user is currently ranked **' + rankName + '[' + rankNumber + ']**, this user cannot be ranked to rank **' + rank + '**')
           console.log(err)
        })
      })
    .catch((err) => {
        message.reply('could not find user. User may not be in the group.')
        console.log(err)
    })
}

function pin(message) {
    message.pin()
}

bot.on('message', async(message) => {
    if(message.type == 'PINS_ADD') {
        if(message.channel.id == '947267799435313204') {
            message.delete()
        }
    }
    if(message.webhookID) {
        if(message.channel.id == '939989998596403230') {
           if(message.content == "App Ticket:"){
             pin(message)
           }
        }
    }
    if(message.author.bot) return;
    if(message.channel.type !== 'text') return;
    let prefix = '!';
    let MessageArray = message.content.split(' ')
    let cmd = MessageArray[0].slice(prefix.length)
    let args = MessageArray.slice(1)

    if(!message.content.startsWith(prefix)) return;

    if(cmd == "rank"){
        //Founder: 635171900175417374, Administrator: 635171900552642560, President: 702993503352782898, Executive Officer: 702993504200032326, Operations Director: 932436276328677376, SHR: 932436308171833354, +: 904163609637183539
        if(message.member.roles.cache.has('947267626692915311') ){
            rank(message, cmd, args)
        }
        else message.reply('You do not have permission to use this command.')
    }
})

keepAlive();
bot.login(process.env.Token)