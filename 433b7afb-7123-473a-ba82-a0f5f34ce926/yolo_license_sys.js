// Require Max Event Limit \\
require("events").EventEmitter.prototype._maxListeners = 1000;

const Discord = require('discord.js')
const exilied_client = new Discord.Client()
const exilied_config = require('./yolo_config.json');
const { log_discord_exilied_auth_online } = require('./yolo_config.json');
const prefix = exilied_config.prefix;
const snekfetch = require('snekfetch');
const moment = require('moment');
const day = new Date();

var exilied_strtime = require('locutus/php/datetime/strtotime');
var exilied_gmdate = require('locutus/php/datetime/gmdate');

const exilied_bestyfir3tm = exilied_config.ruolo

// CONFIGURAZIONE DATABASE \\
const mysql = require("mysql");
const { rejects } = require('assert-strict');
const { resolve } = require('path-posix');

var exilied_database = mysql.createConnection({
    host: exilied_config.host,
    user: exilied_config.user,
    password: exilied_config.password,
    database: exilied_config.dbname,
    timezone: 'Italy'
});

exilied_database.connect(function(err) {
    if (err) {
        console.error('Errore Di Connessione: ' + err.stack);
        return;
    }

    setInterval(function () {
        exilied_database.query('SELECT 1');
    }, 5000);
})

// CONNECTION BOT \\
exilied_client.on('ready', () => {
    // Console Logs \\
    console.log('[Exilied_Auth] - Started Correctly');
    console.log('[Exilied_Auth] - Dev By Yolo#5921');
    console.log('[Exilied_Auth] - Configuration Loaded')
    console.log(`[Exilied_Auth] - ${exilied_client.user.username} Si È Connesso Al Database: ${exilied_config.dbname}`)
    // Activity \\
    exilied_client.user.setPresence({ activity: { name: exilied_config.activity}, status: "dnd"})
    // Log In Discord \\
    exilied_client.channels.fetch(log_discord_exilied_auth_online)
    .then(channel => {
        const inviamessaggio = new Discord.MessageEmbed()
        .setColor('#0099ff')
        .setTitle('Power Auth - License SyS')
        .setURL('https://discord.gg/CQGCtxeBRd')
        .setAuthor('Yolo#5921', 'https://cdn.discordapp.com/attachments/865187223673765894/906295519423369247/re.png', 'https://discord.gg/CQGCtxeBRd')
        .setDescription('**Is Online And Ready**')
        .setThumbnail('https://cdn.discordapp.com/attachments/865187223673765894/906295519423369247/re.png')
        .addFields(
            { name: `'**Developer**:'`, value: `Yolo#5921` },
            )
        .setImage('https://cdn.discordapp.com/attachments/865187223673765894/906295519423369247/re.png')
        .setTimestamp()
        .setFooter('BOT Maded By Power License Sys', 'https://cdn.discordapp.com/attachments/865187223673765894/906295519423369247/re.png');
        channel.send(inviamessaggio);
    })
});

