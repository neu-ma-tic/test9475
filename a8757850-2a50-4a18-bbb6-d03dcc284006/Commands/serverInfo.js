const Command = require("../Structres/Command.js");
const { Permissions, Message, MessageEmbed } = require('discord.js');
const Discord = require('discord.js');

module.exports = new Command({
    name: 'serverinfo',
    description: '顯示伺服器資訊',
    aliases: ["si"],
    permission: "SEND_MESSAGES",


    async run(message, args, client) {
        const vanityCode = message.guild.vanityURLCode;
        let vanityInvite = `https://discord.gg/${vanityCode}`;
        if (vanityCode === null) vanityInvite = '沒有自訂邀請連結';
        const roles = message.guild.roles.cache.filter(r => r.id !== message.guild.id).map(role => role.toString());
        const embed = new MessageEmbed()         
            .setColor('LUMINOUS_VIVID_PINK')
            .setTitle('✧✧✧伺服器資訊✧✧✧')      
            .setThumbnail(message.guild.iconURL({
                dynamic: true
            }))
           
            .addField('➤伺服器名稱', message.guild.name)
            .addField('➤伺服器ID', message.guild.id)
            .addField('➤擁有者', `${(await message.guild.fetchOwner()).user}`)
            .addField('➤成員數量', message.guild.memberCount.toString())
            .addField('➤機器人數量', message.guild.members.cache.filter(member => member.user.bot).size.toString())
            .addField('➤伺服器表情符號', message.guild.emojis.cache.size.toString())
            .addField('➤伺服器動圖', message.guild.emojis.cache.filter(emoji => emoji.animated).size.toString())
            .addField('➤文字頻道數量', message.guild.channels.cache.filter(channel => channel.type === 'GUILD_TEXT').size.toString())
            .addField('➤語音頻道數量', message.guild.channels.cache.filter(channel => channel.type === 'GUILD_VOICE').size.toString())
            .addField('➤自訂邀請連結', `${vanityInvite}`)
            .addField('➤伺服器加成等級', message.guild.premiumTier.toString())
            .addField('➤伺服器加成數量', message.guild.premiumSubscriptionCount.toString())
            .addField('➤管理驗證等級', message.guild.verificationLevel.toString())
            .addField(`➤身分組 [${roles.length}]`, roles.length < 15 ? roles.join(' | ') : roles.length > 15
                ? `${roles.slice(0, 15).join(' | ')} | \`+ ${roles.length - 15} ...\`` : 'None')
            /*如果身分組數量<15 則每個身分組會用 | 隔開 ，
            如果>15則會|隔開以及以 身分組長度-15 表示剩下的
            例如有伺服器20個身分組則顯示前15個 剩下則用 +5...表示*/
          

        message.reply({ embeds: [embed] });
    }
})