require('dotenv').config();

const { Client, Collection, Discord, MessageEmbed } = require('discord.js');

const coins = require('./coins.json')
const fs = require('fs');

//--------uptimer--------------------------

const { keep_alive } = require("./keep_alive");

//----------------------------------------




const xpfile = require('./xp.json')

const { BOT_TOKEN, PREFIX } = process.env;

const client = new Client({partials: ["MESSAGE", "USER", "REACTION"]})





const cooldown = new Set()
const cooldown2 = new Set()
const cooldownCrime = new Set()

const one = '🧠';
const two = '👒';
const three = '📌';
const four = '🦾';
const five = '💍';
const six = '📀';
const seven = '🐟';
const eight = '💄';
const nine = '🎶';
const ten = '🔰';
const eleven = '🎂';
const twelve = '💸';
const thirteen = '👑';


const rock = '✊🏽';
const paper = '✋🏽';
const scissors = '✌🏽';


const heads = '🌲';
const tails = '1️⃣';

client.commands = new Collection();
client.aliases = new Collection();
const db = require("quick.db")
client.prefix = PREFIX;

client.categories = fs.readdirSync('./commands/');



['command', 'event'].forEach((handler) => {
    require(`./handlers/${handler}`)(client);
});

client.on('ready', () => console.log(`${client.user.tag} is ready!`))


client.on('guildMemberAdd', member => {
  const welcomeChannel = member.guild.channels.cache.find(ch => ch.name.includes('welcome'));
  

  if(!welcomeChannel) {
    console.log('Could not find welcome channel, so I am making one');
    member.guild.createChannel('welcome', {
      type: 'text',
      position: 0,
      topic: 'Welcome channel fot new users.',
      permissionOverwrites: [{
        id: member.guild.id,
        allow: ['READ_MESSAGE_HISTORY', 'READ_MESSAGES', 'VIEW_CHANNEL'],
        deny: ['SEND_MESSAGES']
      }]
    }).then(consol.log('Welcome channel created')).catch(console.error)
  }

  let welcomeEmbed = new MessageEmbed()
  .setDescription(`<@${member.user.id}> welcome to our server!`)
  welcomeChannel.send(welcomeEmbed)
})


client.on('message', async message => {
  if(message.author.id === client.user.id) return;
  if(message.content.startsWith(`${PREFIX}`)) return;
  
  if(!coins[message.author.id])
  {
    coins[message.author.id] = {
      coins: 0
    }
  }
  coins[message.author.id] = {
    coins: coins[message.author.id].coins + 1
  }

  fs.writeFile('./coins.json', JSON.stringify(coins), (err) => {
    if(err) console.log(err)
  })
  
})

