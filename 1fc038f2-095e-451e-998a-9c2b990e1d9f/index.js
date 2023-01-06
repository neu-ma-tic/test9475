const Discord = require("discord.js");
const Keyv = require('keyv')
const db = require('./db.js')

const token = 'ODQxOTE0MTM3NzkyNjEwMzM0.YJtrpA.EfimwHw-jezIi7drjpCaVmDQN8Q'
const bot = new Discord.Client()

const keyv = new Keyv('sqlite://fries-db.sqlite')
keyv.on('error', err => console.log(err))

const statEmbed = async (username, rank) => {
  let embed = new Discord.MessageEmbed()
  embed.setTitle(`Ranking for ${username}`)
  embed.setDescription(`Score is ${rank}`)
  return embed
}
const prefix = '!'
bot.on('message', async (msg) => {
  if(msg.content[0] !== prefix) {
    console.log('no prefix')
    return
  }

  const args = msg.content.slice(prefix.length).trim().split(' ')
  const command = args.shift().toLowerCase()

  if(command === 'stats') {
    const user = msg.author

    let rank = await keyv.get(user.username)
    if(rank === undefined) {
      await keyv.set(user.username, 1)
      rank = await keyv.get(user.username)
    }
    console.log('rank: ', rank)
    let embed = await statEmbed(user.username, rank)
    msg.channel.send(embed)
  }

  if(command === 'promote') {
    if(!msg.member.roles.cache.has('602665687051403274')) {
      console.log('user is not moderator')
      return
    }

    const user = msg.mentions.users.first()
    if(!user) {
      console.log('no user mentioned')
      return
    }

    let rankVal = await keyv.get(user.username)
    if(rankVal === undefined) {
      await keyv.set(user.username, 1)
      rankVal = await keyv.get(user.username)
    }

    let num = 1
    if(args.length > 1) {
      num = parseInt(args[0])
    }
    const newRank = rankVal + num
    await keyv.set(user.username, newRank)

    const checker = await keyv.get(user.username)

    if(checker >= 10) {
      let modeRole = msg.guild.roles.cache.find(r => r.name === 'moderator')
      let member = msg.mentions.members.first()
      member.roles.add(modeRole)
    }
  }

  if(command === 'demote') {
    if(!msg.member.roles.cache.has('602665687051403274')) {
      console.log('user is not moderator')
      return
    }

    const user = msg.mentions.users.first()
    if(!user) {
      console.log('no user mentioned')
      return
    }

    let rankVal = await keyv.get(user.username)
    if(rankVal === undefined) {
      await keyv.set(user.username, 1)
      rankVal = await keyv.get(user.username)
    }

    let num = 1
    if(args.length > 1) {
      num = parseInt(args[0])
    }

    const newRank = rankVal - num
    await keyv.set(user.username, newRank)

    const checker = await keyv.get(user.username)

    if(checker < 10) {
      let modRole = msg.guild.roles.cache.find(r => r.name === "moderator")
      let member = msg.mentions.members.first()
      member.roles.remove(modRole)
    }
  }

  if(command === 'highscore') {
    let rows = await db.select()

    //console.log(rows)
    let sortedData = []

    sortedData = rows.sort((a,b) => {
      let newa = JSON.parse(a.value)
      let newb = JSON.parse(b.value)
      a.value = newa
      b.value = newb

      let val = b['value']['value'] - a['value']['value']
      return val
    })

    console.log(sortedData)

    if(sortedData.length > 5) {
      sortedData = sortedData.slice(0,5)
    }

    let embed = new Discord.MessageEmbed()
    embed.setTitle('Highest ranked users')
    embed.setDescription(`Top ${sortedData.length} users`)

    sortedData.map(user => {
      let username = user['key'].slice(5)
      let score = user['value']['value']
      embed.addField(`${username} : `, score)
    })
    embed.setFooter(`this embed made by ${bot.user.username}`)
    msg.channel.send(embed)

  }

})
bot.login(ODQxOTE0MTM3NzkyNjEwMzM0.YJtrpA.EfimwHw-jezIi7drjpCaVmDQN8Q)
