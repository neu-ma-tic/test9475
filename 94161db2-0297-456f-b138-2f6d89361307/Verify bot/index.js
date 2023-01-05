const discord = require("discord.js");
const botConfig = require("./botconfig.json");


//  Command handler
const fs = require("fs");

const client = new discord.Client();


//  Command handler
client.commands = new discord.Collection();


client.login(botConfig.token);


//  Command handler
fs.readdir("./commands/", (err, files) => {

    if (err) console.log(err);

    var jsFiles = files.filter(f => f.split(".").pop() === "js");

    if (jsFiles.length <= 0) {
        console.log("Kon geen files vinden");
        return;
    }

    jsFiles.forEach((f, i) => {

        var fileGet = require(`./commands/${f}`);
        console.log(`De file ${f} is geladen`);

        client.commands.set(fileGet.help.name, fileGet);
    });

});


client.on("guildMemberAdd", member => {

    var role = member.guild.roles.cache.get('821331937129791518');

    if (!role) return console.log("geen kijker role ofzo");

    member.roles.add(role);

    var channel = member.guild.channels.cache.get('823595377139122186');

    if (!channel) return console.log("geen welkom channel");

    var message = `Hey ${member}, welkom by **Aiden | YT community** youtube server! \nSelecteer waar je voor wilt genotificeerd worden in` + member.guild.channels.cache.get('825368186496090133').toString();

    channel.send(message).then(async msg => {

        welkomEmoji(msg, ["🇭", "🇴", "🇮"])
    });

});

// client.on("guildMemberRemove", member => {

//     var channel = member.guild.channels.cache.get('821055509419261977');

//     if (!channel) return;

//     channel.send(`Jammer ${member} verliet de server!`);

// });



client.on("ready", async () => {

    console.log(`${client.user.username} kan je nu gebruiken.`);

    client.user.setActivity(",help | Made by MannKiller#9506", { type: "PLAYING" });

    client.setInterval(async() => {
        //leest iedere .. sec mutes.json uit.
        const mutes = JSON.parse(fs.readFileSync("./mutes.json", "utf8"));
        let mustWrite = false;
        for (let i in mutes) {
            let time = mutes[i].time;
            let guildId = mutes[i].guild;
            let guild = client.guilds.cache.find(guild => guild.id === guildId);
            let unmuteperson = guild.members.cache.find(user => user.id == i) || await guild.members.fetch(i);
            let muteTime = mutes[i].leestijd;
            let reason = mutes[i].reason;
            let stafflidGaveMute = mutes[i].stafflid;
            let mutedRole = guild.roles.cache.find(role => role.name === "muted");
            if (!mutedRole) continue;

            if (Date.now() > time) {
                console.log(`${i} heeft geen mute tijd meer.`);

                if (!unmuteperson) {
                    console.log(`${unmuteperson} is niet gevonden.`)
                } else {
                    unmuteperson.roles.remove(mutedRole.id);
                    delete mutes[i];
                    mustWrite = true;
                    var logsChannel = guild.channels.cache.get('854803918727282713');
                    if(!logsChannel) {
                        console.log(logsChannel);
                    } else {

                    var unmuteEmbed = new discord.MessageEmbed()
                    .setColor("GREEN")
                    .setTitle(`**Automatisch Unmute Systeem.**`)
                    .setDescription(`**Geunmuted:** <@${i}> (${i})
                    **Was gemute door:** <@${stafflidGaveMute}> 
                    **Tijd:** ${muteTime}
                    **Reden: ** ${reason}`)
                    .setTimestamp()
                    .setFooter(`${guild.name}, © By MannKiller#9506`);

                    logsChannel.send(unmuteEmbed);
                
                    unmuteperson.send(unmuteEmbed).catch(err => {
                        return message.channel.send(`Ik kan deze gebruiker geen dm sturen!`);
                    });
 
                    // var unmutedtextDM = `**${guild.name}** \n\n **Automatisch Unmute Systeem** \n U was gemuted door: <@${stafflidGaveMute}> \n Reden: ${reason} \n Tijd: ${muteTime}`;

                    // unmuteperson.send(unmutedtextDM).catch(err => {
                    //     return message.channel.send(`Ik kan ${mutePerson} geen dm sturen!`);
                    // });
                    
                    console.log(`Ik heb ${i} zijn mute role weggehaald.`);
                    };
                }


            }

        }
        if (mustWrite) {
            fs.writeFile("./mutes.json", JSON.stringify(mutes), err => {
                if (err) throw (err);
            });
        }
    }, 60000)
});

client.on("message", async message => {

    if (message.author.bot) return;

    if (message.channel.type === "dm") return;

    var prefix = botConfig.prefix;

    var messageArray = message.content.split(" ");

    var command = messageArray[0];

    if (!message.content.startsWith(prefix)) return;

    // command handler
    var args = messageArray.slice(1);

    var commands = client.commands.get(command.slice(prefix.length));

    if (commands) commands.run(client, message, args);

});

async function welkomEmoji(message, reactions) {

    for (const reaction of reactions) {
        await message.react(reaction);
    }

}  


async function promptMessage(message, author, time, reactions) {

    time *= 1000;

    for (const reaction of reactions) {
        await message.react(reaction);
    }

    var filter = (reaction, user) => reactions.includes(reaction.emoji.name) && user.id === author.id;

    return message.awaitReactions(filter, { max: 1, time: time }).then(collected => collected.first() && collected.first().emoji.name);

}