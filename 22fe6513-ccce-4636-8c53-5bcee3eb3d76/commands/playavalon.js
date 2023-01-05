module.exports = {
    name: 'playwolf',
    description: "this command will start the 阿瓦隆",
    async execute(message, Discord, client) {



    }

}

function IntroEmbed(Discord) {
    let embed = new Discord.MessageEmbed()
        .setColor('#474a4b')
        .setTitle('阿瓦隆')
        .setDescription('This is a embed of member to join game\n\n'
            + 'hit the \'🤓 \' for joining the game!\n\nhit the \'🤝 \' to start the game!')
        .setThumbnail('https://i.pinimg.com/736x/5c/a1/42/5ca142d34fd1903773b4f4e6f43d9045.jpg')
        .addFields(
            { name: 'Rule1', value: 'Try Hard' },
            { name: 'Rule2', value: 'Do not unmute youself until you turn' },
        )
        .setImage('https://p2.bahamut.com.tw/B/2KU/10/e076fc69d16fcdc1d1eb3050ba162fq5.JPG')
        .setFooter('Make sure to add a emoji on this embed if you wanna play.');
    return embed;
}