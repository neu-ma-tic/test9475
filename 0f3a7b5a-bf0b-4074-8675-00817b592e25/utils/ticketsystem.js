const firstmessage = require('./firstmessage')
module.exports = async (Discord, client) =>{
    const enmap = require('enmap');

    const prefix = config.BOT_PREFIX
    const ticketsystemsettings = new enmap({
        name: "ticketsystemsettings",
        autoFetch: true,
        cloneLevel: "deep",
        fetchAll: true
    });

    let reactions = [
        '📩'
    ]
    const Embed = new Discord.MessageEmbed()
        .setTitle("MoonLabs Ticket System")
        .setDescription("За да изтеглите билет, реагирайте с 📩")
        .setFooter("Нашата персонализирана система за билети!")
        .setColor("00ff00");

    firstmessage(client, config.TICKET_SYSTEM.supportChannelID, Embed, reactions, ticketsystemsettings)

    client.on('message', async message => {
        if(message.author.bot) return;
        if(message.content.indexOf(prefix) !== 0) return;
    
        const args = message.content.slice(prefix.length).trim().split(/ +/g);
        const command = args.shift().toLowerCase();
    
        if(command == "ticket-setup") {
            // ticket-setup #channel
    
            let channel = message.mentions.channels.first();
            if(!channel) return message.reply(`Usage: \`${prefix}ticket-setup #channel\` `);
    
            let sent = await channel.send(new Discord.MessageEmbed()
                .setTitle("MoonLabs Ticket System")
                .setDescription("За да изтеглите билет, реагирайте с 📩")
                .setFooter("Нашата персонализирана система за билети!")
                .setColor("00ff00")
            );
    
            sent.react('📩');

            ticketsystemsettings.set(`${message.guild.id}-ticket`, sent.id);
    
            message.channel.send("Ticket System Setup Done!")
        }
    
        if(command == "close") {
            if(!message.channel.name.includes("ticket-")) return message.channel.send("You cannot use that here!")
            message.channel.delete();
        }
    });
    
    client.on('messageReactionAdd', async (reaction, user) => {
        if(user.partial) await user.fetch();
        if(reaction.partial) await reaction.fetch();
        if(reaction.message.partial) await reaction.message.fetch();

        // if(reaction.message.guild.channels) await reaction.message.guild.channels.fetch();
    
        if(user.bot) return;
    
        let ticketid = await ticketsystemsettings.get(`${reaction.message.guild.id}-ticket`);
    
        if(!ticketid) return;

        if(reaction.message.id == ticketid && reaction.emoji.name == '📩') {
            reaction.users.remove(user);
            if(reaction.message.guild.channels.cache.some(channel => channel.name.toLowerCase() === 'ticket-' + user.username.toLowerCase())) {
                user.send(`Вече имате отворен билет <#${reaction.message.guild.channels.cache.find(channel => channel.name.toLowerCase() === 'ticket-' + user.username.toLowerCase()).id}>`); // Send user msg indicating they have a ticket.
                return;
            }
            reaction.message.guild.channels.create(`тикет-${user.username}`, {type: "text"}).then(async(chan) => {
                chan.setParent(config.TICKET_SYSTEM.supportCategoryID).then(async channel => {
                    let roles = reaction.message.guild.roles; // collection
                    let everyone = roles.cache.find(role => role.name === "@everyone");
                    let member = roles.cache.get(config.TICKET_SYSTEM.roleMemberId);
                    let support = roles.cache.get(config.TICKET_SYSTEM.roleSupportId);

                    //Only readable for everyone
                    channel.createOverwrite(everyone, {
                        "VIEW_CHANNEL": false,
                        "READ_MESSAGES": false, 
                        "READ_MESSAGE_HISTORY": false 
                    });
                    //OVERWRITE FOR MEMBER
                    channel.createOverwrite(member, {
                        "VIEW_CHANNEL": false,
                        "READ_MESSAGES": false, 
                        "MANAGE_MESSAGES": false,
                        "READ_MESSAGE_HISTORY": false
                    });
                    //OVERWRITE FOR USER
                    channel.createOverwrite(user.id, {
                        "VIEW_CHANNEL": true,
                        "READ_MESSAGES": true,
                        "SEND_MESSAGES": true,
                        "ATTACH_FILES": true,
                        "CREATE_INSTANT_INVITE": false,
                        "ADD_REACTIONS": true,
                        "READ_MESSAGE_HISTORY": true,
                        "EMBED_LINKS": true,
                        "USE_EXTERNAL_EMOJIS": true
                    });
                    //OVERWRITE FOR STAFF THAT HAS SUPPORT ROLE
                    channel.createOverwrite(support, {
                        "VIEW_CHANNEL": true,
                        "READ_MESSAGES": true,
                        "SEND_MESSAGES": true,
                        "ATTACH_FILES": true,
                        "ADD_REACTIONS": true,
                        "READ_MESSAGE_HISTORY": true,
                        "EMBED_LINKS": true,
                        "USE_EXTERNAL_EMOJIS": true
                    });

                    let suppSentMsg = await channel.send(`<@${user.id}> ${support}`, new Discord.MessageEmbed()
                        .setTitle("Добре дошли в билета си!")
                        .setDescription("Отделът за поддръжка ще се свърже с вас скоро. Моля опишете през това време обилно проблема си! За да затворите този билет, реагирайте с 🔒")
                        .setFooter("Нашата персонализирана система за билети!")
                        .setColor("00ff00")
                    ).catch(error => console.error('Failed! ', error));
                    suppSentMsg.react('🔒');
                })
            })
        }

        else if (reaction.emoji.name == '🔒') {
            if(reaction.message.guild.channels.cache.some(channel => channel.name.toLowerCase() === `тикет-${user.username.toLowerCase()}`) || 
            reaction.message.guild.channels.cache.some(channel => channel.name.split('-')[0].toLowerCase() === `тикет`) ||
            reaction.message.guild.channels.cache.some(channel => channel.name.toLowerCase() !== `тикет-тол`)){
                reaction.users.remove(user);
                reaction.message.react('❎');
                reaction.message.react('✅');
            }
        }

        else if (reaction.emoji.name == '❎') {
            reaction.users.remove(user);
            if(reaction.message.guild.channels.cache.some(channel => channel.name.toLowerCase() === `тикет-${user.username.toLowerCase()}`) || 
            reaction.message.guild.channels.cache.some(channel => channel.name.split('-')[0].toLowerCase() === `тикет`)||
            reaction.message.guild.channels.cache.some(channel => channel.name.toLowerCase() !== `тикет-тол`)){
                reaction.message.reactions.cache.get('✅').remove().catch(error => console.error('Failed to remove reactions: ', error));
                reaction.message.reactions.cache.get('❎').remove().catch(error => console.error('Failed to remove reactions: ', error));
            }
        }
        else if (reaction.emoji.name == '✅') {
            if(reaction.message.guild.channels.cache.some(channel => channel.name.toLowerCase() === `тикет-${user.username.toLowerCase()}`) || 
            reaction.message.guild.channels.cache.some(channel => channel.name.split('-')[0].toLowerCase() === `тикет`) ||
            reaction.message.guild.channels.cache.some(channel => channel.name.toLowerCase() !== `тикет-тол`)){
                reaction.users.remove(user);
                await reaction.message.channel.send(new Discord.MessageEmbed()
                    .setTitle("MoonLabs Ticket System")
                    .setDescription(`Билетът е затворен от <@${user.id}>!`)
                    .setFooter("Нашата персонализирана система за билети!")
                    .setColor("ffff00")
                );
    
                let options = await reaction.message.channel.send(new Discord.MessageEmbed()
                    .setDescription("🔓 Отваряне на билета\n⛔ Изтриване на билета")
                    .setFooter("Нашата персонализирана система за билети!")
                    .setColor("ff0000")
                ).catch(error => console.error('Failed! ', error));;;
                options.react('🔓');
                options.react('⛔');

                //Change send message for everyone
                let roles = reaction.message.guild.roles; // collection
                // let everyone = roles.cache.find(role => role.name === "@everyone");
                // let member = roles.cache.get(config.TICKET_SYSTEM.roleMemberId);
                let channel = reaction.message.channel;
                let support = roles.cache.get(config.TICKET_SYSTEM.roleSupportId);
                let usernameChannel = channel.name.split('-')[1].toLowerCase();
                let userId = null
                try {
                    userId = client.users.cache.find(user => user.username.toLowerCase() == usernameChannel).id;
                  }
                  catch (error) {
                    console.log(error);
                }

                if (userId != null) {
                    //OVERWRITE FOR USER
                    channel.createOverwrite(userId, {
                        "VIEW_CHANNEL": true,
                        "READ_MESSAGES": true,
                        "SEND_MESSAGES": false,
                        "ATTACH_FILES": false,
                        "CREATE_INSTANT_INVITE": false,
                        "ADD_REACTIONS": true,
                        "READ_MESSAGE_HISTORY": true,
                        "EMBED_LINKS": false,
                        "USE_EXTERNAL_EMOJIS": false
                    });
                }
                //OVERWRITE FOR STAFF THAT HAS SUPPORT ROLE
                channel.createOverwrite(support, {
                    "VIEW_CHANNEL": true,
                    "READ_MESSAGES": true,
                    "SEND_MESSAGES": false,
                    "ATTACH_FILES": false,
                    "ADD_REACTIONS": true,
                    "READ_MESSAGE_HISTORY": true,
                    "EMBED_LINKS": false,
                    "USE_EXTERNAL_EMOJIS": false
                });


            }           
        }
        else if (reaction.emoji.name == '⛔') {
            if(reaction.message.guild.channels.cache.some(channel => channel.name.toLowerCase() === `тикет-${user.username.toLowerCase()}`) || 
            reaction.message.guild.channels.cache.some(channel => channel.name.split('-')[0].toLowerCase() === `тикет`) ||
            reaction.message.guild.channels.cache.some(channel => channel.name.toLowerCase() !== `тикет-тол`)){
                //Ticket will be closed in 5 seconds
                await reaction.message.channel.send(new Discord.MessageEmbed()
                    .setTitle("MoonLabs Ticket System")
                    .setDescription("Билетът ще бъде затворен след 5 секунди!")
                    .setFooter("Нашата персонализирана система за билети!")
                    .setColor("ff0000")
                );
                setTimeout(() => {
                    reaction.message.channel.delete('closing ticket').catch(err => console.log(err));
                }, 5000);
            }
        }
        else if (reaction.emoji.name == '🔓') {
            if(reaction.message.guild.channels.cache.some(channel => channel.name.toLowerCase() === `тикет-${user.username.toLowerCase()}`) || 
            reaction.message.guild.channels.cache.some(channel => channel.name.split('-')[0].toLowerCase() === `тикет`) ||
            reaction.message.guild.channels.cache.some(channel => channel.name.toLowerCase() !== `тикет-тол`)){
                reaction.message.delete()
                await reaction.message.channel.send(new Discord.MessageEmbed()
                    .setTitle("MoonLabs Ticket System")
                    .setDescription(`Билетът е отворен отново от <@${user.id}>`)
                    .setFooter("Нашата персонализирана система за билети!")
                    .setColor("00ff00")
                );


                //Change send message for everyone
                let roles = reaction.message.guild.roles; // collection
                // let everyone = roles.cache.find(role => role.name === "@everyone");
                // let member = roles.cache.get(config.TICKET_SYSTEM.roleMemberId);
                let channel = reaction.message.channel;
                let support = roles.cache.get(config.TICKET_SYSTEM.roleSupportId);
                let usernameChannel = channel.name.split('-')[1].toLowerCase();
                let userId = null
                try {
                    userId = client.users.cache.find(user => user.username.toLowerCase() == usernameChannel).id;
                  }
                  catch (error) {
                    console.log(error);
                }

                if (userId != null) {                    
                    //OVERWRITE FOR USER
                    channel.createOverwrite(userId, {
                        "VIEW_CHANNEL": true,
                        "READ_MESSAGES": true,
                        "SEND_MESSAGES": true,
                        "ATTACH_FILES": true,
                        "CREATE_INSTANT_INVITE": false,
                        "ADD_REACTIONS": true,
                        "READ_MESSAGE_HISTORY": true,
                        "EMBED_LINKS": true,
                        "USE_EXTERNAL_EMOJIS": true
                    });
                }
                //OVERWRITE FOR STAFF THAT HAS SUPPORT ROLE
                channel.createOverwrite(support, {
                    "VIEW_CHANNEL": true,
                    "READ_MESSAGES": true,
                    "SEND_MESSAGES": true,
                    "ATTACH_FILES": true,
                    "ADD_REACTIONS": true,
                    "READ_MESSAGE_HISTORY": true,
                    "EMBED_LINKS": true,
                    "USE_EXTERNAL_EMOJIS": true
                });


            }
        }
        
    });
}