// Creation Key In Database \\
exilied_client.on('message', async message => {
    if (message.content.startsWith(`${prefix}creakey`)) {
        if(message.guild === null) {
            message.channel.send('**You Don\'t Have Permission For Use This Command**');
            return;
        };
        if(message.member.roles.cache.has(exilied_bestyfir3tm))
        {
            tagpersona = message.author.username;
            var data = new Date();
            automaticoread = message.author;
            function creaid() {
                var base = 'PowerAC-'
                var result = base + '';
                var length = 20
                var chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
                for (var i = length; i > 0; --i) result += chars[Math.floor(Math.random() * chars.length)];
                return result;
            }
            var string = creaid();
            const argomento = message.content.slice(prefix.length).split(/ +/g)
            const comando = argomento.shift().toLowerCase();
            var tempo1 = parseInt((new Date().getTime() / 1000).toFixed(0))
            var tempo = argomento[0];
            Boolean;
            tempoetag = true;
            let persona = message.guild.member(message.mentions.users.first() || message.guild.members.fetch(argomento[1]))

            if(tempo == undefined)return message.reply("**Need To Insert Time, Use: https://toolset.mrw.it/dev/timestamp.html **");

            if(persona == undefined)return message.reply("**Need To Tag A Player, Example: @BestyFir3TM**");

            if(tempoetag) 
            {
                message.reply("**Key Generated Is**: " + string + "\n **Date Generation**: " + message.createdAt.toLocaleDateString())
                persona.send("**Your Key Is**: " + string + "\n**The Key Duration Is**: **" + argomento[0] + "**" + " **Days**")
                function creaipdinamico() {
                    var resultip = '';
                    var length = 20
                    var chars = '0123456789';
                    for (var i = length; i > 0; --i) resultip += chars[Math.floor(Math.random() * chars.length)];
                    exilied_database.query(`INSERT INTO licenses (license, created_by, total_time, created, used, ip, userid) VALUES ('${string}', '${tagpersona}', '${tempo}', '${tempo1}', '${tempo1}', '${resultip}', '${persona}')`);
                }
                var string = creaipdinamico()       
            }
        }
        else {
            message.channel.send("Access Denied");
        }
    }
})

// Set IP \\
exilied_client.on('message', async message => {
    if (message.content.startsWith(`${prefix}setip`)) {
        const argomento = message.content.slice(prefix.length).split(/ +/g)
        const commando = argomento.shift().toLowerCase();

        if (argomento[0] == undefined)return message.reply("You Need To Insert A License Key")
        if (argomento[1] == undefined)return message.reply("You Need To Insert An IP")

        exilied_database.query(`UPDATE licenses SET ip = '${argomento[1]}' WHERE license = '${argomento[0]}'`)
        message.reply(`**The License**: ${argomento[0]} \n**Has Been Set On IP**: ${argomento[1]}`)
    }
}); 

// Time \\
exilied_client.on('message', async message => {
    if (message.content.startsWith(`${prefix}time`)) {
        automex = message.author;
        if(message.guild == undefined) {
            message.reply("YOU CAN'T USE THIS COMMAND...");
            return;
        };
        if(message.member.roles.cache.has(exilied_bestyfir3tm)) {
            const argomento = message.content.slice(prefix.length).split(/ +/g)
            const comando = argomento.shift().toLowerCase();
            var i = 1;
            if(argomento[0])
            {
                if(message.member.roles.cache.has(exilied_bestyfir3tm))
                {
                    var exilied_diocan = message.guild.member(message.mentions.users.first() || message.guild.members.fetch(argomento[1]))
                } else {
                    message.delete()
                    message.reply(automex.username + "  What u doing?? bruh")
                    return;
                }

            } else {
                var exilied_diocan = automex
            }
            
            const QueryGrossa = `SELECT license, used, total_time FROM licenses WHERE userid = '${exilied_diocan.id}';`
            const autoreasd = querytxt => {
                return new Promise((resolve, reject) => {
                    exilied_database.query(querytxt, (err, results, fields) => {
                        if (err) reject(err);
                        resolve([results, fields]);
                    });
                });
            }; 
            
            const [results, fields] = await autoreasd(QueryGrossa);
            const Mappa1 = results.map(results => `${(results.used)}`);
            const Mappa2 = results.map(results => `${(results.total_time)}`);
            var TempoAttesa = parseInt (Mappa1, 10);
            var TempoAttesa2 = parseInt (Mappa2, 10);
            function ConversioneTempo(UNIX_timestamp){
                var exilied_time = new Date(UNIX_timestamp * 1000);
                var mesi = ['January','February','March','April','May','June','July','August','September','October','November','December'];
                exilied_time.setDate(exilied_time.getDate() + TempoAttesa2);
                var year = exilied_time.getFullYear();
                var month = mesi[exilied_time.getMonth()];
                var date = exilied_time.getDate();
                var hour = exilied_time.getHours();
                var min = exilied_time.getMinutes();
                var sec = exilied_time.getSeconds();
                var time = date + ' ' + month + ' ' + year + ' ' + hour + ":"+  min;
                return time;
            } 
            message.delete()
            var convert =  ConversioneTempo(TempoAttesa)
            var exilied_manda = automex.send("**Your License Key Expired On**: \n" +  "**" + convert + "** \n If Not See Date Your Key Is Expired**")
            } else {
                automex.send("**You Dont Have A License Key**")
            }
        }
});

