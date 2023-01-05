const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => res.send("I'm not dead! :D"));

app.listen(port, () => console.log(`listening at http://localhost:${port}`));

const fetch = require("node-fetch");
const Discord = require("discord.js");
const client = new Discord.Client();

const prefix = ":"; // your short name here (eg. lyh_)

client.on("message", async function(message) {
	if (message.author.bot) return;
	if (!message.content.startsWith(prefix)) return;

	const commandBody = message.content.slice(prefix.length);
	const args = commandBody.split(' ');
	const command = args.shift().toLowerCase();

	if (command === "ping") {
		const timeTaken = Date.now() - message.createdTimestamp;
		message.reply(`Pong! This message had a latency of ${timeTaken}ms.`);
	}

	else if (command === "echo") {
		const string = args.join(" ");
		message.channel.send(string);
	}

	else if (command === "name") {
		message.channel.send(`My creator's name is Ethan Ooi!`); // your full name here
	}

  else if (command === "gif") {
    let keywords = "Electronics"; //The default gif search term


if (args.length) {
     keywords = args.join(" ");  //Checks the array
}
let url = `https://api.tenor.com/v1/search?q=${keywords}&key=${process.env.TENOR_KEY}&contentfilter=high`;  //Tenor Url

let response = await fetch(url);
let json =  await response.json(); //Big Data Sheet
const index = await Math.floor(Math.random() * json.results.length) //Randomize the result
message.channel.send(json.results[index].url);  // Sends GIF    
message.channel.send("GIF from Tenor: " + keywords); 
}

console.log(args)

});

client.login(process.env.BOT_TOKEN);