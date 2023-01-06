const moment = require('moment');
const fetch = require('node-fetch');
const url = require('url');
const { expresstext } = require('./config.json');
const { name } = require('./config.json')
const db = require('quick.db');
const express = require('express');
const app = express();

app.get('/', (req, res) => {
	res.send(`${expresstext}`);
});

app.listen(3000, () => {
	console.log('Express Working');
});

const Discord = require('discord.js');
let client = new Discord.Client();
const Chat = require("easy-discord-chatbot");
const chat = new Chat({ name: `${name}` })

const { prefix } = require('./config.json');
const { token } = require('./config.json');
const { status } = require('./config.json');
const { statustype } = require('./config.json');
const { embedcolor } = require('./config.json');
const { logchannelID } = require('./config.json');
const { ModEmoji } = require('./config.json');
const { erroremoji } = require('./config.json');
const { OwnerEmoji } = require('./config.json');
const { ownerID } = require('./config.json');
const { SendLinksChannelID } = require('./config.json');
const { successemoji } = require('./config.json');
const { supportserver } = require('./config.json');
const { utiemoji } = require('./config.json');
const { CurrencyEmoji } = require('./config.json');
const { CurrencyName } = require('./config.json');
const { FunEmoji } = require('./config.json')

client.on('ready', () => {
	client.user.setActivity(`${status}`, { type: `${statustype}` });
	console.log(`${client.user.username} is online prefix = ${prefix}`);
	console.log(`Token = ${token}`);
	console.log(`Status = ${status}`);
	console.log(`Status type = ${statustype}`);
	console.log(`Color = ${embedcolor}`);
	console.log(`Logging channel = ${logchannelID}`);
	console.log(`Mod emoji = ${ModEmoji}`);
	console.log(`Owner emoji = ${OwnerEmoji}`);
	console.log(`Advertising Channel = ${SendLinksChannelID}`);
	console.log(`Uti Emoji = ${utiemoji}`);
	console.log(`Error Emoji = ${erroremoji}`);
	console.log(`Success Emoji = ${successemoji}`);
	console.log(`Support Server = ${supportserver}`);
	console.log(`Owner = ${ownerID}`);
	console.log(`Curency Emoji = ${CurrencyEmoji}`);
	console.log(`Currency Name = ${CurrencyName}`);
  console.log(`Fun Emoji = ${FunEmoji}`)
  console.log(`Name = ${name}`)
});


client.on("message", async message => {
  //setup chatbot
if(message.content.toLowerCase().startsWith(`${prefix}chatbot`)) {
        if(message.member.permissions.has('MANAGE_CHANNELS')) {
        let channel = message.mentions.channels.first()
        if(!channel) {
            return message.channel.send('You need to provide a channel')
        }
        
        db.set(`chat_${message.guild.id}`, channel.id)
        message.channel.send(`${successemoji} | Bot saved chat channel`)
        } else {
            message.channel.send('You dont have perms')
        }
    }

    //delchatbot
    if(message.content.toLowerCase().startsWith(`${prefix}delchatbot`)) {
        if(message.member.permissions.has('MANAGE_CHANNELS')) {
        let channel = message.mentions.channels.first()
        if(!channel) {
            return message.channel.send('You need to provide a channel')
        }
        
        db.delete(`chat_${message.guild.id}`)
        message.channel.send(`${successemoji} | Bot deleted chat channel`)
        } else {
            message.channel.send('You dont have perms')
        }
    }
})

//chatbot
client.on("message", async message => {
const channel = db.get(`chat_${message.guild.id}`)
if(message.channel.id === `${channel}` &&
 !message.author.bot) { 
 let reply = await chat.chat(message.content)
 client.channels.cache.get(channel).send(reply)
 }
})


//Snipe Collection
let snipe = new Discord.Collection();
client.on('messageDelete', message => {
	if (message.author.bot) return;
	snipe.set(message.channel.id, {
		content: message.content,
		author: message.author
	});
});
client.on('message', message => {
	//snipe commandon different message event
	if (message.author.bot) return;
	if (message.content.toLowerCase() === `${prefix}snipe`) {
		const msg = snipe.get(message.channel.id);
		if (!msg) return message.channel.send(' :x: | Theres Nothing To Snipe');
		const embed = new Discord.MessageEmbed()
			.setTitle('Last Deleted Message')
			.setColor(`${embedcolor}`)
			.setTimestamp()
			.setThumbnail(`${msg.author.displayAvatarURL({ dynamic: true })}`)
			.addFields(
				{ name: 'Sender', value: msg.author.username },
				{ name: 'Content', value: msg.content }
			);
		message.channel.send(embed);
	}
});

//delete words
client.on('message', message => {
	if (message.channel.type === 'DM') return;
	if (message.author.bot) return;
	//Banned words will go here
	if (message.content.toLowerCase().includes('fuck')) {
		message.delete();
		message.author.send('Please do not use the word `fuck`');
		message.reply('Do **NOT** say that');
		let badword1 = new Discord.MessageEmbed()
			.setTitle('BadWords Log')
			.setDescription(`${message.author} said \`fuck\``)
			.setFooter('Coded by Mark')
			.setColor(`${embedcolor}`);
		client.channels.cache.get(`${logchannelID}`).send(badword1);
	}
	if (message.content.toLowerCase().includes('shit')) {
		message.delete();
		message.author.send('Please do not use the word `shit`');
		message.reply('Do **NOT** say that');
		let badword2 = new Discord.MessageEmbed()
			.setTitle('BadWords Log')
			.setDescription(`${message.author} said \`shit\``)
			.setFooter('Coded by Mark')
			.setColor(`${embedcolor}`);
		client.channels.cache.get(`${logchannelID}`).send(badword2);
	}
	if (message.content.toLowerCase().includes('crap')) {
		message.delete();
		message.author.send('Please do not use the word `crap`');
		message.reply('Do **NOT** say that');
		let badword3 = new Discord.MessageEmbed()
			.setTitle('BadWords Log')
			.setDescription(`${message.author} said \`crap\``)
			.setFooter('Coded by Mark')
			.setColor(`${embedcolor}`);
		client.channels.cache.get(`${logchannelID}`).send(badword3);
	}
	if (message.content.toLowerCase().includes('nigga')) {
		message.delete();
		message.author.send('Please do not use the word `nigga`');
		message.reply('Do **NOT** say that');
		let badword4 = new Discord.MessageEmbed()
			.setTitle('BadWords Log')
			.setDescription(`${message.author} said \`nigga\``)
			.setFooter('Coded by Mark')
			.setColor(`${embedcolor}`);
		client.channels.cache.get(`${logchannelID}`).send(badword4);
	}
	if (message.content.toLowerCase().includes('nigger')) {
		message.delete();
		message.author.send('Please do not use the word `nigger`');
		message.reply('Do **NOT** say that');
		let badword5 = new Discord.MessageEmbed()
			.setTitle('BadWords Log')
			.setDescription(`${message.author} said \`nigger\``)
			.setFooter('Coded by Mark')
			.setColor(`${embedcolor}`);
		client.channels.cache.get(`${logchannelID}`).send(badword5);
	}
});

