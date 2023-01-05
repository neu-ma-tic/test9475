const mongoose = require("mongoose");
const schema = new mongoose.Schema({
  guildid: {type: String, required: true},
  role: {type: Boolean, required: true},
  roleTime: {type: Number, default: 0},
  roleid: {type: String, default: "0"},
  kick: {type: Boolean, required:true},
  kicktime: {type: Number, default: 0},
  ban:{type: Boolean, required: true},
  bantime:{type: Number, default: 0},
  tempmute: {type: Boolean},
  mutetime: {type: Number, default: 0},
  temprole: {type: String, default: "0"},
  times: {type: Number}
})
module.exports = mongoose.model("warn_sistem_final", schema);