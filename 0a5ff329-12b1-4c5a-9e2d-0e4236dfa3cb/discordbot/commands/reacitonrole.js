module.exports = {
    name: 'reactionrole',
    description: "Creates a reaction role message!",
    async execute(message, args, Discord, Client){
        const channel = '928064481039384626';
        const allSerieRole = message.guild.roles.cache.find(role => role.name === "All Serie");
        const HazureSkillGachaRole = message.guild.roles.cache.find(role => role.name === "Hazure Skill “Gacha” de Tsuihou Sareta Ore wa, Wagamama Osananajimi wo Zetsuen Shi Kakusei Suru");
        const KamisamaRole = message.guild.roles.cache.find(role => role.name === "Kamisama ni Kago 2 Nin Bun Moraimashita");
        const AttoutekiRole = message.guild.roles.cache.find(role => role.name === "Attouteki Gacha Un de Isekai wo Nariagaru!");

        const allSerieEmoji = '<:wow:920697316485267456>';
        const HazureSkillGachaEmoji = '<:gacha1:922478423996235826>';
        const KamisamaEmoji = '<:kamisama:922481048082849803>';
        const AttoutekiEmoji = '<:gachaluck:923162600710213642>';


        let embed = new Discord.MessageEmbed()
            .setTitle('Series Role!')
            .setDescription('Reaction to an emoji will allow you to be notified when a new chapter is out!\n\n'
                + `${allSerieEmoji} for All Series \n`
                + `${HazureSkillGachaEmoji} for Hazure Skill “Gacha” de Tsuihou Sareta Ore wa, Wagamama Osananajimi wo Zetsuen Shi Kakusei Suru) \n`
                + `${KamisamaEmoji} for Kamisama ni Kago 2 Nin Bun Moraimashita \n`
                + `${AttoutekiEmoji} for Attouteki Gacha Un de Isekai wo Nariagaru!`);
        ;
        let messageEmbed = await message.channel.send({embeds: [embed]})
        messageEmbed.react(allSerieEmoji)
        messageEmbed.react(HazureSkillGachaEmoji)
        messageEmbed.react(KamisamaEmoji)
        messageEmbed.react(AttoutekiEmoji)




        Client.on('messageReactionAdd', async (reaction, user) => {
            if (reaction.message.partial) await reaction.message.fetch();
            if (reaction.partial) await reaction.fetch();
            if (user.bot) return;
            if (!reaction.message.guild) return;

            if (reaction.message.channel.id == channel) {
                if (reaction.emoji.name === allSerieEmoji) {
                    await reaction.message.guild.members.cache.get(user.id).roles.add(allSerieRole);
                }
                if (reaction.emoji.name === HazureSkillGachaEmoji) {
                    await reaction.message.guild.members.cache.get(user.id).roles.add(HazureSkillGachaRole);
                }
                if (reaction.emoji.name === KamisamaEmoji) {
                    await reaction.message.guild.members.cache.get(user.id).roles.add(KamisamaRole);
                }
                if (reaction.emoji.name === AttoutekiEmoji) {
                        await reaction.message.guild.members.cache.get(user.id).roles.add(AttoutekiRole);
                }
            } else {
                return;
            }

        });

    }

} 