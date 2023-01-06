const { Client, MessageEmbed, DiscordAPIError, PermissionOverwrites  } = require("discord.js");
const client = new Client();
 
client.on("message", (message) =>{
    if(message.content.startsWith("!ayuda")){
        message.channel.send("Ayuda de prueba!")
    }
});
 
client.login("OTU0MTMyODM3MTczNDM2NDU3.YjOrcw.PxwxgV0a9kPBSftiNlwmWWwjXok")