const mongoose = require('mongoose');

module.exports = mongoose.model("Users", new mongoose.Schema({
    guildID: {
        type: String,
        required: true,
    },
    userID: {
        type: String,
        required: true,
    },
    steamID: {
        type: String,
    },



    
    messages: {
        type: Number,
        default: 0, 
    },

}));
