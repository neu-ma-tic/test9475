const mongoose = require("mongoose");
const schema = new mongoose.Schema({
   guildid: {type: String},
   userid: {type: String},
   rolid: {type: String},
   time: {type: Number}
});
module.exports = mongoose.model("tempmute_terminado",schema);