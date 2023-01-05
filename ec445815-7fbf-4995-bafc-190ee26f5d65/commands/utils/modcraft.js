const { MessageEmbed } = require('discord.js');
const mcping = require('mcping-js')
const server = new mcping.MinecraftServer('v1.modcraftmc.fr', 25565)

module.exports = {
    name: 'modcraft',
    category: 'info',
    description: 'get modcraft stats',
    aliases: [`modcraftmc`, `serveur`, `info`, `infos`, `launcher`, `jouer`],
    run: async (bot, message, args, config) => {

        server.ping(120, 340, (err, res) => {

            if (err) {
                console.log(err);
                return;
            };


            const embed = new MessageEmbed()
                .setTitle(`ModcraftMC V2.5`)
                .setDescription(`Télécharge le launcher et rejoins-nous !`)
                .addField(`Launcher`, `https://modcraftmc.fr/`)
                .addField(`Connectés`, `${res.players.online} sur ${res.players.max} joueurs`)
                .addField(`Discussion`, `Discute avec les joueurs connecté ici <#696878561075789834>`)
                .setFooter(config.footer)
                .setThumbnail(message.author.displayAvatarURL())
                .setColor(`FFA500`);

            message.channel.send(embed).then(msg => {
                msg.react(`❌`);

                const filter = (reaction, user) => reaction.emoji.name === '❌' && !user.bot

                const collector = msg.createReactionCollector(filter);
                collector.on('collect', () => msg.delete());

            });

            message.delete();

        });
    }

}