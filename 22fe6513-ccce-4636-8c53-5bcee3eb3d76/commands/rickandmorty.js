const { MessageFlags } = require("discord.js");
const { url } = require("inspector");
const fetch = require("node-fetch");

module.exports = {
    name: 'rickandmorty',
    description: "get random quotes from rick and morty by calling api",
    async execute(message, args) {
        let url = 'http://loremricksum.com/api/';
        var obj = await (await fetch(url)).json();
        message.channel.send(obj.data);
    }
}