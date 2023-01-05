//Read The Bottom
const discord = require('discord.js')
const fetch = require("node-fetch")
 const { MessageActionRow, MessageButton } = require('discord.js');
module.exports = {
    name: "findemoji",
    aliases: ["finde", "fe"],
    description: "Steals Emoji from Other Servers to ur Server.",
    authorPermission: ["MANAGE_EMOJIS"],
 
    run: async (client, message, args) => {
      
let emojis = await fetch("https://emoji.gg/api/").then(res => res.json());
     const q = args.join(" ").toLowerCase().trim().split(" ").join("_");
     let matches = emojis.filter(s => s.title == q || s.title.includes(q));
     
     let noResult = new discord.MessageEmbed()
        .setDescription(`:x: |No Results found for ${args.join(" ")}!`)
        .setColor("FF2052")
     
     if (!matches.length) return message.reply({embeds:[noResult]})
     let page = 0;
     let embed = new discord.MessageEmbed()
     .setTitle(matches[page].title)
     .setURL("https://discordemoji.com/emoji/" + matches[page].slug)
     .setColor("00FFFF")
     .setImage(matches[page].image)
     .setFooter(`Emoji ${page + 1}/${matches.length}`);
     let row = new MessageActionRow()
			.addComponents(
				new MessageButton()
					.setCustomId('previous')
					.setLabel('Previous')
					.setEmoji('◀️')
					.setStyle('PRIMARY'),
				new MessageButton()
					.setCustomId('next')
					.setLabel('Next')
					.setEmoji('▶️')
					.setStyle('PRIMARY'),
				new MessageButton()
					.setCustomId('add')
					.setLabel('Add')
					.setEmoji('✅')
					.setStyle('SUCCESS'),
				new MessageButton()
					.setCustomId('cancel')
					.setLabel('Cancel')
					.setEmoji('❌')
					.setStyle('DANGER'),
			);
     const msg = await message.reply({embeds:[embed],components: [row]});
     //emojis = ["◀️", "▶️", "✅", "❌"]
     const filter = (button) => button.user.id === message.author.id && button.message.id === msg.id && button.isButton();
 
     let collector = msg.createMessageComponentCollector({time: 120000,filter: filter})
     collector.on('collect', async (b) => {
		switch(b.customId) {
			case "previous":
			page--;
		if(!matches[page]) {
          page++;
        } else {
        	let newembed = new discord.MessageEmbed()
     .setTitle(matches[page].title)
     .setURL("https://discordemoji.com/emoji/" + matches[page].slug)
     .setColor("00FFFF")
     .setImage(matches[page].image)
     .setFooter(`Emoji ${page + 1}/${matches.length}`);
     msg.edit({embeds:[newembed],components: [row]});
           }
           break;
         case "next":
           page++;
     if(!matches[page]) page--;
     else msg.edit({embeds:[new discord.MessageEmbed()
     .setTitle(matches[page].title)
     .setURL("https://discordemoji.com/emoji/" + matches[page].slug)
     .setColor("00FFFF")
     .setImage(matches[page].image)
     .setFooter(`Emoji ${page + 1}/${matches.length}`)],components:[row]})
           break;
         case "add":
           collector.stop()
           const res = matches[page];
        let created;
        message.channel.sendTyping()
        try { 
        created = await message.guild.emojis.create(res.image, res.title);
        //message.channel.stopTyping();
        message.channel.send(`Successfully added ${created}!`);
       } catch(error) {
      console.log(error) //message.channel.stopTyping();
      message.channel.send(`Unable to add ${res.title}.`);
       }
           break;
         case "cancel":
           collector.stop()
           b.reply("Cancelled Command.")
           break;
     }
     });
    }
}
//Ok,So There Was A Code Already But It Uses Reactions And v12 But This One Is For V13 And Uses Buttons Also I Coded It In Phone It Took 3 Days So If It Works Ping Me At General And Tell Me If It Works Or Not