//delete links
client.on('message', message => {
	if (message.author.bot) return;
	if (message.channel.type === 'DM') return;
	if (message.channel.id === `${SendLinksChannelID}`) return;
	if (
		message.content.toLowerCase().includes('https://') ||
		message.content.toLowerCase().includes('http://') ||
		message.content.toLowerCase().includes('discord.gg/')
	) {
		if (message.member.hasPermission('MANAGE_MESSAGES')) {
		} else {
			message.delete();
			message.channel.send(
				`${
					message.author
				}, Nice try but you cannot send links unless you have \`MANAGE_MESSAGES\`, if you want to send a link send it in <#${SendLinksChannelID}>`
			);
			message.author.send(
				`Sorry, but we had to take down your link because we do not allow members to send links`
			);
			let link = new Discord.MessageEmbed()
				.setTitle('BadLinks Log')
				.setDescription(`${message.author} tried to send a \`link\``)
				.setFooter('Coded by Mark')
				.setColor(`${embedcolor}`);
			client.channels.cache.get(`${logchannelID}`).send(link);
		}
	}
});

//currency
client.on('message', async message => {
	if (message.author.bot) return;

//shop command
	if (message.content.toLowerCase() === `${prefix}store` ||message.content.toLowerCase() === `${prefix}shop`) {
		let store = new Discord.MessageEmbed()
			.setTitle('Items')
			.setDescription(
				`
FortniteGiftCard, 19 ${CurrencyName}
Car, 50,000 ${CurrencyName}
Kit, 500 ${CurrencyName}
Blob, 10,000 ${CurrencyName}
Mansion, 300,000`
			)
			.setFooter(`Type: ${prefix}buy <item>`)
			.setColor(`${embedcolor}`);
		message.channel.send(store);
	}

	//work command
	if (message.content.toLowerCase().startsWith(`${prefix}work`)) {
		const check = await db.get(`workCheck_${message.author.id}`);
		let timeout = 100000;
		if (check !== null && timeout - (Date.now() - check) > 0) {
			const ms = require('pretty-ms');
			const timeLeft = ms(timeout - (Date.now() - check));
			message.reply(
				`${erroremoji}You have already worked come back after ${timeLeft}`
			);
		} else {
			let currency = `${CurrencyEmoji}`;
			let money =
				Math.round(Math.random() * 2000) ||
				Math.round(Math.random() * 0) ||
				Math.round(Math.random() * 1000);
			let worked = [
				`You cut the grass, and got ${money} ${CurrencyName}, noice!`,
				`You fell off the ground and got ${money} ${CurrencyName}, hah free money!`,
				`You typed ${prefix}work and got ${money} ${CurrencyName}, well idk what to say...`,
				`Here get your ${money} ${CurrencyName}`,
				`You helped someone and got ${money} ${CurrencyName}`
			];
			let currentWallet = await db.get(`wallet_${message.author.id}`);
			let currentBank = await db.get(`bank_${message.author.id}`);
			await db.set(`wallet_${message.author.id}`, currentWallet + money);
			await db.set(`workCheck_${message.author.id}`, Date.now());
			let embed = new Discord.MessageEmbed()
				.setTitle(`${CurrencyEmoji} You worked! ${CurrencyEmoji}`)
				.setDescription(worked[Math.floor(Math.random() * worked.length)])
				.setColor(`${embedcolor}`);
			message.channel.send(embed);
		}
	} 

  //beg command
  if(message.content.toLowerCase().startsWith(`${prefix}beg`)) {
		const check = await db.get(`beg_${message.author.id}`);
		let timeout1 = 50000;
		if (check !== null && timeout1 - (Date.now() - check) > 0) {
			const ms = require('pretty-ms');
			let timeLeft2 = ms(timeout1 - (Date.now() - check));
			message.reply(
				`${erroremoji} | You have already begged come back after ${timeLeft2}`
			);
		} else {
			let currency = `${CurrencyEmoji}`;
			let money =
				Math.round(Math.random() * 2000) ||
				Math.round(Math.random() * 0) ||
				Math.round(Math.random() * 1000);
			let worked = [
				`Mark gave you ${money} ${CurrencyName}, noice!`,
				`You begged so much that Blob gave you ${money} ${CurrencyName}!`,
				`You typed ${prefix}beg and got ${money} ${CurrencyName}`,
				`Bill gates gave you ${money} ${CurrencyName}`,
				`Ill pay you to stop begging, here is ${money} ${CurrencyName}`
			];
			let currentWallet = await db.get(`wallet_${message.author.id}`);
			let currentBank = await db.get(`bank_${message.author.id}`);
			await db.set(`wallet_${message.author.id}`, currentWallet + money);
			await db.set(`beg_${message.author.id}`, Date.now());
			let embed = new Discord.MessageEmbed()
				.setTitle(`${CurrencyEmoji} You Begged! ${CurrencyEmoji}`)
				.setDescription(worked[Math.floor(Math.random() * worked.length)])
				.setColor(`${embedcolor}`);
			message.channel.send(embed);
		}
	}

	//daily command
	if (message.content.toLowerCase().startsWith(`${prefix}daily`)) {
		let currency = `${CurrencyEmoji}`;
		const check = await db.get(`dailyCheck_${message.author.id}`);
		const timeout = 86400000;
		if (check !== null && timeout - (Date.now() - check) > 0) {
			const ms = require('pretty-ms');
			const timeLeft = ms(timeout - (Date.now() - check));
			let fail = new Discord.MessageEmbed()
			.setTitle("You have already claimed your daily!")
				.setColor(`${embedcolor}`)
				.setDescription(
					`${erroremoji}Nice try, but you've already claimed your daily for today!\nCome back after ${timeLeft} for your next daily.`
				)
			message.channel.send(fail);
		} else {
			let reward = 25000;
			let currentBalance = await db.get(`wallet_${message.author.id}`);
			let success = new Discord.MessageEmbed()
				.setTitle('You claimed your daily!')
				.setColor(`${embedcolor}`)
				.setDescription(
					`Nice job, you just claimed ${currency} ${reward.toLocaleString()}!\nCome back tomorrow for another ${currency} ${reward.toLocaleString()}!`
				)
				.setTimestamp();
			message.channel.send(success);
			await db.set(`wallet_${message.author.id}`, currentBalance + reward);
			await db.set(`dailyCheck_${message.author.id}`, Date.now());
		}
	}

	//balance command
	if (message.content.toLowerCase().startsWith(`${prefix}bal`) ||message.content.toLowerCase().startsWith(`${prefix}balance`)) {
		let user = message.mentions.users.first() || message.author;
		let balance = await db.get(`wallet_${user.id}`);
		console.log(balance);
		let bank = await db.get(`bank_${user.id}`);
		console.log(bank);
		if (balance === null) balance = 0;
		if (bank === null) bank = 0;
		let balbalance = new Discord.MessageEmbed()
			.setTitle(`${user.username}'s Balance ${CurrencyEmoji}`)
			.setDescription(
				`${CurrencyEmoji} **${CurrencyName}:** \n Wallet: ${balance}\n Bank: ${bank}`
			)
			.setColor(`${embedcolor}`);
		message.channel.send(balbalance);
	}

	//inv
	if (message.content.toLowerCase().startsWith(`${prefix}inventory`) ||message.content.toLowerCase().startsWith(`${prefix}inv`)) {
		let user = message.mentions.users.first() || message.author;
		let items = db.get(user.id);
		if (items === null) items = 'User has no items';

		let inv = new Discord.MessageEmbed()
			.setTitle(`${user.username}'s Inventory`)
			.addField('Inventory', items)
			.setColor(`${embedcolor}`);
		message.channel.send(inv);
		console.log(db.fetch(`user_${user.id}`, items));
	}

	//buy kit
	if (message.content.toLowerCase().startsWith(`${prefix}buy kit`) ||message.content.toLowerCase().startsWith(`${prefix}purchase kit`)) {
		let args = message.content.slice(1).split(' ');
		let bal = db.fetch(`wallet_${message.author.id}`);
		if (bal < 500) {
			message.reply(
				`${erroremoji}Insufficient Funds! | You need at least \`500\` ${CurrencyName}${CurrencyEmoji} in order to complete this transaction. `
			);
		} else {
			let items = db.fetch(message.author.id, { items: [] });
			db.push(`${message.author.id}`, 'kit');
			message.channel.send(
				'Purchase Completed | You have successfully bought `1x` kit.'
			);
			db.subtract(`wallet_${message.author.id}`, 500);
			console.log(db.fetch(`wallet_${message.author.id}`));
		}
	}

	//buy car
	if (message.content.toLowerCase().startsWith(`${prefix}buy car`) ||message.content.toLowerCase().startsWith(`${prefix}purchase car`)) {
		let args = message.content.slice(1).split(' ');
		let bal = db.fetch(`wallet_${message.author.id}`);
		if (bal < 50000) {
			message.reply(
				`${erroremoji}Insufficient Funds! | You need at least \`50000\` ${CurrencyName}${CurrencyEmoji} in order to complete this transaction. `
			);
		} else {
			let items = db.fetch(message.author.id, { items: [] });
			db.push(`${message.author.id}`, 'car');
			message.channel.send(
				'Purchase Completed | You have successfully bought `1x` car.'
			);
			db.subtract(`wallet_${message.author.id}`, 50000);
			console.log(db.fetch(`wallet_${message.author.id}`));
		}
	}

	//buy fortnitegiftcard
	if (message.content.toLowerCase().startsWith(`${prefix}buy fortnitegiftcard`) ||message.content.toLowerCase().startsWith(`${prefix}purchase fortnitegiftcard`)) {
		let args = message.content.slice(1).split(' ');
		let bal = db.fetch(`wallet_${message.author.id}`);
		if (bal < 19) {
			message.reply(
				`${erroremoji}Insufficient Funds! | You need at least \`19\` ${CurrencyName}${CurrencyEmoji} in order to complete this transaction. `
			);
		} else {
			let items = db.fetch(message.author.id, { items: [] });
			db.push(`${message.author.id}`, 'FortniteGiftCard');
			message.channel.send(
				'Purchase Completed | You have successfully bought `1x` Fortnite Gift Card.'
			);
			db.subtract(`wallet_${message.author.id}`, 19);
			console.log(db.fetch(`wallet_${message.author.id}`));
		}
	}

	//buy blob
	if (
		message.content.toLowerCase().startsWith(`${prefix}buy blob`) ||
		message.content.toLowerCase().startsWith(`${prefix}purchase blob`)
	) {
		let args = message.content.slice(1).split(' ');
		let bal = db.fetch(`wallet_${message.author.id}`);
		if (bal < 10000) {
			message.reply(
				`${erroremoji}Insufficient Funds! | You need at least \`10000\` ${CurrencyName}${CurrencyEmoji} in order to complete this transaction. `
			);
		} else {
			let items = db.fetch(message.author.id, { items: [] });
			db.push(`${message.author.id}`, 'blob');
			message.channel.send(
				'Purchase Completed | You have successfully bought `1x` blob.'
			);
			db.subtract(`wallet_${message.author.id}`, 10000);
			console.log(db.fetch(`wallet_${message.author.id}`));
		}
	}

	//buy mansion
	if (message.content.toLowerCase().startsWith(`${prefix}buy mansion`) ||message.content.toLowerCase().startsWith(`${prefix}purchase mansion`)
	) {
		let args = message.content.slice(1).split(' ');
		let bal = db.fetch(`wallet_${message.author.id}`);
		if (bal < 300000) {
			message.reply(
				`${erroremoji}Insufficient Funds! | You need at least \`300000\` ${CurrencyName}${CurrencyEmoji} in order to complete this transaction. `
			);
		} else {
			let items = db.fetch(message.author.id, { items: [] });
			db.push(`${message.author.id}`, 'Mansion');
			message.channel.send(
				'Purchase Completed | You have successfully bought `1x` mansion.'
			);
			db.subtract(`wallet_${message.author.id}`, 300000);
			console.log(db.fetch(`wallet_${message.author.id}`));
		}
	}

	//pay command
	if (message.content.toLowerCase().startsWith(`${prefix}pay`)) {
		db.fetch(`wallet_${message.author.id}`);
		let user = message.mentions.users.first();
		if (!user) {
			return message.channel.send(`${erroremoji} | Mention someone to pay`);
		}
		let currentWallet2 = await db.get(`wallet_${user.id}`);
		let currentWallet1 = await db.get(`wallet_${message.author.id}`);

		let args = message.content.split(' ').slice(1);
		if (!args[1]) return message.reply('How much coins to you want to PAY');
		if (currentWallet1 < args[1]) {
			return message.channel.send(
				` ${erroremoji}Insufficient Funds! | You need at least`
			);
		}
		if (args[1] < 0) {
			return message.channel.send(`${erroremoji} | You can't do less than 0`);
		}
		await db.subtract(`wallet_${message.author.id}`, args[1]);
		await db.add(`wallet_${user.id}`, args[1]);
		message.channel.send(
			`Succesfully Paid ${CurrencyEmoji}**${args[1]} ${CurrencyName}**`
		);
	}

	//deposit command
	if (message.content.toLowerCase().startsWith(`${prefix}dep`) ||message.content.toLowerCase().startsWith(`${prefix}deposit`)
	) {
		const args = message.content.split(' ').slice();
		if (args[1] < 0) {
			return message.channel.send(`${erroremoji} | You can't do less than 0`);
		}
		const currentWallet = await db.get(`wallet_${message.author.id}`);
		const currentBank = await db.get(`bank_${message.author.id}`);
		if (args[1] > currentWallet) {
			return message.channel.send(
				`${erroremoji} | You are to broke to do that`
			);
		}
		db.subtract(`wallet_${message.author.id}`, args[1]);
		db.add(`bank_${message.author.id}`, args[1]);
		message.channel.send(
			`${successemoji} | Successfully Deposited **${args[1]} ${CurrencyName}**`
		);
	}

	//withdraw command
	if (message.content.toLowerCase().startsWith(`${prefix}withdraw`) ||message.content.toLowerCase().startsWith(`${prefix}with`)) {
		const args = message.content.split(' ').slice();
		if (args[1] < 0) {
			return message.channel.send(`${erroremoji} | You can't do less than 0`);
		}
		const currentWallet = await db.get(`wallet_${message.author.id}`);
		const currentBank = await db.get(`bank_${message.author.id}`);
		if (args[1] > currentBank) {
			return message.channel.send(
				`${erroremoji} | You are to broke to do that`
			);
		}
		db.add(`wallet_${message.author.id}`, args[1]);
		db.subtract(`bank_${message.author.id}`, args[1]);
		message.channel.send(
			`${successemoji} | Successfully Withdrew **${args[1]} ${CurrencyName}**`
		);
	}

	//rob command
	if(message.content.toLowerCase().toLowerCase().startsWith(`${prefix}rob`)) {
    let user = message.mentions.users.first();
		if (!user) {
			return message.channel.send(
				`${erroremoji} | You need to mention someone to rob`)
		}
  	const rob = await db.get(`rob_${message.author.id}`);
		let timeout1 = 300000;
		if (rob !== null && timeout1 - (Date.now() - rob) > 0) {
    let ms = require('pretty-ms');
		let timeLeft2 = ms(timeout1 - (Date.now() - rob));
			message.reply(`${erroremoji} | You have already robbed come back after ${timeLeft2}`);
		} else {
      await db.get(`wallet_${message.author.id}`);
     let userm = await db.get(`wallet_${user.id}`)
		 let rmoney = Math.round(Math.random() * userm)
			let robbed = await db.get(`wallet_${user.id}`);
      if(userm === null) {
        return message.channel.send(`You can't rob them they have 0 ${CurrencyName} in their wallet`)
      }
      if(robbed < rmoney) {
        return message.channel.send(`${erroremoji} | HAHA You failed to rob ${user.username} you can try again until its successful`)
      }
				await db.add(`wallet_${message.author.id}`, rmoney)
				await db.subtract(`wallet_${user.id}`, rmoney);
				await db.set(`rob_${message.author.id}`, Date.now())
				message.channel.send(`${successemoji} | Successfully Robbed ${rmoney} ${CurrencyName} from ${user.username}`)
		}
	}

})

