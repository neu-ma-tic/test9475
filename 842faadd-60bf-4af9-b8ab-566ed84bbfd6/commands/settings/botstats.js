bot.command({
 name: "stats",
 aliases: ["botstats"],
 code: `
$title[Bot Statistics]
$author[$username[$clientid];$useravatar[$clientid]]
$color[#fff0f3]
$addField[Others;
• Total commands: $commandsCount
• Latency: $botPing ms
• Uptime: $uptime
• Owner: $usertag[$botownerid]]
$addField[Versions;
• NodeJS Version: $getObjectProperty[nodev]
• Discord.js Version: $getObjectProperty[discordv]
]
$addField[Hosting Related Stats;
• CPU Usage: $cpu
• CPU Model: $djsEval[require ('os').cpus()[0\\].model;yes] 
• CPU Platform: $djsEval[require ('os').platform();yes]
• RAM Usage: $ram MB
• Memory Usage: $djsEval[process.memoryUsage().rss / 1024 / 1024;yes] MB]
 $djseval[d.object.nodev = process.version
d.object.discordv = require('discord.js').version
$createObject[{}]]`
})