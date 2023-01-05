const Discord = require('discord.js');

const DiscordPages = require("discord-pages");

module.exports = {
    name: "help",
    description: "sends help",

     async run(bot, message, args) {
            var user = message.author;
            const embed1 = new Discord.MessageEmbed()
            .setColor('#ff4267')
            .setTitle('Command List (Page - 1)')
            .setThumbnail('https://static.vecteezy.com/system/resources/previews/002/363/142/original/logic-icon-free-vector.jpg')
            .addFields(
                { name: '1) Weather' ,  value:  "+weather"                      },
                { name: '2) Dad Jokes'  ,  value:  "+dadjokes "                 }, 
                { name: '3) Memes'  ,  value:  "+meme "                         }, 
                { name: '4) GIF'  ,  value:  "+gifhelp"                         },
                { name: '5) Cute Dog Pictures'  ,  value:  "+doggo "            },
                { name: '6) Cute Shiba Inu Pictures'  ,  value:  "+shiba"       },
                { name: '7) Cute Cat Pictures'  ,  value:  "+catto "            },
                { name: '8) Display Picture'  ,  value:  "+dp"                  },
                { name: '9) Random Number Generator'  ,  value:  "+randnum"     },
                { name: '10) Tic-Tac-Toe'  ,  value:  "+ttt/+tictactoe "        }, 
                { name: '11) Snake Game'  ,  value:  "+snake"                   },
                { name: '12) Rock-Paper-Scissors'  ,  value:  "+rps"            },
                { name: '13) Hello'  ,  value:  "+hello"                        },
                { name: '14) Fight'  ,  value:  "+fight"                        },
                { name: '15) Fast-Type'  ,  value:  "+fstype"                   },
                { name: '16) Text Flip'  ,  value:  "+tf"                       },
                { name: '17) Calculator'  ,  value:  "+calc"                    },
                { name: '18) Sentence Reverse'  ,  value:  "+senrev"            },
                { name: '19) Affirmation'  ,  value:  "+aff "                   }, 
                { name: '20) Level'  ,  value:  "+lvl "                         }, 
                { name: '21) Leaderboard'  ,  value:  "+lb"                     }, 
                { name: '22) Encrypt Messages'  ,  value:  "+encrypt"           }, 
                { name: '23) Decrypt Messages'  ,  value:  "+decrypt"           }
            )
            
            const embed2 = new Discord.MessageEmbed()
            .setColor('#ff4267')
            .setTitle('Command List')
            .setThumbnail('https://static.vecteezy.com/system/resources/previews/002/363/142/original/logic-icon-free-vector.jpg')
            .addFields(
                { name: '24) Random Facts', value: "+rf"                        },
                { name: '25) Random Picture', value: "+randpic"                 },
                { name: '26) Picture Search', value: "+picsearch"               },
                { name: '27) Send Message', value: "+sendmsg"                   },
                { name: '28) Word Meaning', value: "+meaning"                   },
                { name: '29) YT Channel Information', value: "+ytinfo"          },
                { name: '30) Server Information', value: "+serverinfo"          },
            )

            const pages = [embed1, embed2];

            const embedPages = new DiscordPages
            ({ 
                pages: pages, 
                channel: message.channel, 
            });
    
            embedPages.createPages();
    }
}