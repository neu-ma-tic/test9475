const mongoose = require('mongoose');
const config = require('../../../config.json');

module.exports = mongoose.model("Guild", new mongoose.Schema({
    guildID: {
        type: String,
        unique: true,
        required: true,
    },
    prefix: {
        type: String,
        required: true,
        default: config.prefix,
    }



}));
