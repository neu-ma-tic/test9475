const Command = require('../../structures/Command');
const { CommandInteraction, CommandInteractionOptionResolver, MessageEmbed, MessageActionRow, MessageButton, MessageSelectMenu } = require('discord.js');
const settings = require('../../assets/settings.json');
const emojis = require('../../assets/emojis.json');

module.exports = class extends Command {
    constructor(client) {
        super(client, {
            name: 'setup',
            description: 'Setup the discord bot',
            category: 'admin',
            cooldown: 2,
            userPermissions: ['ADMINISTRATOR'],
            options: [],
        });
    }
    /**
     * @param {CommandInteraction} interaction
     * @param {CommandInteractionOptionResolver} options
    */
    async run(interaction, options) {
        let verifyChannel = interaction.guild.channels.cache.get(settings.verify_ID);
        let rulesChannel = interaction.guild.channels.cache.get(settings.rules_ID);
        let infoChannel = interaction.guild.channels.cache.get(settings.info_ID);
        let pollsChannel = interaction.guild.channels.cache.get(settings.polls_ID);
        let boostersChannel = interaction.guild.channels.cache.get(settings.boosters_ID);
        let rolesChannel = interaction.guild.channels.cache.get(settings.roles_ID);

        let colorRoles = settings.color_roles;
        let pingRoles = settings.ping_roles;
        let levelRoles = settings.level_roles;
        let regionRoles = settings.region_roles;
        
        if(rolesChannel) {
            let roleMsg = "";

            for(let i = 0; i < colorRoles.length; i++) {
                roleMsg += `${settings.color_roles_emoji[i]} <@&${settings.color_roles[i]}>\n`
            }

            let embed1 = new MessageEmbed()
                .setColor(this.client.colors.maincolor)
                .setImage(settings.rolls_image)

            let embed2 = new MessageEmbed()
                .setColor(this.client.colors.maincolor)
                .setTitle(':art: Color Roles')
                .setDescription(`Click on the menu below to recieve your very own **color role**!\n\n${roleMsg}`)

            const row1 = new MessageActionRow()
                .addComponents(
                    new MessageSelectMenu()
                        .setCustomId('color-roles')
                        .setPlaceholder('Please select a color!')
                        .addOptions([ 
                            colorRoles.map((roleID) => {
                                let role = interaction.guild.roles.cache.get(roleID);
                                let index = colorRoles.indexOf(roleID);
                                return {
                                    label: role.name,
                                    value: role.id,
                                    description: `You will recieve the "${role.name}" role!`,
                                    emoji: settings.color_roles_emoji[index] || null,
                                }
                            })
                        ])
                )
            await rolesChannel.send({ embeds: [embed1, embed2], components: [row1]})

            let roleMsg2 = "";

            for(let i = 0; i < pingRoles.length; i++) {
                roleMsg2 += `${settings.ping_roles_emoji[i]} <@&${settings.ping_roles[i]}>\n`
            }

            let embed3 = new MessageEmbed()
                .setColor(this.client.colors.maincolor)
                .setTitle(':pushpin: Pings')
                .setDescription(`Click on the menu below to select your **ping roles**!\n\n ${roleMsg2}`)

            const row2 = new MessageActionRow()
                .addComponents(
                    new MessageSelectMenu()
                        .setCustomId('discord-pings')
                        .setPlaceholder('Please select a role')
                        .addOptions([ 
                            pingRoles.map((roleID) => {
                                let role = interaction.guild.roles.cache.get(roleID);
                                let index = pingRoles.indexOf(roleID);
                                return {
                                    label: role.name,
                                    value: role.id,
                                    description: `You will recieve the "${role.name}" role!`,
                                    emoji: settings.ping_roles_emoji[index] || null,
                                }

                            })
                        ])
                )
            await rolesChannel.send({ embeds: [embed3], components: [row2]})

            let roleMsg3 = "";

            for(let i = 0; i < levelRoles.length; i++) {
                roleMsg3 += `${settings.level_roles_emoji[i]} <@&${settings.level_roles[i]}>\n`
            }

            let embed4 = new MessageEmbed()
                .setColor(this.client.colors.maincolor)
                .setTitle(':star2: Polygon Ranks')
                .setDescription(`Click on the menu below to select what **rank** you are in polygon!\n\n ${roleMsg3}`)

            const row3 = new MessageActionRow()
                .addComponents(
                    new MessageSelectMenu()
                        .setCustomId('polygon-ranks')
                        .setPlaceholder('Please select a role')
                        .addOptions([ 
                            levelRoles.map((roleID) => {
                                let role = interaction.guild.roles.cache.get(roleID);
                                let index = levelRoles.indexOf(roleID);
                                return {
                                    label: role.name,
                                    value: role.id,
                                    description: `You will recieve the "${role.name}" role!`,
                                    emoji: settings.level_roles_emoji[index] || null,
                                }

                            })
                        ])
                )
            await rolesChannel.send({ embeds: [embed4], components: [row3]})
            
            let roleMsg4 = "";

            for(let i = 0; i < regionRoles.length; i++) {
                roleMsg4 += `${settings.region_roles_emoji[i]} <@&${settings.region_roles[i]}>\n`
            }

            let embed5 = new MessageEmbed()
                .setColor(this.client.colors.maincolor)
                .setTitle(':globe_with_meridians: Region')
                .setDescription(`Click on the menu below to select in what **region** you play polygon!\n\n ${roleMsg4}`)

            const row4 = new MessageActionRow()
                .addComponents(
                    new MessageSelectMenu()
                        .setCustomId('region-roles')
                        .setPlaceholder('Please select a role')
                        .addOptions([ 
                            regionRoles.map((roleID) => {
                                let role = interaction.guild.roles.cache.get(roleID);
                                let index = regionRoles.indexOf(roleID);
                                return {
                                    label: role.name,
                                    value: role.id,
                                    description: `You will recieve the "${role.name}" role!`,
                                    emoji: settings.region_roles_emoji[index] || null,
                                }

                            })
                        ])
                )
            await rolesChannel.send({ embeds: [embed5], components: [row4]})            
        }

        if(boostersChannel){
            let embed1 = new MessageEmbed()
                .setColor(this.client.colors.maincolor)
                .setImage(settings.boosters_image)
            boostersChannel.send({ embeds: [embed1] })
        }

        if(pollsChannel){
            let embed1 = new MessageEmbed()
                .setColor(this.client.colors.maincolor)
                .setImage(settings.polls_image)
            pollsChannel.send({ embeds: [embed1] })
        }

        if(verifyChannel){
            let embed = new MessageEmbed()
                .setColor(this.client.colors.maincolor)
                .setTitle('Verification')
                .addField('How to verify?', 'Please click on the button below to verify yourself!')
                .setImage('https://img.gg.deals/5d/6d/093ef3c336ad32cdc21ebf2dedad47f91fbc_307xt176.jpg')
            const row = new MessageActionRow()
                .addComponents(
                    new MessageButton()
                        .setCustomId('verification')
                        .setEmoji('✅')
                        .setStyle('SECONDARY')
                        .setLabel('Verification')
                )
            verifyChannel.send({ embeds: [embed], components: [row]})
        }

        if(rulesChannel){
            let embed1 = new MessageEmbed()
                 .setColor(this.client.colors.maincolor)
                 .setImage(settings.rules_image)

            let embed2 = new MessageEmbed()
                .setColor(this.client.colors.maincolor)
                .setTitle('Server Rules')
                .setDescription(`
**1. Follow all of the Discord Guidelines and Terms of Service**
> You can view them at the following links:
> - https://discord.com/guidelines
> - https://discord.com/terms
                
**2. No Inappropriate Language**
> The use of profanity should be kept to a minimum. However, any derogatory language towards any user is prohibited.

**3. No spamming**
> Don't send a lot of small messages right after each other. Do not disrupt chat by spamming.

**4. No pornographic/adult/other NSFW material**
> This is a community server and not meant to share this kind of material.

**5. No offensive names and profile pictures**
>  You will be asked to change your name or picture if the staff deems them inappropriate.

**6. Do not advertise**
> Do not post any sort of advertisement unless you have received permission 
> from a server administrator.

**7. Do not act immature in voice channels**
> This includes microphone spamming, playing music through your microphone 
> or intentionally creating loud noises. 
> If you have a high level of background noise, please use push-to-talk.


\`\`\`Your presence in this server implies accepting these rules, including all further changes. These changes might be done at any time without notice, it is your responsibility to check for them.\`\`\``)
            let msg = await rulesChannel.send({ embeds: [embed1, embed2] })

            await msg.react('✅')
        }

        if(infoChannel){
            let embed1 = new MessageEmbed()
                .setColor(this.client.colors.maincolor)
                .setImage(settings.information_image)

            let embed2 = new MessageEmbed()
                .setColor(this.client.colors.maincolor)
                .setTitle(`What is ${interaction.guild.name} About ⁉️`)
                .setDescription(`
> Welcome to ${interaction.guild.name}, This is a gaming community based around the 
> game **Polygon**. Make sure to grab your roles in <#${settings.roles_ID}>. Feel free to chat
> with your fellow polygonners in <#${settings.chat_ID}>. :smile:`)

            let embed3 = new MessageEmbed()
                .setColor(this.client.colors.maincolor)
                .setTitle(`Special Roles`)
                .setDescription(`
${emojis.boost} **<@&${settings.booster_ID}> Booster Role**
> For those who boost this server. By boosting u help us grow as a community and it shows support to us.

${emojis.youtube} **<@&${settings.media_ID}> Media Role**
> For those content creators who upload or stream polygon gameplay. You will be 
> able to share your content with others in <#${settings.videos_ID}> & <#${settings.streams_ID}>

${emojis.star} **<@&${settings.vip_ID}> VIP Role**
> For those who are popular in the Polygon community`)

            let embed4 = new MessageEmbed()
                .setColor(this.client.colors.maincolor)
                .setTitle('Text Channels')
                .setDescription(`
<#${settings.welcome_ID}>
> When a new members joins the server a welcome message gets posted here.

<#${settings.announcements_ID}>
> All the important messages regarding this servers get posted there.

<#${settings.info_ID}>
> All the information relating this server is there.

<#${settings.rules_ID}>
> All the server rules are listed there. Make sure to ready them!

<#${settings.roles_ID}>
> Get your self roles here.

<#${settings.polls_ID}>
> We will be posting polls here regarding polygon and this server.

<#${settings.boosters_ID}>
> If someone boosts this server it will be posted here.

<#${settings.videos_ID}>
> If content creator uploads a polygon video it will be posted here

<#${settings.streams_ID}>
> If a content creator is streaming it will be posted here.
`)

let embed5 = new MessageEmbed()
    .setColor(this.client.colors.maincolor)
    .setTitle('Voice Channels')
    .setDescription(`
<#${settings.discordMembers_ID}>
> This channels shows how many people are currently in this server.

<#${settings.playerCount_ID}>
> This shows the number of players who are playing polygon at the time.`)

let embed6 = new MessageEmbed()
    .setColor(this.client.colors.maincolor)
    .setTitle('Polygon Game')
    .setThumbnail('https://img.gg.deals/5d/6d/093ef3c336ad32cdc21ebf2dedad47f91fbc_307xt176.jpg')
    .setDescription(`
${emojis.steam} **Steam Page**
> https://store.steampowered.com/app/1241100/POLYGON/

${emojis.patreon} **Patreon**
> https://www.patreon.com/redaster_polygon

${emojis.tiktok} **Tiktok**
> https://www.tiktok.com/@polygon.game?lang=en

${emojis.twitter} **Twitter**
> https://twitter.com/RedasterPOLYGON

${emojis.discord} **Discord**
> https://discord.gg/4dfzfja3yv`)

            infoChannel.send({ embeds: [embed1, embed2, embed3, embed4, embed5, embed6] })
        }
        return;
    }
}