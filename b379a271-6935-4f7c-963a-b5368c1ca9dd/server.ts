import { opine } from "https://deno.land/x/opine@1.3.4/mod.ts";

const server = opine();

server.all("/", (req, res) => {
  res.send("OK");
});

function keepAlive() {
  server.listen(3000, () => {
    console.log("Server is ready!" + Date.now);
  });
}

export default keepAlive;
