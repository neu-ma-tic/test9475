dvar commando = require('discord.js-commando');
var discord = require('discord.js');

class aboutuser extends commando.Command 
{
    constructor(client) {
        super(client, {
            name: 'aboutuser',
            group: 'help',
            memberName: 'aboutuser',
            description: 'Lists information about a specific user.',
            aliases: ['au', 'aboutu', 'auser', 'user'],
        })
    }
async run(message, args){
    const userMention = message.mentions.users.first() || msg.author;
    const memberMention = message.mentions.members.first() || msg.member;

    let userinfo = {};
    userinfo.bot = userMention.bot;
    userinfo.createdat = userMention.createdAt;
    userinfo.discrim = userMention.discriminator;
    userinfo.id = userMention.id;
    userinfo.mfa = userMention.mfaEnabled;
    userinfo.pre = userMention.premium;
    userinfo.presen = userMention.presence;
    userinfo.tag = userMention.tag;
    userinfo.uname = userMention.username;
    userinfo.verified = userMention.verified;

    userinfo.avatar = userMention.avatarURL;

    const rolesOfTheMember = memberMention.roles.filter(r => r.name !== '@everyone').map(role => role.name).join(', ')

    var myInfo = new discord.RichEmbed()
        .setAuthor(userinfo.uname, userinfo.avatar)
        .addField("Bot?",userinfo.bot, true)
        .addField("Created At",userinfo.createdat, true)
        .addField("Discriminator",userinfo.discrim, true)
        .addField("Client ID",userinfo.id, true)
        .addField("2FA/MFA Enabled?",userinfo.mfa, true)
        .addField("Paid Account?",userinfo.pre, true)
        .addField("Presence",userinfo.presen, true)
        .addField("Client Tag",userinfo.tag, true)
        .addField("Username",userinfo.uname, true)
        .addField("Verified?",userinfo.verified, true)
        .setColor(0xf0e5da)
        .setFooter('s!aboutserver')
        .setTitle("About this user...")
        .setThumbnail(userinfo.avatar)


        message.channel.sendEmbed(myInfo);

}

}
module.exports = aboutuser;