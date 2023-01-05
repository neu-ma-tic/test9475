const Discord = require('discord.js');
const client = new Discord.Client();
client.login('ODQ1MTg4MTk5NjkzNTQ5NTY4.YKdU2Q.dWQ3bT5MjVmOsHXDR_i0zdXzO2M');

client.on('message', messageDiscord);
const userBernard = "300983808386400256";
const userPetrock = "334627283753238528";
const userMarco = "749905192492990484";

function messageDiscord(msg){
    if(msg.content.toLowerCase().includes("tenor") && (msg.member.user.id == userPetrock)){
        msg.delete();
    }
}