const Discord = require('discord.js');
const bot = new Discord.Client();
const https = require('https');
const token = 'NTY5NDk0NDQ1MDE2MjE5NjQ5.XLxdEw.iCxed3aFuPMUqL9kCpVExbrGAeo'
const fs = require('fs')
var littlepain

var today = new Date();
var dd = today.getDate();

var mm = today.getMonth()+1; 
var yyyy = today.getFullYear();

today = yyyy+'-'+mm+'-'+dd;


function wormtime() {
    var returnvalue 
    fs.readFile('words.txt', (err, dataaaa) => { 
       if (err) throw err; 
        
        var throwbackkk = JSON.parse(dataaaa.toString());
        var rannum = Math.floor((Math.random() * throwbackkk.data.length));
        
        returnvalue = (throwbackkk.data[rannum].word);
        littlepain = throwbackkk.data[rannum].word
    }) 
    return returnvalue;
}
// 546380862288035880
setInterval(function(){ // Set interval for checking
    var date = new Date(); // Create a Date object to find out what time it is
    if(date.getHours() === 0 && date.getMinutes() === 0){ // Check the time
         runprefunc1 = wormtime()
     setTimeout(function () {
        https.get('https://owlbot.info/api/v2/dictionary/' + littlepain + '?format=json', (resp) => {
            let data = '';
          
            // A chunk of data has been recieved.
            resp.on('data', (chunk) => {
              data += chunk;
            });

            resp.on('end', () => {
                var json = JSON.parse(data)
                if (bot.channels.get("546380862288035880")){
                bot.channels.get("546380862288035880").send({embed: {
                    color: 3447003,
                    author: {
                      name: bot.user.username + " (" + today  + ")",
                      icon_url: bot.user.avatarURL
                    },
                    title: "The Word of the Day for today is:",
                    description: littlepain,
                    fields: [{
                        name: "Type",
                        value: JSON.parse(data)[0].type
                      },
                      {
                        name: "Definition",
                        value: JSON.parse(data)[0].definition
                      },
                      {
                        name: "Example Sentence",
                        value: JSON.parse(data)[0].example
                      }
                    ],
                    timestamp: new Date(),
                    footer: {
                      icon_url: bot.user.avatarURL,
                      text: "Made by Worm"
                    }
                  }
                })
            }
            });
          }).on("error", (err) => {
            console.log("Error!");
          })}, 5000)

        }
    
}, 60000);



runprefunc = wormtime()




bot.on('message', function(message){
    if (message.content.startsWith('!definition')){
        var splitted = message.content.split(" ") 
    var url = 'https://owlbot.info/api/v2/dictionary/' + splitted[1] + '?format=json' 
    https.get(url, (resp) => {
        let data = '';
      
        // A chunk of data has been recieved.
        resp.on('data', (chunk) => {
          data += chunk;
        });
        // The whole response has been received. Print out the result.
        resp.on('end', () => {
            var json = JSON.parse(data)
            
            for(var i = 0; i < json.length; i++) {
                var result = json[i];
                if (JSON.parse(data)[0].definition) {
                    message.channel.send({embed: {
                        color: 3447003,
                        author: {
                          name: bot.user.username,
                          icon_url: bot.user.avatarURL
                        },
                        title: "Word:",
                        description: splitted[1],
                        fields: [{
                            name: "Type",
                            value: result.type
                          },
                          {
                            name: "Definition",
                            value: result.definition
                          },
                          {
                            name: "Example Sentence",
                            value: result.example
                          }
                        ],
                        timestamp: new Date(),
                        footer: {
                          icon_url: bot.user.avatarURL,
                          text: "Made by Worm"
                        }
                      }
                    })
                    }
            }

            
        });
      }).on("error", (err) => {
        console.log("Error!");
      });
    
    }
})
// file:///C:/Users/tllw5/Desktop/languagebot/words.txt
 
  
bot.on('message', function(message){
    if (message.content === ('!wotd')){

        https.get('https://owlbot.info/api/v2/dictionary/' + littlepain + '?format=json', (resp) => {
            let data = '';
          
            // A chunk of data has been recieved.
            resp.on('data', (chunk) => {
              data += chunk;
            });

            resp.on('end', () => {
                var json = JSON.parse(data)
                message.channel.send({embed: {
                    color: 3447003,
                    author: {
                      name: bot.user.username + " (" + today  + ")",
                      icon_url: bot.user.avatarURL
                    },
                    title: "The Word of the Day for today is:",
                    description: littlepain,
                    fields: [{
                        name: "Type",
                        value: JSON.parse(data)[0].type
                      },
                      {
                        name: "Definition",
                        value: JSON.parse(data)[0].definition
                      },
                      {
                        name: "Example Sentence",
                        value: JSON.parse(data)[0].example
                      }
                    ],
                    timestamp: new Date(),
                    footer: {
                      icon_url: bot.user.avatarURL,
                      text: "Made by Worm"
                    }
                  }
                })

            });
          }).on("error", (err) => {
            console.log("Error!");
          });
        }

    }

)


bot.login(token)

bot.on('ready', function() {
console.log('BOT IS ONLINE!')

})