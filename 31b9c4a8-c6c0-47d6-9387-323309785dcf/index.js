var welcomeChannelID = "716195229849354260";
var staffID = "737331602102943766";
var HighStaffID = "737330872310825022";
var serverID = "737327525365022761";
var memberCountChannel = "731462198731210803";
var bumbChannel = "720231659483431012";
var bumpID = "724976368349216771";
var testRoleID = "723794807260184646";
var boyRoleID = "881163672477663272";
var girlRoleID = "881163961083514900";
var muteRole = "716349942091743283";
var PunishmentsChannelID = "724315458282586144";
var commandChannel = "716207742561550337";
var byeChannelID = "723813375171362856";
var vmuteRole = "726480199209844806"

const discord = require("discord.js");
const client = new discord.Client();
const ms = require("ms");
var levels = [];

for (var i = 1; i < 50; i++) {
  levels.push(i * 50);
}

const canvas = require("canvas");
var db = require("quick.db");

client.login('ODgxMTU5NjEzMTk2Njk3NjAw.YSox1g._em3ibV0VFXZoKexKwi7Nh2fkEQ');

const { createCanvas, loadImage } = require("canvas");
const canvas2 = createCanvas(1600, 570);

client.on("ready", () => {
  console.log(levels);

  console.log("This Bot IsOnline");

  setInterval(function() {
    var status = `${client.users.size} מבברים !help`;

    // db.set("status", `${status}`)
    client.user //join again
      .setActivity(status, {
        type: "WATCHING"
      });
  }, 1800);
});
var timeout = 1000;
  client.on("message", async message => {
	  let args = message.content.toLocaleLowerCase().split(" ");
	  var cmd = args[0];
	  
  if (message.channel.type === "dm") return;

  if(message.content == "בוקר טוב"){
    const good_m = new discord.RichEmbed()
    .setTitle("__Community Bot__")
    .setDescription(`${message.author} , בוקר טוב`)
    .setFooter("Arnon bot", client.user.avatarURL)
     
      .setTimestamp()
    .setColor("BLUE")
    message.channel.send(good_m)
  }
    if(message.content == "לילה טוב"){
    const good_m2 = new discord.RichEmbed()
        .setTitle("__Community Bot__")
.setFooter("Arnon bot", client.user.avatarURL)
     
      .setTimestamp()
    .setDescription(`${message.author} , לילה טוב`)
        .setColor("BLUE")
    message.channel.send(good_m2)
  }
    if(message.content == "ערב טוב"){
    const good_m2 = new discord.RichEmbed()
        .setTitle("__Community Bot__")
.setFooter("Arnon bot", client.user.avatarURL)
     
      .setTimestamp()
    .setDescription(`${message.author} , ערב טוב`)
        .setColor("BLUE")
    message.channel.send(good_m2)
  }
  
      if(message.content ==  "צהריים טובים"){
    const good_m2 = new discord.RichEmbed()
        .setTitle("__Community Bot__")
.setFooter("Arnon bot", client.user.avatarURL)
     
      .setTimestamp()
    .setDescription(`${message.author} , צהריים טובים`)
        .setColor("BLUE")
    message.channel.send(good_m2)
  }

 if (cmd == "!הלפמי" || cmd == "!h") {
    if (message.member.voiceChannel != null) {
      channel = "`" + message.member.voiceChannel.name + "`";
    } else {
      channel = "`📛 המשתמש לא בשום חדר 📛`";
    }

    var reason = "";
    for (var i = 1; i < args.length; i++) {
      reason += " " + args[i];
    }
    if (reason == "") {
      reason = "אין סיבה";
    }

    const h_embed = new discord.RichEmbed()
      .addField("__User:__", message.author + "** | זקוק לעזרתכם **") //סבבה
      .addField("__סיבה__", reason)
      .addField("__חדר__", channel)
      .addField("__Staff__", `<@&${staffID}>`)
      .addField("__ID__", message.author.id)
      //  `<@723876743756251178>, ${message.author} זקוק לעזרתכם! \n חדר: ${channel} \n סיבה: ${reason}`
      // )
      .setFooter("Created by Arnon", client.user.avatarURL)
      .setThumbnail(message.member.user.avatarURL)
      .setTimestamp()
      .setColor("BLUE");

    let delay = await db.fetch(`delay_${message.author.id}`);
    if (delay !== null && 60000 - (Date.now() - delay) > 0) {
      const h_err = new discord.RichEmbed()
        .setDescription("אתה צריך לחכות 60 שניות בשביל להשתמש בפקודה זו שוב!")
        .setColor("RED");
      message.channel.send(h_err).then(msg => {
        msg.delete(8000);
      });
    } else {
      message.channel.send(h_embed);
      message.channel.send("<@&" + staffID + ">");
      await db.set(`delay_${message.author.id}`, Date.now());
    }

    //     if (cmd == "!h" || cmd == "!helpme") {
    //       var channel = message.member.voiceChannel
    //         ? message.member.voiceChannel.name
    //         : " 📛המשתמש לא בשום חדר📛";
    //       message.channel.send(`
    // זקוק לעזרתכם תעזרו לו | ${message.author}
    // חדר: \`${channel}\``);
    //    }
  }
  if (cmd == "!17" || cmd == "!17+") {
    var channel = message.member.voiceChannel
      ? message.member.voiceChannel.name
      : "המשתמש לא בשום חדר";
    message.channel.send(`<@&${staffID}>
רוצה בחינה ל17+  | ${message.author} 
חדר: \`${channel}\``);
  }

  

  if (cmd == "!ping") {
  if (message.channel.id != commandChannel && message.member.id != "512965766862209025") {
    const err_e = new discord.RichEmbed()
        .setDescription(
          `אתה יכול לשלוח את פקודה זו רק בחדר <#${commandChannel}>`
        )
        .setColor("RED");
      message.channel.send(err_e);
      return;
    }
    message.delete();
    let embedioz = new discord.RichEmbed()
      .setTitle(`Pong! 🏓`)
      .addField(`הפינג הוא:`, `\`${Math.round(client.ping)}\` ms `)
      .setColor("BLUE")
      .setThumbnail(
        "https://img2.pngdownload.id/20180320/suq/kisspng-wi-fi-alliance-logo-internet-wifi-modem-icon-5ab0c69c1e7634.5561903815215346201248.jpg"
      );
    message.channel.send(embedioz);
  }

  if (cmd == "!say") { 
    message.delete();
    if (
      message.member.roles.find(udsd => udsd.id === HighStaffID) ||
      message.member.roles.find(udsds => udsds.id === staffID)
    ) {
      message.channel.send(message.content.slice(5));
    } else {
      const not_persms = new discord.RichEmbed()
        .setDescription("אין לך גישות בשביל להשתמש בפקודה זו!")
        .setColor("RED");
      message.channel.send(not_persms).then(msg => {
        msg.delete(3000);
      });
    }
  }
  
  
  if (cmd == "!embed") { 
    message.delete();
    if (
      message.member.roles.find(udsd => udsd.id === HighStaffID) ||
      message.member.roles.find(udsds => udsds.id === staffID)
    ) {
      const say_e = new discord.RichEmbed()
      .setDescription(message.content.slice(8))
      .setColor("BLUE")
      message.channel.send(say_e);
    } else {
      const not_persms = new discord.RichEmbed()
        .setDescription("אין לך גישות בשביל להשתמש בפקודה זו!")
        .setColor("RED");
      message.channel.send(not_persms).then(msg => {
        msg.delete(3000);
      });
    }
  }


  if (cmd == "!userinfo") {
  if (message.channel.id != commandChannel && message.member.id != "512965766862209025") {
    const err_e = new discord.RichEmbed()
        .setDescription(
          `אתה יכול לשלוח את פקודה זו רק בחדר <#${commandChannel}>`
        )
        .setColor("RED");
      message.channel.send(err_e);
      return;
    }
    var mentione = "";
    message.delete();
    if (args[1]) {
      mentione = message.mentions.members.first();
    } else {
      mentione = message.member;
    }
    const joineddiscord =
      "**" +
      (mentione.user.createdAt.getDate() + 1) +
      "/" +
      (mentione.user.createdAt.getMonth() + 1) +
      "/" +
      mentione.user.createdAt.getFullYear() +
      " | " +
      mentione.user.createdAt.getHours() +
      ":" +
      mentione.user.createdAt.getMinutes() +
      ":" +
      mentione.user.createdAt.getSeconds() +
      "**";
    const joinedserver =
      "**" +
      (mentione.joinedAt.getDate() + 1) +
      "/" +
      (mentione.joinedAt.getMonth() + 1) +
      "/" +
      mentione.joinedAt.getFullYear() +
      " | " +
      mentione.joinedAt.getHours() +
      ":" +
      mentione.joinedAt.getMinutes() +
      ":" +
      mentione.joinedAt.getSeconds() +
      "**";
    if (mentione.user.joinedAt == undefined) {
      mentione.user.joinedAt = "לא ידוע";
    }
    if (mentione.presence.status == "Custom Status") {
      mentione.presence.status = "לא משחק";
    }
    if (mentione.presence.status == "Custom Status") {
      mentione.presence.status = "לא משחק";
    }

    if (mentione.presence.status == "dnd") {
      mentione.presence.status = "⛔️ Do Not Disturb";
    }
    if (mentione.nickname == null) {
      mentione.nickname = "אין כינוי";
    }

    var roles = mentione.roles.map(g => `<@&${g.id}>`).join(`,`);
    let embedp = new discord.RichEmbed()
      .setAuthor(
        `${mentione.user.username} Info:`,
        mentione.user.displayAvatarURL
      )
      .addField("**שם השחקן**", ` **${mentione.user.username}**`, true)
      .addField("ID:", `**${mentione.id}**`, true)
      .addField("**כינוי השחקן**", ` **${mentione.nickname}**`, true)
      .addField("סטאטוס:", `**${mentione.presence.status} **`, true)
      .addField(
        "משחק :",
        `🕹️**${mentione.presence.game || "Not Playing"} **`,
        true
      )
      .addField("הרול הגבוה ביותר:", `${mentione.highestRole} `)
      .addField("רולים", "**" + roles + "**")
      .addField("נוצר ב:", `${joineddiscord} `)
      .addField("נכנס לשרת ב", `${joinedserver}`)
      .setColor("BLUE")
      .setFooter("Created by Arnon", client.user.avatarURL)
      .setTimestamp()

      .setThumbnail(mentione.user.displayAvatarURL);
    message.channel.send(embedp);
  }

  //Do not touch who to kick and who not to kick?... so many wtf ink I did not understand do it in hebrew like this one up there ^^^^^^^^^^^^^

  if (cmd == "!commands" || cmd == "!help") {
    if (message.channel.id != commandChannel && message.channel.id != "717336671967903814" && message.member.id != "512965766862209025") {
      const err_e = new discord.RichEmbed()
        .setDescription(
          `אתה יכול לשלוח את פקודה זו רק בחדר <#${commandChannel}>`
        )
        .setColor("RED");
      message.channel.send(err_e);
      return;
    }
    const h_embed = new discord.RichEmbed()
      .setTitle("__פקודות של השרת__")
        .addField("__General Commands__", "`!h`, `!userinfo`")
            .addField("__Staff Commands__", "`!say <message>`, `!embed <message>`")

      .setFooter("Created by Arnon ", client.user.avatarURL)
      .setThumbnail(message.member.user.avatarURL)
      .setTimestamp()
      .setColor("BLUE");
    message.channel.send(h_embed);
  }
    if(message.content == "טופס"){
    const good_m2 = new discord.RichEmbed()
        .setTitle("__Community Bot__")
      .setFooter("Arnon bot", client.user.avatarURL)
     
      .setTimestamp()
    
    .setDescription(`${message.author} ,https://forms.gle/knR97Esj68xm1sHR7 `)
     .setColor("BLUE");
    message.channel.send(good_m2)
      
  }  
});
