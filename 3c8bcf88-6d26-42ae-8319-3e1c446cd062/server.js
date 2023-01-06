const express = require('express');
const server = express();

server.all('/', (req, res)=>{
       res.send("DiscordBot 24/7")
       })
       function keepAlive(){
        server.listen(3000, ()=>{console.log("Server is Ready!")
        })
}
module.exports = keepAlive;