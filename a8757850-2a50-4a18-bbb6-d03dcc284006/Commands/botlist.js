const Command = require("../Structres/Command.js");
const Discord = require("discord.js")
const paginationEmbed = require('discordjs-button-pagination');

module.exports = new Command({
    name: "botlist",
    description: "列出伺服器機器人數量",
    aliases:["bl"],
    permission: "SEND_MESSAGES",
    async run(message, args, client) {

    const pEmbed = new Discord.MessageEmbed()
      .setColor('#a8f1ff')
      .setDescription(`**尋找這個伺服器的機器人** <a:neo_loading:877035130076659762>`)
      .setFooter('這可能會花點時間')
      const m = await message.reply({embeds: [pEmbed]})

            let Bots = []
            let embed = {}
            let embedslist = []
            message.guild.members.cache.filter(m=>m.user.bot).map(m=> {
              Bots.push(`<@${m.id}> [ ${m.user.username} ]\n**ID :** \`${m.id}\``)})
            var i,j, temporary, chunk = 8;
              for (i = 0,j = Bots.length; i < j; i += chunk) {
                  temporary = Bots.slice(i, i + chunk);
                  embed[`${i/8}`] = new Discord.MessageEmbed()
                  .setAuthor(`Bots in ${message.guild.name}`, `${message.guild.iconURL({dynamic: true})}`)
                  .setDescription(`總共機器人 - \`[${Bots.length}]\`\n\━\━\━\━\━\━\━\━\━\━\━\━\━\━\━\━\━\━\n${temporary.join(`\n\━\━\━\━\━\━\━\━\━\━\━\━\━\━\━\━\━\━\n`)}`)
                  .setColor('#a8f1ff')
              }
              for (let i = 0; i < (Object.keys(embed).length); i++) {
                embedslist.push(embed[i])
              }
              const button1 = new Discord.MessageButton()
              .setCustomId('previousbtn')
              .setEmoji('<:neox_leftarrow:877767124544782368>')
              .setStyle('SECONDARY');
           
              const button2 = new Discord.MessageButton()
              .setCustomId('nextbtn')
              .setEmoji('<:neox_rightarrow:877765155230994482>')
              .setStyle('SECONDARY');
              buttonList = [
                button1,
                button2
            ]
        if (embedslist.length<1) return message.channel.send('沒有機器人在這個群組')
              paginationEmbed(message, embedslist, buttonList);
      m.delete()
          
  }
})