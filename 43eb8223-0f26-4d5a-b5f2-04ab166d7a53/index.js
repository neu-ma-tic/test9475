const express = require('express');
 
const app = express();
 
app.get('/', (req, res) => {
  res.send('Hello Express app!')
});
 
app.listen(3000, () => {
  console.log('server started');
});
 
const Discord = require("discord.js");
const client = new Discord.Client();
const prefix = "#";
client.login("");