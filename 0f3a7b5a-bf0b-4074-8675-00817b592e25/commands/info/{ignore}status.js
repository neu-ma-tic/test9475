const { MessageEmbed } = require('discord.js')
// const config = require('../../config.json'); // Making so we can use the config.json as a config file
const fetch = require("node-fetch"); // swapped to node-fetch instead of request to use async / await
const { stat } = require('fs');
module.exports = {
    name : "status",
    category : 'info',
    description : "Връща информация за FiveM Сървъра",
    prefix : "!",

    /**
     * @param {Bot} bot
     * @param {Message} message
     * @param {String[]} args
     */

    run : async(client, message, args) => {

        await get_serverinfo().then(async(finalDataJSON) => {
            // let status = jsondata.status;
            // let serverdata = jsondata.serverdata;
            const { hostname, clients, vars, sv_maxclients } = finalDataJSON.serverData

            if (finalDataJSON.status != null && finalDataJSON.status == 200) {
                const serverOnlineMsg = new MessageEmbed()
                    .setTitle('MoonLabsRP СТАТИСТИКА')
                    .setThumbnail('https://i.imgur.com/Pr0OBYu.png')
                    .setTimestamp()
                    .setDescription("**Сървър Статус:** 🟢 online")
                    .addFields(
                        { name: 'Активни Играчи :', value: `${clients}/${sv_maxclients}` },
                        { name: 'Дискорд :', value: `https://discord.gg/Uk8wrrJA2P`},
                    )
                    .setColor('#0099ff')
            await message.channel.send(serverOnlineMsg)
            } else {
                const serverOfflineMsg = new MessageEmbed()
                    .setTitle('MoonLabsRP СТАТИСТИКА')
                    .setThumbnail('https://i.imgur.com/Pr0OBYu.png')
                    .setTimestamp()
                    .addFields(
                        { name: '**Сървър Статус:** ', value: '🔴 offline' },
                        { name: 'Дискорд :', value: `https://discord.gg/Uk8wrrJA2P`},
                    )
                    // .setDescription("**Сървър Статус:** 🔴 offline")
                    .setColor('#0099ff')
                await message.channel.send(serverOfflineMsg)
            }

        })

    }
}

async function get_serverinfo(){
  const url = 'https://servers-live.fivem.net/api/servers/single/6v6or8'
  const res = await fetch(url);
  const status = await res.status;
  const resData = await res.json();//assuming data is json
  const resDataServer = resData.Data;//assuming data is json
  let finalDataJSON = {
      status: status, 
      serverData: resDataServer
  }
  return finalDataJSON;
}