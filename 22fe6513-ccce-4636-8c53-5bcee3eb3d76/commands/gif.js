const { MessageFlags } = require("discord.js");
const { url } = require("inspector");
const fetch = require("node-fetch");

module.exports = {
    name: 'gif',
    description: "This send a gif from tenor gif base.",
    async execute(message, args) {
        var keywords = "loli";
        if (args != '') {
            keywords = args;
        }
        let url = `https://api.tenor.com/v1/search?q=${keywords}&key=${process.env.TENORKEY}&contentfilter=high`;
        let response = await fetch(url);
        let json = await response.json();
        const index = Math.floor(Math.random() * json.results.length);
        message.channel.send(json.results[index].url);
    }
}