// Delete License \\
exilied_client.on('message', async message => {
    if (message.content.startsWith(`${prefix}delkey`)) {
        if(message.guild == undefined) {
            message.reply('You Can\'t Use This Command');
            return;
        };
        if(message.member.roles.cache.has(exilied_bestyfir3tm)) 
        {
            const argomento = message.content.slice(prefix.length).split(/ +/g)
            const comando = argomento.shift().toLowerCase();
            var chiave = argomento.join(' ')
            if(argomento[0] == undefined)return message.reply("You Need An Insert A License Key")
            exilied_database.query(`DELETE FROM licenses WHERE license = '${argomento[0]}'`)
            message.reply("**The License Key**: "+ chiave +" **Has Been Deleted**") 
        } else {
            message.reply('Access Denied');
        }
    }
});

// Costante Lettura Cartelle \\
const fs = require('fs')

// List Key \\
exilied_client.on('message', async message => {
    if (message.content.startsWith(`${prefix}listkey`)) {
        if(message.guild == undefined) {
            message.reply("**YOU CAN'T USE THIS COMMAND");
            return;
        };
        if(message.member.roles.cache.has(exilied_bestyfir3tm))
        {
            var i = 1;
            const QueryLista = `SELECT * FROM licenses;`
            const autoreasd = querytxt => {
                return new Promise((resolve, reject) => {
                    exilied_database.query(querytxt, (err, results, fields) => {
                        if (err) rejects(err);
                        resolve([results, fields]);
                    });
                });
            };
            const [results, fields] = await autoreasd(QueryLista);
            const Mappa1 = results.map(results => ` **{License Number**: **${(i++)}}** \n\n **License Key:** ${(results.license)} \n **Created by** ${(results.created_by)} \n **Created For:** ${('@',results.userid)} \n **IP Set**: ${(results.ip)} \n **Duration Days**: ${(results.total_time)} \n`)
            message.channel.send(Mappa1)
        } else {
            message.reply("Access Denied");
        }
    }
});

// Check Key With Discord ID \\
exilied_client.on('message', async message => {
    if (message.content.startsWith(`${prefix}checkkey`)) {
        if(message.guild == undefined) {
            message.reply("**YOU CAN'T USER THIS COMMAND**");
            return;
        };
        if(message.member.roles.cache.has(exilied_bestyfir3tm))
        {
            const argomento = message.content.slice(prefix.length).split(/ +/g)
            const comando = argomento.shift().toLowerCase();
            var id = argomento.join(' ')
            if(argomento[0] == undefined)return message.reply("You Need Insert Discord ID")
            const QueryCheck = `SELECT * FROM licenses WHERE userid = '${argomento[0]}'`
            const autoreasd = querytxt => {
                return new Promise((resolve, reject) => {
                    exilied_database.query(querytxt, (err, results, fields) => {
                        if (err) rejects(err);
                        resolve([results, fields]);
                    });
                });
            };
            const [results, fields] = await autoreasd(QueryCheck);
            if (results == '') return message.reply('This User ID '+ argomento[0] +' Doesn\'t Have A License Key In Database')
            const MessaggioCheck = results.map(results => `**The License Key**: \n ${results.license} \n **Discord ID**: ${results.userid} \n **IP**: ${results.ip} \n **Duration Key**: ${results.total_time} **Days** \n **This License Is Setted At Discord ID**: '${argomento[0]}'`)
            message.delete()
            message.reply(MessaggioCheck)
        } else {
            message.reply("Access Denied")
        }
    }
})

exilied_client.login(exilied_config.token)