import express from "express";

const server = express();

server.all("/", (req, res) => {
  console.log("Pinged");
  res.send("OK");
});

function keepAlive() {
  server.listen(3000, () => {
    console.log("Server is ready!" + Date.now);
  });
}

export default keepAlive;
