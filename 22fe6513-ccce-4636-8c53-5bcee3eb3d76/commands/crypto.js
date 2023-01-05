const rp = require("request-promise");
const requestOptions = {
  method: "GET",
  uri: "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest",
  // qs: {
  //   start: "1",
  //   limit: "5000",
  //   convert: "USD",
  // },
  headers: {
    "X-CMC_PRO_API_KEY": process.env.CMKAPIKEY,
  },
  json: true,
  gzip: true,
};


module.exports = {
  name: "crypto",
  description: "get the latest price of crypto",
  async execute(message, args) {
    if(args.length){
      var symbol = args[0].toUpperCase();
      requestOptions.uri+=`?symbol=${symbol}`;
      rp(requestOptions)
      .then((response) => {
        message.channel.send(`${response.data[symbol].name } : $${response.data[symbol].quote.USD.price } \n 24hrs changed: ${response.data[symbol].quote.USD.percent_change_24h.toFixed(2)}%`);
      });
      requestOptions.uri="https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest";
      // .catch((err) => {
      //   message.channel.send("API call error:", err.status);
      // });
    }
  },
};
