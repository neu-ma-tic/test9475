const { MessageFlags } = require("discord.js");
const { url } = require("inspector");
const fetch = require("node-fetch");

module.exports = {
    name: 'meme',
    description: "get random meme by calling api",
    async execute(message, args) {
        let url = 'https://meme-api.herokuapp.com/gimme';
        var obj = await (await fetch(url)).json();
        message.channel.send(obj.title);
        message.channel.send(obj.url);
    }
}