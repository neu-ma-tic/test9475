const fs = require("fs");
var list = ["dumb","idiot","stupid"];
class Bot {

  filter(message){
    for (let i = 0; i in list; i++){
      if (message.content.toLowerCase().includes(list[i])) {
        console.log(message.content);
        message.delete();
        break;
      }
    }
  }

  

}


module.exports = Bot;
