const { MessageFlags } = require("discord.js");
const { url } = require("inspector");
const fetch = require("node-fetch");

module.exports = {
    name: 'weather',
    description: "get current weather from HK GOV",
    async execute(message, args) {
        let url = 'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang=tc';
        let response = await fetch(url);
        let obj = await response.json();
        message.channel.send("大致情况 : \n**" + obj.generalSituation + "**\n\n" + "熱帶氣旋警告信號 : \n**" + obj.tcInfo + "**\n\n"+ "火災危險警告 : \n**" + obj.fireDangerWarning + " **\n\n"+"本港地區今晚及明日天氣預測 : \n**" + obj.forecastDesc + "**\n\n"+ "更新時間 : **" + obj.updateTime + "**");
        
    }
}