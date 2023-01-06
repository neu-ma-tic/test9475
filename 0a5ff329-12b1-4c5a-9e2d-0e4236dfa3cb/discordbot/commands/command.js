module.exports = {
    name: 'command',
    Description: "Embed !",
    execute(message, args, Discord){
        const newEmbed = new Discord.MessageEmbed()
        .setColor('#000000')
        .setTitle('i am alive')
        .addField (
                {name: 'i am not emotionless', value: 'mr gamer is'}
        )
        .setImage('https://st2.depositphotos.com/1020482/5713/i/950/depositphotos_57131609-stock-photo-human-heart-3d-illustration-isolated.jpg')
        .setFooter('i am going to kill you');

        message.channel.send(newEmbed);
    }


    
}