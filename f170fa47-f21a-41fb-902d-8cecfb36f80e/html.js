const http = require("http");
http.createServer((_, res)=>res.end("Windwalker Studio Status : READY")).listen(8080);