const { MessageEmbed } = require('discord.js');

module.exports = {
    // create embed
    createEmbed({ member }) {
        const welcomEmbed = new MessageEmbed()
            .setAuthor(`${member.user.tag} joined!`)
            .setDescription("Welcome to Root!\n/insert <학번_이름> <트랙명>으로 정보를 입력해주세요.")
            .setColor("#eecbff");
        return welcomEmbed;
    }
};