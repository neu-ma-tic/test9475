const weather = require('weather-js');

const Discord = require('discord.js');

module.exports = {
    name: "weather",
    description: "shows the current weather in a specified location",

     async run(bot, message, args) {
        weather.find({search: args.join(" "), degreeType: `C`}, function (error, result) {
            if(error) return message.channel.send(error);
            if(!args[0]) return message.channel.send('Please specify a location!')

            if(result === undefined || result.length === 0) return message.channel.send('**invalid** location!!')

            var current = result[0].current;
            var location = result[0].location;
            if((current.skytext=='Cloudy')||(current.skytext=='Rainy')||(current.skytext=='Mostly Cloudy')||(current.skytext=='Light Rain')||(current.skytext=='Rain Showers')||(current.skytext=='Mostly Rainy')||(current.skytext=='Rain')){
                const embed = new Discord.MessageEmbed()
                .setColor('#ff4267')
                .setAuthor(`Weather forecast for ${current.observationpoint}`)
                .setThumbnail(current.imageUrl)
                .setDescription(`**${current.skytext}**`)
                .addField('TimeZone', `UTC ${location.timezone}`, true)
                .addField('Degree Type', 'Celcius', true)
                .addField('Temperature', `${current.temperature}°`, true) 
                .addField('Wind', `${current.winddisplay}`, true)
                .addField('Feels Like', `${current.feelslike}°`, true)
                .addField('Humidity', `${current.humidity}%`, true)
                .setFooter('Time of Message: ' + message.createdAt);
                message.channel.send(embed);
                message.reply('Heavy MOOD detected in this region');

            }
            else{
                const embed = new Discord.MessageEmbed()
                .setColor('#ff4267')
                .setAuthor(`Weather forecast for ${current.observationpoint}`)
                .setThumbnail(current.imageUrl)
                .setDescription(`**${current.skytext}**`)
                .addField('TimeZone', `UTC ${location.timezone}`, true)
                .addField('Degree Type', 'Celcius', true)
                .addField('Temperature', `${current.temperature}°`, true) 
                .addField('Wind', `${current.winddisplay}`, true)
                .addField('Feels Like', `${current.feelslike}°`, true)
                .addField('Humidity', `${current.humidity}%`, true)
                .setFooter('Time of Message: ' + message.createdAt);
                message.channel.send(embed)
            }
        })
    }
}