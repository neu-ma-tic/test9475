const express = require("express")
const app = express()

app.get("/", (req,res) => {
res.send("hello hell!")
})

app.listen(3000, () => {
  console.log("Project is ready!")
})..