//fun Commands
client.on('message', async message => {
  if(message.author.bot) return;
  if(message.channel.type === 'DM') return;

  //kiss Command
if(message.content.toLowerCase().startsWith(`${prefix}kiss`)) {
 let user = message.mentions.members.first() 
 
 
 if(!user) {
   return message.reply(`${erroremoji} | You need to mention someone!`)
 }
 
 let slappers = [
   "https://c.tenor.com/hK8IUmweJWAAAAAC/kiss-me-%D0%BB%D1%8E%D0%B1%D0%BB%D1%8E.gif",
   "https://cdn.myanimelist.net/s/common/uploaded_files/1483589602-6b6484adddd5d3e70b9eaaaccdf6867e.gif",
   "https://c.tenor.com/I8kWjuAtX-QAAAAM/anime-ano.gif",
   "https://i.pinimg.com/originals/58/bd/29/58bd29ff879af961e41e7f7096f5c0aa.gif",
   "https://thumbs.gfycat.com/HopefulFabulousKouprey-max-1mb.gif",
   "https://data.whicdn.com/images/106742359/original.gif",
   "https://acegif.com/wp-content/uploads/anime-kissin-3.gif",
   "https://c.tenor.com/Aaxuq2evHe8AAAAM/kiss-cute.gif",
   "https://cutewallpaper.org/21/cute-anime-kiss/Anime-Cute-GIF-Anime-Cute-Kiss-Discover-and-Share-GIFs.gif",
   "https://media4.giphy.com/media/11GnTlz9rJ07Mk/giphy.gif",
   "https://cutewallpaper.org/21/kiss-anime-pictures/forehead-kiss-anime-Album-on-Imgur.gif",
   "https://cutewallpaper.org/21/anime-passionate-kiss/Anime-Scums-Wish-GIF-Anime-ScumsWish-Passionate-Discover-Share-GIFs.gif",
   "https://cdn.myanimelist.net/s/common/uploaded_files/1483589646-9c8cd327454990f5da24af7d3f057627.gif",
   "http://37.media.tumblr.com/b12bd032e97037081108f993aadcae62/tumblr_mwo343m7tK1sv72vno1_500.gif",
   "https://aniyuki.com/wp-content/uploads/2021/07/aniyuki-anime-gif-kiss-85.gif",
   "https://i.pinimg.com/originals/6e/2f/e9/6e2fe9073f4e6aa4080e2e9ab5e3f790.gif",
   "https://thumbs.gfycat.com/PreciousSharpBuffalo-size_restricted.gif"
     ];
 let embed = new Discord.MessageEmbed()
 .setColor(`${embedcolor}`)
 .setDescription(`👄 **|** **${message.author}** *kissed*  **${user}**`)
 .setImage(`${slappers[Math.floor(Math.random() * slappers.length)]}`)
 .setFooter(`👀`)
 
 message.channel.send(embed)
 }

 //cuddle command
 if(message.content.toLowerCase().startsWith(`${prefix}cuddle`)) {
 let user = message.mentions.members.first() 
 
 
 if(!user) {
   return message.reply(`${erroremoji} | You need to mention someone!`)
 }
 
 let slappers = [
   "https://media.discordapp.net/attachments/870077973196328960/880195909454032936/image0.gif?width=448&height=249",
   "https://media.discordapp.net/attachments/870077973196328960/880195909823119402/image1.gif?width=387&height=218",
   "https://media.discordapp.net/attachments/870077973196328960/880195910167040091/image2.gif?width=180&height=102",
   "https://media.discordapp.net/attachments/870077973196328960/880195910473220116/image3.gif?width=448&height=252",
   "https://media.discordapp.net/attachments/870077973196328960/880197181225709578/image0.gif?width=198&height=220",
   "https://media.discordapp.net/attachments/870077973196328960/880197181552877628/image1.gif?width=432&height=243",
   "https://media.discordapp.net/attachments/870077973196328960/880197181905203220/image2.webp?width=450&height=301",
   "https://i.imgur.com/9V8wVuE.gif",
   "https://c.tenor.com/0KJtODIw0UkAAAAM/anime-cuddle.gif",
   "https://i.kym-cdn.com/photos/images/newsfeed/001/153/417/104.gif",
   "https://acegif.com/wp-content/gif/anime-hug-21.gif",
   "https://acegif.com/wp-content/gif/anime-hug-19.gif",
   "http://i.imgur.com/tuH4gqZ.gif",
   "https://cutewallpaper.org/21/hugs-anime/Hugs-for-everyone-3-image-Anime-Fans-of-DBolical-Indie-DB.gif"
     ];
 let embed = new Discord.MessageEmbed()
 .setColor(`${embedcolor}`)
 .setDescription(`🤗 **|** **${message.author}** *cuddled*  **${user}**`)
 .setImage(`${slappers[Math.floor(Math.random() * slappers.length)]}`)
 .setFooter(`👀`)
 
 message.channel.send(embed)
 }

 //cookfor command
 if(message.content.toLowerCase().startsWith(`${prefix}cookfor`)) {
 let user = message.mentions.members.first() 
 
 
 if(!user) {
   return message.reply(`${erroremoji} | You need to mention someone!`)
 }
 
 let slappers = [
   "https://data.whicdn.com/images/321924961/original.gif",
 "https://64.media.tumblr.com/e3a68f78652fc3e40c966385ad88b6d9/b212e7a9364163de-59/s540x810/3d933b5810c176244ce775763b6c5bc2e8ae3bf2.gif",
  "https://cdn.shopify.com/s/files/1/0790/6707/files/yakisoba.gif",
 "https://i.imgur.com/td0nRnR.gif",
 "https://i.pinimg.com/originals/9e/ed/4e/9eed4ebe43edab41b25d908d5a0e188a.gif",
 "https://img.buzzfeed.com/buzzfeed-static/static/2017-11/27/12/asset/buzzfeed-prod-fastlane-03/anigif_sub-buzz-17930-1511804381-7.gif?downsize=700:*&output-format=auto&output-quality=auto",
 "https://64.media.tumblr.com/e024be50ccd1e74cabfbcbf064a778fd/tumblr_nsdsakjwn81ruv1gno1_500.gif",
 "https://thumbs.gfycat.com/DelectablePepperyAlligatorsnappingturtle-max-1mb.gif",
 "https://i.gifer.com/T0ao.gif",
 "https://i.chzbgr.com/full/9137818368/h3078E75B/packaged-goods",
 "http://25.media.tumblr.com/d63681d1cd8dd4dcaf6e036f3fe6d96d/tumblr_mtwzw8Rzow1s4uarco1_500.gif",
 "https://static-storychat.pstatic.net/2021/6/22/30/3406680_nb5975fb825dh2.gif",
 "https://c.tenor.com/74Jcm5kI_AAAAAAM/food-anime.gif",
 "https://thumbs.gfycat.com/ScholarlyImportantAngelfish-size_restricted.gif",
 "https://i.pinimg.com/originals/99/71/83/997183d0eecfa635b9f7dc21a1d5d057.gif",
 "https://nerdist.com/wp-content/uploads/2020/04/flavors-of-youth.gif",
 "https://64.media.tumblr.com/c5fa500952952ff19cfae4508e0c227d/25d70070b1e7bc59-e2/s500x750/1da4be8327701c046a9a35ad05027b8196659b4f.gifv",
 "https://i.pinimg.com/originals/0b/1a/ba/0b1abad14d514105bb186fcfd5ddb07b.gif"
     ];
 let embed = new Discord.MessageEmbed()
 .setColor(`${embedcolor}`)
 .setDescription(`👩‍🍳 **|** **${message.author}** *cooked for*  **${user}**`)
 .setImage(`${slappers[Math.floor(Math.random() * slappers.length)]}`)
 .setFooter(`👀`)
 
 message.channel.send(embed)
 }

 //hug command
 if(message.content.toLowerCase().startsWith(`${prefix}hug`)) {
 let user = message.mentions.members.first() 
 
 
 if(!user) {
   return message.reply(`${erroremoji} | You need to mention someone!`)
 }
 
 let slappers = [
   "https://c.tenor.com/ixaDEFhZJSsAAAAM/anime-choke.gif",
   "https://66.media.tumblr.com/8d7f21698a2e2c85bf9ff7a829488336/tumblr_nmrmhleuYw1u4zujko1_400.gif",
   "https://data.whicdn.com/images/124011841/original.gif",
   "https://monophy.com/media/kvKFM3UWg2P04/monophy.gif",
   "https://acegif.com/wp-content/gif/anime-hug-73.gif",
   "https://1.bp.blogspot.com/-86yVsCoo8Lg/YG74owL3TRI/AAAAAAAAD_g/bzEb8XecokcC7jyolOFu6w44nhklUSCwQCLcBGAsYHQ/s296/anime%2Bhug%2Bgif1.gif",
   "https://c.tenor.com/dbIbtIyByEwAAAAM/cuddle-anime.gif",
   "http://i.imgur.com/gmiJEbu.gif",
   "https://i.imgur.com/ntqYLGl.gif",
  "https://64.media.tumblr.com/db736b7f7e2583d3970f37a90dee89c2/tumblr_pm3mzc6zcZ1y5gr1do1_500.gif",
  "https://acegif.com/wp-content/gif/anime-hug-45.gif",
  "https://media2.giphy.com/media/xT1R9yzqpvhPETYoV2/giphy.gif",
  "https://c.tenor.com/S3KQ1sDod7gAAAAC/anime-hug-love.gif"
     ];
 let embed = new Discord.MessageEmbed()
 .setColor(`${embedcolor}`)
 .setDescription(`🤗 **|** **${message.author}** *hugged*  **${user}**`)
 .setImage(`${slappers[Math.floor(Math.random() * slappers.length)]}`)
 .setFooter(`👀`)
 
 message.channel.send(embed)
 }

//slap command
if(message.content.toLowerCase().startsWith(`${prefix}slap`)) {
 let user = message.mentions.members.first() 
 
 
 if(!user) {
   return message.reply(`${erroremoji} | You need to mention someone!`)
 }
 
 let slappers = [
   "https://media1.tenor.com/images/b6d8a83eb652a30b95e87cf96a21e007/tenor.gif?itemid=10426943",
 "https://i.gifer.com/2Dji.gif",
 "http://i.imgur.com/lYxSTLA.gif",
 "https://media0.giphy.com/media/kHl4YDI8GLYVXDBV7r/giphy.gif?cid=6c09b952vlroa76qqbcxrrif13ckdq2jk1cajg6yv8kaqlpe&rid=giphy.gif&ct=s",
 "http://pa1.narvii.com/5728/7b796b9cd6a6f44ef6b0aabee0d28d1351fdc7be_hq.gif",
 "https://i.imgur.com/XoiO3Uz.gif",
 "https://media0.giphy.com/media/lSDqu7IbMqMiQvCjjN/giphy.gif",
 "https://i.imgur.com/uwHDm3r.gif",
 "https://c.tenor.com/_hOx_MqEN_YAAAAd/mosquito-anime.gif",
 "https://media0.giphy.com/media/OQ7phVSLg3xio/giphy.gif",
 "https://i.gifer.com/WpWp.gif",
 "https://media0.giphy.com/media/m6etefcEsTANa/giphy.gif",
 "https://thumbs.gfycat.com/IllinformedRigidAfricangoldencat-size_restricted.gif",
 "https://i.pinimg.com/originals/bf/ef/b4/bfefb401ed8f1f7a3fee62d76a2856a4.gif",
 "http://www.commercialgifs.com/wp-content/uploads/2021/04/Head-Slapping.gif",
 "https://media.tenor.co/videos/2c3c9e14cd80605e1afb83baf1d75bbc/mp4",
 "https://media.tenor.co/videos/09307032b404d283eec9761971d9595c/mp4",
 "https://media.tenor.co/videos/611aaf5c3e73b43b70de23e97a2268fe/mp4",
 "https://media.tenor.co/videos/b16614ffcbcfd215ef5af3366016e16f/mp4"
     ];
 let embed = new Discord.MessageEmbed()
 .setColor(`${embedcolor}`)
 .setDescription(`🤚 **|** **${message.author}** *slapped*  **${user}**`)
 .setImage(`${slappers[Math.floor(Math.random() * slappers.length)]}`)
 .setFooter(`👀`)
 
 message.channel.send(embed)
 }

})


