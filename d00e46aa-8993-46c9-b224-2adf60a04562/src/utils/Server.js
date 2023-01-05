const express = require('express');
const server = express();

server.all('/', (req, res)=>{
    res.send(`Bot online`)
})
function keepAlive(client){
    server.listen(3000, ()=>{ client.logger.log('Server is ready!') });
}
module.exports = keepAlive;