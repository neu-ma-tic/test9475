const Discord = require('discord.js');

const fetch = require('node-fetch');

module.exports = {
    name: "dadjokes",
    description: "sends dad jokes",

     async run(bot, message, args) {
        var user = message.author;
        let status; 
        fetch('https://icanhazdadjoke.com/slack')
        .then((res) => { 
            status = res.status; 
            return res.json()
        })
        .then((dadjoke) => {
            console.log(status);
            console.log(dadjoke);
            const embed = new Discord.MessageEmbed()
            .setColor('#ff4267')
            .setThumbnail('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_GPlHFwbBdLyaBuItx1acqyFM-hyP8-J-68T2TxOJLKMaZ-Z-4aE2EyyitquyR-Clxcg&usqp=CAU')
            .setTitle("here's your dad joke")
            .setDescription(dadjoke['attachments']['0']['text'])
            .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true }));
            message.channel.send(embed);
        });
    }
}