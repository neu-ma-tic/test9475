const Discord = require('discord.js');
const request = require('request');
const youtube_node = require('youtube-node');
const config  = require('./config.json');
const client  = new Discord.Client();

client.login(config.token);

// Show message when jarvis comes online
client.on('ready', () => {
  console.log('I am ready!');
});

client.on('message', (message) => {

  // Set the prefix
  let prefix = '!';
  // Exit and stop if the prefix is not there or if user is a bot
  if (!message.content.startsWith(prefix) || message.author.bot) return;

  if (message.content.startsWith(prefix + "gif"))
  {
    // Split message to search GIPHY
    let splitWord = message.toString().split(" ");
    let gifWord   = "";

    // Loop through incase of multiple word search
    for( var i = 1; i < splitWord.length; i++)
    {
      if(i > 1)
      {
        gifWord = gifWord + "+";
      }

      gifWord = gifWord + splitWord[i];
    }

    request("http://api.giphy.com/v1/gifs/search?q=" + gifWord + "&api_key=" + config.giphyKey + "&limit=100", function (error, response, body)
    {
      if (!error && response.statusCode == 200)
      {
        // Convert body to JSON object
        let jsonUrl = JSON.parse(body);

        // Get random number to choose GIF
        let totGif = jsonUrl.data.length;

        if(totGif > 100)
        {
          totGif = 100;
        }

        let ranNum = Math.floor(Math.random() * totGif);

        message.channel.sendMessage(jsonUrl.data[ranNum].url);
      }
    });
  }

  if (message.content.startsWith(prefix + "img"))
  {
    // Split message to search image
    let splitWord = message.toString().split(" ");
    let searchWrd = "";
    let googKey   = config.googleKey;
    let cxKey     = config.cx;

    // Loop through incase of multiple word search
    for( var i = 1; i < splitWord.length; i++)
    {
      if(i > 1)
      {
        searchWrd = searchWrd + " ";
      }

      searchWrd = searchWrd + splitWord[i];
    }

    let page = 1;

    request("https://www.googleapis.com/customsearch/v1?key=" + googKey + "&cx=" + cxKey + "&q=" + searchWrd + "&searchType=image&alt=json&num=10&start="+page, function(err, res, body) {
      let data;

      try {
        data = JSON.parse(body);
      } catch (error) {
        console.log(error)
        return;
      }

      if(!data){
        console.log(data);
        message.channel.sendMessage( "Error:\n" + JSON.stringify(data));
        return;
      } else if (!data.items || data.items.length == 0){
        console.log(data);
        message.channel.sendMessage( "No result for '" + args + "'");
        return;
      }
      // Get random number
      let ranNum = Math.floor(Math.random() * data.items.length);
      let randResult = data.items[ranNum];
      message.channel.sendMessage( randResult.title + '\n' + randResult.link);
    });
  }

  if (message.content.startsWith(prefix + "youtube"))
  {
    // Split message to search image
    let splitWord = message.toString().split(" ");
    let searchWrd = "";
    this.youtube = new youtube_node();
    this.youtube.setKey(config.googleKey);
    this.youtube.addParam('type', 'video');

    // Loop through incase of multiple word search
    for( var i = 1; i < splitWord.length; i++)
    {
      if(i > 1)
      {
        searchWrd = searchWrd + " ";
      }

      searchWrd = searchWrd + splitWord[i];
    }

    this.youtube.search(searchWrd, 1, function(error, result) {
      if (error)
      {
        console.log(error);
        message.channel.sendMessage("¯\\_(ツ)_/¯");
      }
      else {
        if (!result || !result.items || result.items.length < 1)
        {
          message.channel.sendMessage("¯\\_(ツ)_/¯");
        } else {
          // Get random number
          let ranNum = Math.floor(Math.random() * result.items.length);
          let randResult = result.items[ranNum].id.videoId;
          message.channel.sendMessage("http://www.youtube.com/watch?v=" + randResult);
        }
      }
    });
  }

});
