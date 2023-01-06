const express = require('express')
const app = express()

app.all('/', (req, res) => {
  res.send('The server is online')
})

function keepAlive(){
  app.listen(5000, () => {
    console.log('Server started in http://localhost:5000')
  })
}

module.exports = keepAlive;