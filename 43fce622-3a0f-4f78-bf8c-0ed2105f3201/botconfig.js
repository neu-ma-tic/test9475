module.exports = {
  Admins: ["UserID", "UserID"], //Admins of the bot
  ExpressServer: true,//If you wanted to make the website run or not
  DefaultPrefix: process.env.Prefix || "!", //Default prefix, Server Admins can change the prefix
  Port: 3000, //Which port website gonna be hosted
  SupportServer: "https://discord.gg/sbySMS7m3v", //Support Server Link
  Token: process.env.Token || "ODg4MTIzNTMxMzU3OTg2ODU3.YUOHfg.xhfJRgDzX4g3azgKV7HjEUSoD4A", //Discord Bot Token
  ClientID: process.env.Discord_ClientID || "888123531357986857", //Discord Client ID
  ClientSecret: process.env.Discord_ClientSecret || "sbekSUv-REEPOFObxV0NZkCV5iYY7efh", //Discord Client Secret
  Scopes: ["identify", "guilds", "applications.commands"], //Discord OAuth2 Scopes
  CallbackURL: "/api/callback", //Discord OAuth2 Callback URL
  "24/7": false, //If you want the bot to be stay in the vc 24/7
  CookieSecret: "Macaco Prego é PIKA", //A Secret like a password
  IconURL:
    "https://raw.githubusercontent.com/SudhanPlayz/Discord-MusicBot/master/assets/logo.gif", //URL of all embed author icons | Dont edit unless you dont need that Music CD Spining
  Permissions: 2205280576, //Bot Inviting Permissions
  Website: process.env.Website || "http://localhost", //Website where it was hosted at includes http or https || Use "0.0.0.0" if you using Heroku

  //Lavalink
   Lavalink: {
    id: "Main",
    host: "0.0.0.0",
    port: 3000,
    pass: "allanbrandao", 
    secure: true, // Set this to true if you're self-hosting lavalink on replit.
  },


  //Please go to https://developer.spotify.com/dashboard/
  Spotify: {
    ClientID: process.env.Spotify_ClientID || "5aeeabe26bfa49dd822a62479b437757", //Spotify Client ID
    ClientSecret: process.env.Spotify_ClientSecret || "bdf29f89c4014113babb3d461496db11", //Spotify Client Secret
  },
};
