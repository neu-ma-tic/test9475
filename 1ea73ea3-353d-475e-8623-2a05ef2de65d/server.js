const express = require('express');

const server = express();

server.all('/', (req, res) =>{
  res.send('discordbot-script is Running!');
});

function keepAlive() {
  server.listen(4000, () =>{
    console.log('Server Is Ready!');
  });
}

module.exports = keepAlive;