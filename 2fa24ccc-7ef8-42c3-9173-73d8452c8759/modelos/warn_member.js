const mongoose = require("mongoose");
const schema = new mongoose.Schema({
  guildid: {type: String, required: true},
  memberid: {type: String, requied:true},
  warnings: 0,
});
module.exports = mongoose.model("warn_member_final", schema)