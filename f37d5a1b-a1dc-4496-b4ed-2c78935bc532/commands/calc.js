const Discord = require('discord.js');

const { MessageButton, MessageActionRow, ButtonCollector } = require('discord-buttons');

var row1;
var row2;
var row3;
var row4;
var row5;

var calcEmbed;

module.exports = {
    name: "calc",
    description: "calculates",

    async run(bot, message, args) { 
        let user = message.author;
        let stringify = " "

        row1 = new MessageActionRow().addComponents(
               new MessageButton().setID('clear').setLabel('C').setStyle('red').setDisabled(false),
		       new MessageButton().setID('2.71828182846').setLabel('e').setStyle('blurple').setDisabled(false),
		       new MessageButton().setID('3.14159265359').setLabel('π').setStyle('blurple').setDisabled(false),
		       new MessageButton().setID('**').setLabel('^').setStyle('blurple').setDisabled(false)
        );
        row2 = new MessageActionRow().addComponents(
               new MessageButton().setID('7').setLabel('7').setStyle('gray').setDisabled(false),
		       new MessageButton().setID('8').setLabel('8').setStyle('gray').setDisabled(false),
		       new MessageButton().setID('9').setLabel('9').setStyle('gray').setDisabled(false),
		       new MessageButton().setID('/').setLabel('/').setStyle('blurple').setDisabled(false)
        );
        row3 = new MessageActionRow().addComponents(
               new MessageButton().setID('4').setLabel('4').setStyle('gray').setDisabled(false),
		       new MessageButton().setID('5').setLabel('5').setStyle('gray').setDisabled(false),
		       new MessageButton().setID('6').setLabel('6').setStyle('gray').setDisabled(false),
		       new MessageButton().setID('*').setLabel('*').setStyle('blurple').setDisabled(false)
        );
        row4 = new MessageActionRow().addComponents(
               new MessageButton().setID('1').setLabel('1').setStyle('gray').setDisabled(false),
		       new MessageButton().setID('2').setLabel('2').setStyle('gray').setDisabled(false),
		       new MessageButton().setID('3').setLabel('3').setStyle('gray').setDisabled(false),
		       new MessageButton().setID('-').setLabel('-').setStyle('blurple').setDisabled(false)
        );
        row5 = new MessageActionRow().addComponents(
               new MessageButton().setID('0').setLabel('0').setStyle('gray').setDisabled(false),
		       new MessageButton().setID('.').setLabel('.').setStyle('gray').setDisabled(false),
		       new MessageButton().setID('=').setLabel('=').setStyle('green').setDisabled(false),
		       new MessageButton().setID('+').setLabel('+').setStyle('blurple').setDisabled(false)
        );

        calcEmbed = new Discord.MessageEmbed()
        .setColor('#ff4267')
        .setThumbnail('https://image.freepik.com/free-vector/calculator-math-isolated-icon_24877-8718.jpg')
        .setDescription('```Blank```')
        .setTitle('Here is your Calculator! ')
        .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true }));

        const filter = m => m.clicker.user.id === message.author.id;

        message.channel.send({
            embed: calcEmbed,
            components: [row1, row2, row3, row4, row5] 
        })
        .then(async (msg) => {
            
            const calc = msg.createButtonCollector(filter);

            calc.on('collect', async btn => {
                if (btn.clicker.user.id !== message.author.id) {
                    return btn.defer();
                }
                btn.defer()
                switch (btn.id){
                    case '7': 
                    case '8': 
                    case '9':
                    case '4': 
                    case '5': 
                    case '6': 
                    case '1': 
                    case '2': 
                    case '3': 
                    case '0': 
                    case '+': 
                    case '-': 
                    case '*':
                    case '**':
                    case '2.71828182846':
                    case '3.14159265359':
                    case '/': 
                    case '.': stringify += btn.id;
                              break; 

                    case 'clear': stringify = ' ';
                                    break;

                    case '=': if(stringify != ' ')
                                stringify = eval(stringify);
                                    btn.message.edit({
                                        embed: calcEmbed = new Discord.MessageEmbed()
                                                .setColor('#ff4267')
                                                .setThumbnail('https://image.freepik.com/free-vector/calculator-math-isolated-icon_24877-8718.jpg')
                                                .setDescription('```' + stringify + '```')
                                                .setTitle('The Calculator Has Expired!')
                                                .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true })),   
                                    })
                };
                
                if((btn.message.editable) && (btn.id != '=')){
                    btn.message.edit({
                        embed: calcEmbed = new Discord.MessageEmbed()
                                .setColor('#ff4267')
                                .setThumbnail('https://image.freepik.com/free-vector/calculator-math-isolated-icon_24877-8718.jpg')
                                .setDescription('```' + stringify + '```')
                                .setTitle('Here is your Calculator! ')
                                .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true })),
                        components: [row1, row2, row3, row4, row5]
                    })
                }
            })
        })
    }
}