client.on('message', async message => {
  const args = message.content.slice(PREFIX.length).trim().split(' ');
  if(message.content.startsWith(`${PREFIX}coins`)){
    if(message.channel.id !== "934904933919117312") return message.reply("You can't do this here \n <#934904933919117312>")
    let member = message.mentions.users.first() || message.guild.members.cache.get(args[1]) || message.author;
    if(!coins[member.id]){
      coins[member.id] = {
        coins: 0
      }
    }
    let MemberCoins = coins[member.id].coins
      let coinsEmbed = new MessageEmbed()
      .setTitle(`__${member.username}'s Coins:__`)
      .setThumbnail(member.displayAvatarURL({ dynamic: true }))
      .setDescription(`${member.username} has \`${MemberCoins}\` coins !`)
      .setFooter(client.user.tag, client.user.displayAvatarURL({ dynamic: true }))
      message.channel.send(coinsEmbed)
    
  }
  if(message.content.startsWith(`${PREFIX}shop`)){
    if(!message.member.permissions.has("ADMINISTRATOR")) return message.reply("You don't have permissions")



    client.guilds.cache.get("934872609844256778").roles.cache.find(role => role.name === "🧠")
    client.guilds.cache.get("934872609844256778").roles.cache.find(role => role.name === "👒")
    client.guilds.cache.get("934872609844256778").roles.cache.find(role => role.name === "📌")
    client.guilds.cache.get("934872609844256778").roles.cache.find(role => role.name === "🦾")
    client.guilds.cache.get("934872609844256778").roles.cache.find(role => role.name === "💍")
    client.guilds.cache.get("934872609844256778").roles.cache.find(role => role.name === "📀")
    client.guilds.cache.get("934872609844256778").roles.cache.find(role => role.name === "🐟")
    client.guilds.cache.get("934872609844256778").roles.cache.find(role => role.name === "💄")
    client.guilds.cache.get("934872609844256778").roles.cache.find(role => role.name === "🎶")
    client.guilds.cache.get("934872609844256778").roles.cache.find(role => role.name === "🔰")
    client.guilds.cache.get("934872609844256778").roles.cache.find(role => role.name === "🎂")
    client.guilds.cache.get("934872609844256778").roles.cache.find(role => role.name === "💸")
    client.guilds.cache.get("934872609844256778").roles.cache.find(role => role.name === "👑")



    let shopEmbed = new MessageEmbed()
    .setTitle(`${message.guild.name} - Coins Shop`)
    .setDescription(`<@&935150565091069952> - 0$ \n \n <@&935156458272751687> - 500$ \n \n <@&935184911579623444> - 1000$ \n \n <@&935184653789323344> - 1500$ \n \n <@&935186015533019156>  - 2000$\n \n <@&935189955360227398> - 2500$ \n \n <@&935284115228459008> - 3000$ \n \n <@&935189514400432189> - 3500$ \n \n <@&935190860436492319> - 4000$ \n \n <@&935283257799483442> - 4500$ \n \n <@&935283135736840252> - 5000$ \n \n <@&935283062873411615> - 5500$ \n \n <@&935284281037705277> - 6000$`)
    .setFooter(client.user.tag, client.user.displayAvatarURL({ dynamic: true }))
    let messageEmbed = await message.channel.send(shopEmbed);

    // react emojies
    messageEmbed.react(one);
    messageEmbed.react(two);
    messageEmbed.react(three);
    messageEmbed.react(four);
    messageEmbed.react(five);
    messageEmbed.react(six);
    messageEmbed.react(seven);
    messageEmbed.react(eight);
    messageEmbed.react(nine);
    messageEmbed.react(ten);
    messageEmbed.react(eleven);
    messageEmbed.react(twelve);
    messageEmbed.react(thirteen);
    //end of react emojies

    client.on('messageReactionAdd', async (reaction, user) => {
      if (reaction.message.partial) await reaction.message.fetch();
      if (reaction.partial) await reaction.fetch();
      if (user.bot) return;
      if (!reaction.message.guild) return;
 
      if (reaction.message.channel.id == '934904514669072425') {
              //give a role when reacting the emoji
        if (reaction.emoji.name === one) {
          let UserCoins = coins[user.id].coins
          
          if(UserCoins >= 0) {
            await reaction.message.guild.members.cache.get(user.id).roles.add('935150565091069952');
          }
        }
        if(reaction.emoji.name === two) {
          let UserCoins = coins[user.id].coins
          if(UserCoins >= 500) {
            await reaction.message.guild.members.cache.get(user.id).roles.add('935156458272751687')
            coins[user.id] = {
              coins: UserCoins - 500
            }
          }
          
        }
        if(reaction.emoji.name === three) {
          let UserCoins = coins[user.id].coins
          if(UserCoins >= 1000) {
            await reaction.message.guild.members.cache.get(user.id).roles.add('935184911579623444')
            coins[user.id] = {
              coins: UserCoins - 1000
            }
          }
        }
        if(reaction.emoji.name === four) {
          let UserCoins = coins[user.id].coins
          if(UserCoins >= 1500) {
            await reaction.message.guild.members.cache.get(user.id).roles.add('935184653789323344')
            coins[user.id] = {
              coins: UserCoins - 1500
            }
          }
        }
        if(reaction.emoji.name === five) {
          let UserCoins = coins[user.id].coins
          if(UserCoins >= 2000) {
            await reaction.message.guild.members.cache.get(user.id).roles.add('935186015533019156')
            coins[user.id] = {
              coins: UserCoins - 2000
            }
          }
        }
        if(reaction.emoji.name === six) {
          let UserCoins = coins[user.id].coins
          if(UserCoins >= 2500) {
            await reaction.message.guild.members.cache.get(user.id).roles.add('935189955360227398')
            coins[user.id] = {
              coins: UserCoins - 2500
            }
          }
        }
        if(reaction.emoji.name === seven) {
          let UserCoins = coins[user.id].coins
          if(UserCoins >= 3000) {
            await reaction.message.guild.members.cache.get(user.id).roles.add('935284115228459008')
            coins[user.id] = {
              coins: UserCoins - 3000
            }
          }
        }
        if(reaction.emoji.name === eight) {
          let UserCoins = coins[user.id].coins
          if(UserCoins >= 3500) {
            await reaction.message.guild.members.cache.get(user.id).roles.add('935189514400432189')
            coins[user.id] = {
              coins: UserCoins - 3500
            }
          }
        }
        if(reaction.emoji.name === nine) {
          let UserCoins = coins[user.id].coins
          if(UserCoins >= 4000) {
            await reaction.message.guild.members.cache.get(user.id).roles.add('935190860436492319')
            coins[user.id] = {
              coins: UserCoins - 4000
            }
          }
        }
        if(reaction.emoji.name === ten) {
          let UserCoins = coins[user.id].coins
          if(UserCoins >= 4500) {
            await reaction.message.guild.members.cache.get(user.id).roles.add01('935283257799483442')
            coins[user.id] = {
              coins: UserCoins - 4500
            }
          }
        }
        if(reaction.emoji.name === eleven) {
          let UserCoins = coins[user.id].coins
          if(UserCoins >= 5000) {
            await reaction.message.guild.members.cache.get(user.id).roles.add('935283135736840252')
            coins[user.id] = {
              coins: UserCoins - 5000
            }
          }
        }
        if(reaction.emoji.name === twelve) {
          let UserCoins = coins[user.id].coins
          if(UserCoins >= 5500) {
            await reaction.message.guild.members.cache.get(user.id).roles.add('935283062873411615')
            coins[user.id] = {
              coins: UserCoins - 5500
            }
          }
        }
        if(reaction.emoji.name === thirteen) {
          let UserCoins = coins[user.id].coins
          if(UserCoins >= 6000) {
            await reaction.message.guild.members.cache.get(user.id).roles.add('935284281037705277')
            coins[user.id] = {
              coins: UserCoins - 6000
            }
            
          }
        }
        
//end of give a role when reacting the emoji
      }
      
      else {
          return;
        }
        fs.writeFile('./coins.json', JSON.stringify(coins), (err) => {
          if(err) console.log(err)
        })
    })

  }
//-----------------------------------------------------
  if(message.content.startsWith(`${PREFIX}add`)) {
    //add coins (for giveaways...)
    // !add @Gavish 150
    if(!message.member.permissions.has("ADMINISTRATOR")) return message.reply("You don't have permissions")
    let member = message.mentions.users.first() || message.guild.members.cache.get(args[1])
    if(!member) return message.reply('Please mention someone')
    if(member.id === client.user.id) return message.reply("You can't add me coins")
    if(!coins[member.id]){
      coins[member.id] = {
        coins: 0
      }
    }
    let MemberCoins = coins[member.id].coins
    if(!coins[message.author.id]) {
      coins[message.author.id] = {
        coins: 0
      }
    }
    
    let amount = parseInt(args[2])
    if(isNaN(amount) || !amount) return message.reply('Please enter a number of coins')
    if(amount < 1) return message.reply('Please enter a number above 1')
    coins[member.id] = {
      coins: MemberCoins + amount
    }
    message.channel.send(`added ${amount} to ${member}`)

    fs.writeFile('./coins.json', JSON.stringify(coins), (err) => {
      if(err) console.log(err)
    })
  }

//-------------------------------------
  if(message.content.startsWith(`${PREFIX}remove`)) {
    //remove coins
    // !remove @Gavish 150
    let member = message.mentions.users.first() || message.guild.members.cache.get(args[1])
    if(!message.member.permissions.has("ADMINISTRATOR")) return message.reply("You don't have permissions")
    if(!member) return message.reply('Please mention someone')
    if(member.id === client.user.id) return message.reply("You can't remove my coins")
    if(!coins[member.id]){
      coins[member.id] = {
        coins: 0
      }
    }
    let MemberCoins = coins[member.id].coins
    if(!coins[message.author.id]) {
      coins[message.author.id] = {
        coins: 0
      }
    }
    
    let amount = parseInt(args[2])
    if(isNaN(amount) || !amount) return message.reply('Please enter a number of coins')
    if(amount < 1) return message.reply('Please enter a number above 1 coin')
    coins[member.id] = {
      coins: MemberCoins - amount
    }
    message.channel.send(`removed ${amount} to ${member}`)

    fs.writeFile('./coins.json', JSON.stringify(coins), (err) => {
      if(err) console.log(err)
    })
  }

//-----------------------------------------------------
  



  if(message.content.startsWith(`${PREFIX}give`)){
    //give coins between 2 members
    //!give @Gavish 150
    let member = message.mentions.users.first() || message.guild.members.cache.get(args[1])
    if(message.channel.id !== "934904933919117312") return message.reply("You can't do this here \n <#934904933919117312>")
    if(!member) return message.reply('Please mention someone')
    if(member.id === client.user.id) return message.reply("You can't give me coins")
    if(!coins[member.id]){
      coins[member.id] = {
        coins: 0
      }
    }
    let MemberCoins = coins[member.id].coins
    let MyCoins = coins[message.author.id].coins

    if(!coins[member.id]){
      coins[member.id] = {
        coins: 0
      }
    }
    
    let amount = parseInt(args[2])
    if(isNaN(amount) || !amount) return message.reply("Please enter a number of coins")
    if(MyCoins < amount) return message.reply(`You don't have ${amount} coins`)
    if(amount < 1) return message.reply("You can't give below 1 coin")
    coins[message.author.id] = {
      coins: MyCoins - amount
    }
    coins[member.id] = {
      coins: MemberCoins + amount
    }
    message.channel.send(`${message.author} gave ${amount} to ${member}`)

    fs.writeFile('./coins.json', JSON.stringify(coins), (err) => {
      if(err) console.log(err)
    })
  }

//---------------------------------------------------------------------



  if(message.content.startsWith(`${PREFIX}bet`)){
    //bet
    //!bet 150
    if(!coins[message.author.id]){
      coins[message.author.id] = {
        coins: 0
      }
    }
    let MyCoins = coins[message.author.id].coins
    let amount = parseInt(args[1])
    if(message.channel.id !== "934904933919117312") return message.reply("You can't do this here \n <#934904933919117312>")
    if(isNaN(amount) || !amount) return message.reply("Please enter a number of coins")
    if(amount < 1) return message.reply("You can't give below 1 coin")
    if(MyCoins < amount) return message.reply(`You don't have ${amount} coins`)
    if(amount < 10) return message.reply("The minimum amount to bet is 10 coins")


    const YesOrNo = ['yes', 'yes', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no']
    let random = YesOrNo[Math.floor(Math.random() * YesOrNo.length)]
    if(random === 'yes') {
      coins[message.author.id] = {
        coins: MyCoins + amount
      }
      message.reply(`You Won! \n You got ${amount} coins!`)
    } else if(random === 'no') {
        coins[message.author.id] = {
         coins: MyCoins - amount
      }
      message.reply(`You Lose! \n You lost ${amount} coins!`)
    }

    fs.writeFile('./coins.json', JSON.stringify(coins), (err) => {
      if(err) console.log(err)
    })
  }


  if(message.content.startsWith(`${PREFIX}top`)){
    if(message.channel.id !== "934904933919117312") return message.reply("You can't do this here \n <#934904933919117312>")
    let CoinsJson = JSON.parse(fs.readFileSync('./coins.json'))
    
    var Sorted = Object.entries(CoinsJson).sort((a, b) => b[1].coins - a[1].coins)
    if(Sorted.length > 10) Sorted = Sorted.slice(0, 10)
    
    var LBString = [];
    let place = 1;
    console.log(Sorted)
    
    Sorted.forEach(user => {
      LBString += `**${place++}.** <@${user[0]}> - ${user[1].coins} coins! \n`
    })
    let embed = new MessageEmbed()
    .setTitle(`Top 10:`)
    .setDescription(LBString)
    .setFooter(client.user.tag, client.user.displayAvatarURL())
    .setTimestamp()
    message.channel.send(embed)
  }


  if(message.content.startsWith(`${PREFIX}rps`)){
    if(!coins[message.author.id]){
      coins[message.author.id] = {
        coins: 0
      }
    }
    let MyCoins = coins[message.author.id].coins
    let amount = parseInt(args[1])
    if(message.channel.id !== "934904933919117312") return message.reply("You can't do this here \n <#934904933919117312>")
    if(isNaN(amount) || !amount) return message.reply("Please enter a number of coins")
    if(MyCoins < amount) return message.reply(`You don't have ${amount} coins`)
    if(amount < 25) return message.reply("The minimum amount is `25`")
    let embed = new MessageEmbed()
    .setTitle("**__Choose:__**")
    .setDescription(`Rock / Paper / Scissors \n <@${message.author.id}>`)
    .setFooter(client.user.tag, client.user.displayAvatarURL())
    .setTimestamp()
    let msg = await message.channel.send(embed);
    await msg.react('✊🏽')
    await msg.react('✋🏽')
    await msg.react('✌🏽')
    const filter = (reaction, user) => {
      return ['✊🏽', '✋🏽', '✌🏽'].includes(reaction.emoji.name) && user.id === message.author.id
    }
      const choices = ['✊🏽', '✋🏽', '✌🏽']
      const bot = choices[Math.floor(Math.random() * choices.length)]
      console.log(bot)
      msg.awaitReactions(filter, { max: 1, time: 120000, error: ['time']}).then(
        async(collected) => {
          const reaction = collected.first()
          let result = new MessageEmbed()
          .setTitle("**__Game Result:__**")
          .addField(`You chose:`, `${reaction.emoji.name}`)
          .addField(`I chose:`, `${bot}`)
          .setColor('#0d0c0c')
          .setTimestamp()
          await msg.edit(result)
          
          if(bot === '✊🏽' && reaction.emoji.name === '✌🏽' ||
          bot === '✌🏽' && reaction.emoji.name === '✋🏽' || 
          bot === '✋🏽' && reaction.emoji.name === '✊🏽') {
            let lose = new MessageEmbed()
            .setTitle("**__Game Result:__**")
            .setDescription(`You Lose!`)
            .addFields(
              { name: `You chose:`, value: `${reaction.emoji.name}`},
              { name: `I chose:`, value: `${bot}`}
            )
            .setColor('#f20a29')
            .setTimestamp()
            await msg.edit(result = lose)
            coins[message.author.id] = {
              coins: coins[message.author.id].coins - amount
            }
          } else if(bot === reaction.emoji.name){
              let draw = new MessageEmbed()
              .setTitle("**__Game Result:__**")
              .setDescription(`It's a draw!`)
              .addFields(
                { name: `You chose:`, value: `${reaction.emoji.name}`},
                { name: `I chose:`, value: `${bot}`}
              )
              .setColor('black')
              .setTimestamp()
              await msg.edit(result = draw)
              return;

          } else {
              let win = new MessageEmbed()
              .setTitle("**__Game Result:__**")
              .setDescription("**__You Won!__**")
              .addFields(
                { name: `You chose:`, value: `${reaction.emoji.name}`},
                { name: `I chose:`, value: `${bot}`}
              )

              .setColor('#03ab11')
              .setTimestamp()
              await msg.edit(result = win)
              coins[message.author.id] = {
                coins: coins[message.author.id].coins + amount
            }
            return;
          }
          
        }
      )
      fs.writeFile('./coins.json', JSON.stringify(coins), (err) => {
        if(err) console.log(err)
      })
  }
  

  if(message.content.startsWith(`${PREFIX}flip`)){
    //flip
    //!flip 150
    if(!coins[message.author.id]){
      coins[message.author.id] = {
        coins: 0
      }
    }
    let MyCoins = coins[message.author.id].coins
    let amount = parseInt(args[1])
    if(message.channel.id !== "934904933919117312") return message.reply("You can't do this here \n <#934904933919117312>")
    if(isNaN(amount) || !amount) return message.reply("Please enter a number of coins")
    if(amount < 1) return message.reply("You can't give below 1 coin")
    if(MyCoins < amount) return message.reply(`You don't have ${amount} coins`)
    if(amount < 10) return message.reply("The minimum amount to bet is 10 coins")


    let embed = new MessageEmbed()
    .setTitle("Choose:")
    .setDescription("Heads / Tails")
    let msg = await message.channel.send(embed);
    await msg.react('1️⃣')
    await msg.react('🌲')
    
    const filter = (reaction, user) => {
      return ['1️⃣', '🌲'].includes(reaction.emoji.name) && user.id === message.author.id
    }
    const flip = ['tail', 'heads']
    let random = flip[Math.floor(Math.random() * flip.length)]
    console.log(random)
    msg.awaitReactions(filter, { max: 1, time: 120000, error: ['time']}).then(
      async(collected) => {
        const reaction = collected.first()
        let result = new MessageEmbed()
        .setTitle("**__Game Result:__**")
        .addField(`You chose:`, `${reaction.emoji.name}`)
        .addField(`I chose:`, `${random}`)
        .setColor('#0d0c0c')
        .setTimestamp()
        await msg.edit(result)
      if(random === 'tail' && reaction.emoji.name === '1️⃣' || random === 'heads' && reaction.emoji.name === '🌲') {
        coins[message.author.id] = {
          coins: MyCoins + amount
        }
        let win = new MessageEmbed()
        .setTitle("**__Game Result:__**")
        .setDescription(`You Won!`)
        .addFields(
          { name: `You chose:`, value: `${reaction.emoji.name}`},
          { name: `The result is:`, value: `${reaction.emoji.name}`}
        )
        .setColor('#22d40b')
        .setTimestamp()
        await msg.edit(result = win)
      } else {
        coins[message.author.id] = {
          coins: MyCoins - amount
        }
        let loseE
        if(reaction.emoji.name === '🌲'){
          loseE = '1️⃣'
        } else if(reaction.emoji.name === '1️⃣'){
          loseE = '🌲'
        }
        let lose = new MessageEmbed()
        .setTitle("**__Game Result:__**")
        .setDescription(`You Lose!`)
        .addFields(
          { name: `You chose:`, value: `${reaction.emoji.name}`},
          { name: `The result is:`, value: `${loseE}`}
        )
        .setColor('#e60b25')
        .setTimestamp()
        await msg.edit(result = lose)
    
      }
    })  
    fs.writeFile('./coins.json', JSON.stringify(coins), (err) => {
      if(err) console.log(err)
    })
  }
  
  if(message.content.startsWith(`${PREFIX}daily`)){
    if(!coins[message.author.id]){
      coins[message.author.id] = {
        coins: 0
      }
    }
    let UserCoins = coins[message.author.id].coins
    if(message.channel.id !== "934904933919117312") return message.reply("You can't do this here \n <#934904933919117312>")
    if(cooldown.has(message.author.id)) return message.reply("You have cooldown")
    if(message.author.bot) return;
    cooldown.add(message.author.id)
    let random = Math.floor(Math.random() * 250) + 1;
    coins[message.author.id] = {
      coins: UserCoins + random
    }
    let embed = new MessageEmbed()
    .setDescription(`You got ${random} coins! \n \n Come again in 24 hours`)
    .setColor('#22d40b')
    message.channel.send(embed)

    setTimeout(() => {
      cooldsown.delete(message.authir.id)
    }, 86400000)
    fs.writeFile('./coins.json', JSON.stringify(coins), (err) => {
      if(err) console.log(err)
    })
  }

//---------------------------------------------------------------------

  if(message.content.startsWith(`${PREFIX}work`)){
    if(!coins[message.author.id]){
      coins[message.author.id] = {
        coins: 0
      }
    }
    let UserCoins = coins[message.author.id].coins
    if(message.channel.id !== "934904933919117312") return message.reply("You can't do this here \n <#934904933919117312>")
    if(cooldown2.has(message.author.id)) return message.reply("You have cooldown")
    if(message.author.bot) return;
    cooldown2.add(message.author.id)
    const optionsFor25 = [
      'farmer',
      'teacher',
      'shepherd',
    ]
    const optionsFor150 = [
      'waiter',
      'lawyer',
      'doctor',
      'cop',
    ]
    const optionsFor250 = [
      'director of a high-tech company',
      'judge',
      'Famous football player'
    ]
    let random = Math.floor(Math.random() * 250) + 1;
    if(random <= 25){
      coins[message.author.id] = {
        coins: UserCoins + random
      }
      const random25 = optionsFor25[Math.floor(Math.random() * optionsFor25.length)]
      let farmer = new MessageEmbed()
      .setDescription(`You worked as a ${random25} and got ${random} coins.`)
      .setColor('#22d40b')
      message.reply(farmer)
    } 
    else if(random <= 150 && random > 25){
      coins[message.author.id] = {
        coins: UserCoins + random
      }
      const random150 = optionsFor150[Math.floor(Math.random() * optionsFor150.length)]
      let farmer = new MessageEmbed()
      .setDescription(`You worked as a ${random150} and got ${random} coins.`)
      .setColor('#22d40b')
      message.reply(farmer)    
    }
    else if( random > 150){
      coins[message.author.id] = {
        coins: UserCoins + random
      }
      const random250 = optionsFor250[Math.floor(Math.random() * optionsFor250.length)]
      let farmer = new MessageEmbed()
      .setDescription(`You worked as a ${random250} and got ${random} coins.`)
      .setColor('#22d40b')
      message.reply(farmer)
    }
    setTimeout(() => {
      cooldown2.delete(message.author.id)
    }, 600000)

    fs.writeFile('./coins.json', JSON.stringify(coins), (err) => {
      if(err) console.log(err)
    })
  }


  if(message.content.startsWith(`${PREFIX}crime`)){
    if(!coins[message.author.id]){
      coins[message.author.id] = {
        coins: 0
      }
    }
    let UserCoins = coins[message.author.id].coins
    if(message.channel.id !== "934904933919117312") return message.reply("You can't do this here \n <#934904933919117312>")
    if(cooldownCrime.has(message.author.id)) return message.reply("You have cooldown")
    cooldownCrime.add(message.author.id)
    let random = Math.floor(Math.random() * 401) - 200;
    console.log(random)
    const crimeWon = [
      'robbed a bank',
      
      
    ]
    const crimeLose = [
      'broke a television',
      'robbed an old woman and getting caught by the police',
      
    ]
    if(random > 0){
      coins[message.author.id] = {
        coins: UserCoins + random
      }
      const random200 = crimeWon[Math.floor(Math.random() * crimeWon.length)]
      let won = new MessageEmbed()
      .setDescription(`You ${random200} and got ${random} coins.`)
      .setColor('#22d40b')
      message.reply(won)
    }
    else if(random < 0) {
      coins[message.author.id] = {
        coins: UserCoins + random
      }
      const randomM200 = crimeLose[Math.floor(Math.random() * crimeLose.length)]
      let losecoins = (random - random) - random;
      console.log(losecoins)
      let lose = new MessageEmbed()
      .setDescription(`You ${randomM200} and you lose ${losecoins} coins.`)
      .setColor('#d90711')
      message.reply(lose)
    }
    setTimeout(() => {
      cooldownCrime.delete(message.author.id)
    }, 600000)

    fs.writeFile('./coins.json', JSON.stringify(coins), (err) => {
      if(err) console.log(err)
    })
  }
})



client.login(BOT_TOKEN)