client.on('message', async message => {
	if (message.author.bot) return;
	if (message.channel.type === 'DM') return;
	//commands stay below this

  //
  if(message.content.toLowerCase() === `${prefix}`) {
    message.channel.send(`Need help type \`${prefix}help\``)
  }

	//help command
	if(message.content.toLowerCase() === `${prefix}help`) {
		let help = new Discord.MessageEmbed()
			.setTitle(`${client.user.username}'s Commands`)
			.setDescription(
				`My prefix is \`${prefix}\`
[✨Support Server](${supportserver}) | [🤖Invite Me]({
					client.user.id
				}&scope=bot&permissions=8) | [📗discord]()`
			)
      .addField(
        `Setup Commands🛡`,
        `\`${prefix}chatbot #channel\`, \`${prefix}delchatbot #channel\``
      )
			.addField(
				`Mod Commands${ModEmoji}`,
				`\`${prefix}warn <@user> <reason>\`, \`${prefix}kick <@user>\`, \`${prefix}ban <@user>\`, \`?lock\`, \`?unlock\`, \`${prefix}snipe\`, \`${prefix}sudo <@user> <text>\`, \`${prefix}unban <ID>\`, \`${prefix}slowmode <seconds>\`, \`${prefix}embed\``
			)
			.addField(
				`Owner Commands${OwnerEmoji}`,
				`\`${prefix}eval\`, \`${prefix}say <text>\``
			)
			.addField(
				`Utility Commands${utiemoji}`,
				`\`${prefix}dm <@user> <text>\`, \`${prefix}emojistats\`, \`${prefix}serverinfo\`, \`${prefix}whois <@user>\``
			)
      .addField(
        `Fun Commands ${FunEmoji}`,
        `\`${prefix}kiss <@user>\`, \`${prefix}cookfor <@user>\`, \`${prefix}cuddle <@user>\`, \`${prefix}hug <@user>\`, \`${prefix}slap <@user>\``
      )
			.addField(
				`Currency Commands ${CurrencyEmoji}`,
				`\`${prefix}daily\`, \`${prefix}bal\`, \`${prefix}work\`, \`${prefix}inventory\`, \`${prefix}store\`, \`${prefix}pay <@user> <amount>\`, \`${prefix}beg\`, \`${prefix}deposit <amount>\`, \`${prefix}withdraw <amount>\`, \`${prefix}rob <@user>\``
			)
			.setFooter('Does this help❔')
			.setColor(`${embedcolor}`);
		message.channel.send(help);
	}


	//warn command
	if (message.content.toLowerCase().startsWith(`${prefix}warn`)) {
		if (message.member.hasPermission('MANAGE_MESSAGES')) {
			let victim = message.mentions.users.first();
			if (!victim)
				message.channel.send(`Mention someone to warn
 Example: \`${prefix}warn <@someone>\``);
			else {
				const sentence = message.content
					.split(' ')
					.slice(1)
					.join(' ');
				if (!sentence) return message.reply('Please provide a reason!');
				let embed = new Discord.MessageEmbed()
					.setTitle('Warning!')
					.setDescription(`${victim} **was warned, because ${sentence}**`)
					.setColor(`${embedcolor}`)
					.setFooter(`WARNED BY: ${message.author.username}`)
					.setTimestamp();

				message.channel.send(embed);
			}
		} else {
			message.reply(`${erroremoji} | You don't have permission to do that!`);
		}
	}

	//kick command
	if (message.content.toLowerCase().startsWith(`${prefix}kick`)) {
		if (message.member.hasPermission('KICK_MEMBERS')) {
			let member = message.mentions.members.first();
			if (!member) message.channel.send('Mention someone to kick.');
			else {
				member.kick().then(mem => {
					message.channel.send(`Successfully kicked ${mem.user.username}!`);
				});
			}
		} else {
			message.reply(`${erroremoji}You tried!`);
		}
	}

	//ban command
	if (message.content.toLowerCase().startsWith(`${prefix}ban`)) {
		if (message.member.hasPermission('BAN_MEMBERS')) {
			let member = message.mentions.members.first();
			if (!member) message.channel.send('Please mention someone to ban.');
			else {
				member.ban().then(mem => {
					message.channel.send(`Successfully banned ${mem.user.username}!`);
				});
			}
		} else {
			message.reply(`${erroremoji}You tried`);
		}
	}

	//lock command
	if (message.content.toLowerCase() === `${prefix}lock`) {
		if (!client.lockit) client.lockit = [];
		if (!message.member.hasPermission('MANAGE_CHANNELS'))
			return msg.reply(
				`${erroremoji}**Error:** You don't have the permission to do that!`
			);

		message.channel.createOverwrite(message.guild.id, {
			SEND_MESSAGES: false
		});
		message.channel.send(
			`Damnn, **${
				message.author.username
			}** just locked the channel down. Don't worry, Admins will soon open the chat again so be patient.`
		);
	}

	//unlock command
	if (message.content.toLowerCase() === `${prefix}unlock`) {
		if (!client.lockit) client.lockit = [];
		if (!message.member.hasPermission('MANAGE_CHANNELS'))
			return msg.reply(
				`${erroremoji}**Error:** You don't have the permission to do that!`
			);

		message.channel.createOverwrite(message.guild.id, {
			SEND_MESSAGES: true
		});
		message.channel.send(
			`**${message.author.username}**, unlocked the channel!`
		);
	}

	//eval
	if (message.content.toLowerCase().startsWith(`${prefix}eval`)) {
		const notowner = new Discord.MessageEmbed()
			.setDescription('Only the bot owner can use this command')
			.setColor(`${embedcolor}`);
		const owners_id = [`${ownerID}`];
		if (!owners_id.includes(message.author.id))
			return message.channel.send(notowner);
		const args2 = message.content.split(' ').slice(1);

		const clean = text => {
			if (typeof text === 'string')
				return text
					.replace(/`/g, '`' + String.fromCharCode(8203))
					.replace(/@/g, '@' + String.fromCharCode(8203));
			else return text;
		};

		try {
			const code = args2.join(' ');
			let evaled = eval(code);
			const lmao = message.content
				.slice(''.length)
				.trim()
				.split(/ +/);
			lmao
				.shift()
				.toLowerCase()
				.split(' ')[0];
			msg.channel.send(lmao.join(' '));
			const { inspect } = require('util');
			const output = clean(evaled);

			const eval2 = new Discord.MessageEmbed()
				.addField('Input', `\`\`\`js\n${lmao.join(' ')}\`\`\``)
				.addField('Output', `\`\`\`js\n${output}\`\`\``);

			// msg.channel.send(clean(evaled));
			message.channel.send(eval2);
		} catch (err) {
			message.author.send(
				`\`${erroremoji}ERROR${erroremoji}\` \`\`\`xl\n${clean(err)}\n\`\`\``
			);
		}
	}

	//say command
	if (message.content.toLowerCase().startsWith(`${prefix}say`)) {
		const notowner = new Discord.MessageEmbed()
			.setDescription('Only the bot owner can use this command')
			.setColor(`${embedcolor}`);
		const owners_id = [`${ownerID}`];
		if (!owners_id.includes(message.author.id))
			return message.channel.send(notowner);
		message.delete();
		const whattosay = message.content
			.slice(''.length)
			.trim()
			.split(/ +/);
		whattosay
			.shift()
			.toLowerCase()
			.split(' ')[0];
		message.channel.send(whattosay.join(' '));
	}

	//dm command
	if (message.content.toLowerCase().startsWith(`${prefix}dm`)) {
		let member = message.mentions.users.first();
		let content = message.content.split(' ');
		content.shift();
		content = content.join(' ');
		if (!member) return;
		if (!content)
			return message.reply(
				`${erroremoji} | Incorrect Usage | :x: | Correct Usage: \`${prefix}dm <@user> <your text>\``
			);
		else {
			message.delete();
			let embed = new Discord.MessageEmbed()
				.setTitle(
					`New Text Message From ${message.author.username}#${
						message.author.discriminator
					}`
				)
				.setDescription(`${content}`)
				.setFooter(
					`To Send Them A Reply Message, Go To A Mutual Server with this bot and type ${prefix}dm @user <text>`
				)
				.setColor(`${embedcolor}`);
			member.send(embed);
		}
	}

	//serverinfo command
	if (message.content.toLowerCase() === `${prefix}serverinfo`) {
		let embed = new Discord.MessageEmbed()
			.setColor(`${embedcolor}`)
			.setAuthor(
				`Info for ${message.guild}`,
				message.guild.iconURL({ dynamic: true })
			)
			.addField('Owner', message.guild.owner, true)
			.addField('Channels', message.guild.channels.cache.size, true)
			.addField('Roles', message.guild.roles.cache.size, true)
			.addField('Emojis', message.guild.emojis.cache.size, true)
			.addField('Verification Level', message.guild.verificationLevel, true)
			.addField('Region', `${message.guild.region}`, true)
			.addField(
				'Members',
				`Total: ${message.guild.members.cache.size} | Humans: ${
					message.guild.members.cache.filter(member => !member.user.bot).size
				} | Bots: ${
					message.guild.members.cache.filter(member => member.user.bot).size
				}`,
				true
			)
			.setThumbnail(message.guild.iconURL({ dynamic: true }))
			.setFooter(
				`ID: ${
					message.guild.id
				}, Created • ${message.guild.createdAt.toDateString()}`
			);
		message.channel.send(embed);
	}

	//purge command
	if (message.content.toLowerCase().startsWith(`${prefix}purge`)) {
		let arg = message.content.split(' ');
		if (message.member.hasPermission('MANAGE_MESSAGES')) {
			let clear = arg[1];
			if (!clear)
				return message.channel
					.send(`${erroremoji} | \`Incorrect usage of command you need to provide an amount of messages to Clear.\` 
**Example:** \`${prefix}purge 50\` `);
			if (isNaN(clear))
				return message.channel.send(
					`${erroremoji} | Please Put a Valid Number to Clear messages.`
				);
			if (clear > 100)
				return message.channel.send(
					`${erroremoji} | I can't Clear more than 100 messages.`
				);
			if (clear < 1)
				return message.channel.send(
					`${erroremoji} | You cannot Clear less than 1 message.`
				);

			message.channel.bulkDelete(clear);
			message.channel
				.send(
					`${successemoji} | \`Succesfully cleared ${clear} messages! | If purge fails please make sure I have MANAGE_MESSAGES to make the purge successful.\` `
				)
				.then(message => message.delete({ timeout: 2000 }));
		} else {
			message.reply(
				`${erroremoji}Sorry, but sadly you do not have \`MANAGE_MESSAGES\` perm${erroremoji}`
			);
		}
	}

	//sudo command
	if (message.content.toLowerCase().startsWith(`${prefix}sudo`)) {
		if (message.member.hasPermission('MANAGE_MEMBERS')) {
			message.delete();
			let args = message.content.split(' ').slice(1);

			if (!args[1]) return message.reply('Please provide a message to send');
			const member = message.mentions.members.first();
			if (!member) return message.reply('Please tag a user');
			message.channel
				.createWebhook(member.user.username, {
					avatar: member.user.displayAvatarURL({ dynamic: true })
				})
				.then(webhook => {
					webhook.send(args.slice(1).join(' '));
					setTimeout(() => {
						webhook.delete();
					}, 3000);
				});
		} else {
			message.channel.send('You need manage_members');
		}
	}

	//emojistats command
	if (message.content.toLowerCase().startsWith(`${prefix}emojistats`)) {
		const config = [100, 200, 300, 500];
		const emo = config[message.guild.premiumTier];
		const se = `**${
			message.guild.emojis.cache.filter(e => !e.animated).size
		} / ${emo / 2}** (${emo / 2 -
			message.guild.emojis.cache.filter(e => !e.animated).size} left, ${Number(
			(message.guild.emojis.cache.filter(e => !e.animated).size / emo / 2) * 100
		).toFixed(2)}% full)`;
		const ae = `**${
			message.guild.emojis.cache.filter(e => !e.animated).size
		} / ${emo / 2}** (${emo / 2 -
			message.guild.emojis.cache.filter(e => e.animated).size} left, ${Number(
			(message.guild.emojis.cache.filter(e => e.animated).size / emo / 2) * 100
		).toFixed(2)}% full)`;
		const te = `**${message.guild.emojis.cache.size} / ${emo}** (${emo -
			message.guild.emojis.cache.size} left, ${Number(
			(message.guild.emojis.cache.size / emo) * 100
		).toFixed(2)}% full)`;
		const server = message.guild;
		const embed = new Discord.MessageEmbed()
			.setColor(`${embedcolor}`)
			.setTimestamp()
			.setThumbnail(server.iconURL({ dynamic: true }))

			.addField(`Static Emojis:`, se)
			.addField(`Animated Emojis:`, ae)
			.addField(`Total Emojis:`, te);
		message.channel.send(`**EMOJIS STATS**`, embed);
	}

	//whois command
	if (message.content.toLowerCase().startsWith(`${prefix}whois`)) {
		let user = message.mentions.users.first() || message.author;
		let member = message.mentions.members.first() || message.member;
		let e = new Discord.MessageEmbed()
			.setColor(`${embedcolor}`)
			.setTimestamp()
			.addFields(
				{
					name: 'User Joined Server At',
					value: member.joinedAt
				},
				{
					name: 'User Created At',
					value: user.createdAt
				},
				{
					name: 'User Name & Tag',
					value: user.tag
				},
				{
					name: 'User ID',
					value: user.id
				}
			)
			.setThumbnail(user.displayAvatarURL({ dynamic: true }));
		message.channel.send(e);
	}

	//unbancommand
	if (message.content.toLowerCase().startsWith(`${prefix}unban`)) {
		let args = message.content.split(' ').slice(1);
		const id = args[0];
		message.guild.members.unban(id);
		message.channel.send('User unbanned');
	}

	//slowmode command
	if (message.content.toLowerCase().startsWith(`${prefix}slowmode`)) {
		if (message.member.hasPermission('MANAGE_CHANNELS')) {
			let sentence = message.content.split(' ');
			sentence.shift();
			sentence = sentence.join(' ');
			if (sentence != null) {
				message.channel.setRateLimitPerUser(sentence);
			}

			message.reply(`This chat now has a slowmode of ${sentence} seconds!`);
		} else {
			message.reply(`${erroremoji} | You dont have perms for that`);
		}
}

//embed builder command
if(message.content.toLowerCase().startsWith(`${prefix}embed`)) {
  if(message.member.hasPermission(`ADMINISTRATOR`)) {
 let args = message.content.split(' ').splice(1);
 const cmd = args.join(' ').split(' ')
 if(!cmd[0]) return message.channel.send(`${erroremoji} | Wrong! You must provide: \`hex_color title description\``)
 if(!cmd[1]) return message.channel.send(`${erroremoji} | Wrong! You must provide: \`hex_color title description\``)
 if(!cmd[2]) return message.channel.send(`${erroremoji} | Wrong! You must provide: \`hex_color title description\``)

 let emb = new Discord.MessageEmbed()
 .setTitle(cmd[1])
 .setColor(cmd[0])
 .setDescription(cmd[2])
 .setTimestamp()

 message.channel.send(emb)
  }else {
    message.channel.send(`${erroremoji} | You need permission \`ADMINISTRATOR\``)
  }
 }
	//commands stay above this
});


client.login(`${token}`)