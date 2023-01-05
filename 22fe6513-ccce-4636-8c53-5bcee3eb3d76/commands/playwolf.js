// 2名狼人、2名村民、2名神職：預言家、守衛
const channel = '797731060523597834';
const ms = require('ms');
var gameStarted = false;
var playerNo = 0;
const joinGameEmoji = '🤓';
const startGameEmoji = '🤝';
var playerAndEmoji = '';

const rChannel = [
    { cID: '798500873504030760', cName: "狼人", cIntro: "黑夜可以睜眼與隊友見面並討論戰術與選擇殺害對象。狼人可以選擇當夜不殺害任何玩家（空刀）或自殺（自刀）。白天混入村落中混淆好人。狼人可以在白天任何時候選擇公布角色牌自我淘汰（自爆）強制進入黑夜階段，並在黑夜階段結束時離場。", cImage: 'https://truth.bahamut.com.tw/s01/201912/85b0734a6eb2e7823d0c082787749a74.JPG', cSkill: '今晚想殺邊個呀?(禁佢嘅emoji)' },
    { cID: '798500977137287209', cName: "預言家", cIntro: "神職角色。每晚可以查驗一位存活玩家的所屬陣營，並在白天透過發言向好人報出資訊。", cImage: 'https://pic4.zhimg.com/v2-d4d6835b1f60f4a06e1fc4549912ab75_720w.jpg?source=172ae18b', cSkill: '今晚想查邊個呀?(禁佢嘅emoji)' },
    { cID: '798501074088361984', cName: "守衛", cIntro: "神職角色。每晚可以選擇守護一名玩家免受狼人殺害，並可以選擇守護自己或不進行守護，不可連續兩晚守護同一名玩家。", cImage: 'https://5b0988e595225.cdn.sohucs.com/images/20190306/a197527857d84407b7211c2f01093c85.png', cSkill: '今晚想保護邊個呀?(禁佢嘅emoji)' }
];

const roles = [
    { rName: "狼人", rIntro: "黑夜可以睜眼與隊友見面並討論戰術與選擇殺害對象。狼人可以選擇當夜不殺害任何玩家（空刀）或自殺（自刀）。白天混入村落中混淆好人。狼人可以在白天任何時候選擇公布角色牌自我淘汰（自爆）強制進入黑夜階段，並在黑夜階段結束時離場。", rImage: 'https://truth.bahamut.com.tw/s01/201912/85b0734a6eb2e7823d0c082787749a74.JPG', rSkill: '今晚想殺邊個呀?(禁佢嘅emoji)' },
    { rName: "狼人", rIntro: "黑夜可以睜眼與隊友見面並討論戰術與選擇殺害對象。狼人可以選擇當夜不殺害任何玩家（空刀）或自殺（自刀）。白天混入村落中混淆好人。狼人可以在白天任何時候選擇公布角色牌自我淘汰（自爆）強制進入黑夜階段，並在黑夜階段結束時離場。", rImage: 'https://truth.bahamut.com.tw/s01/201912/85b0734a6eb2e7823d0c082787749a74.JPG', rSkill: '今晚想殺邊個呀?(禁佢嘅emoji)' },
    { rName: "預言家", rIntro: "神職角色。每晚可以查驗一位存活玩家的所屬陣營，並在白天透過發言向好人報出資訊。", rImage: 'https://pic4.zhimg.com/v2-d4d6835b1f60f4a06e1fc4549912ab75_720w.jpg?source=172ae18b', roleSkill: '今晚想查邊個呀?(禁佢嘅emoji)' },
    { rName: "守衛", rIntro: "神職角色。每晚可以選擇守護一名玩家免受狼人殺害，並可以選擇守護自己或不進行守護，不可連續兩晚守護同一名玩家。", rImage: 'https://5b0988e595225.cdn.sohucs.com/images/20190306/a197527857d84407b7211c2f01093c85.png', rSkill: '今晚想保護邊個呀?(禁佢嘅emoji)' },
    { rName: "平民", rIntro: "又稱「村民」。沒有特殊技能，黑夜階段全程閉眼，透過白天階段所得資訊投票放逐疑似狼人的玩家。", rImage: 'https://pic4.zhimg.com/50/v2-5ba87b1317bc8b9db4f5b49133864876_hd.jpg?source=1940ef5c', rSkill: '你無技能呀, 等天光啦' },
    { rName: "平民", rIntro: "又稱「村民」。沒有特殊技能，黑夜階段全程閉眼，透過白天階段所得資訊投票放逐疑似狼人的玩家。", rImage: 'https://pic4.zhimg.com/50/v2-5ba87b1317bc8b9db4f5b49133864876_hd.jpg?source=1940ef5c', rSkill: '你無技能呀, 等天光啦' }
],
    emojis = ['💩', '🐒', '😫', '😍', '😇', '😊'];

var player = [
    { pID: null, pEmoji: null, pRole: "", pIntro: null, pImage: null, pSkill: null },
    { pID: null, pEmoji: null, pRole: "", pIntro: null, pImage: null, pSkill: null },
    { pID: null, pEmoji: null, pRole: "", pIntro: null, pImage: null, pSkill: null },
    { pID: null, pEmoji: null, pRole: "", pIntro: null, pImage: null, pSkill: null },
    { pID: null, pEmoji: null, pRole: "", pIntro: null, pImage: null, pSkill: null },
    { pID: null, pEmoji: null, pRole: "", pIntro: null, pImage: null, pSkill: null }
];
const ranRoles = genRenArray(roles);
const ranEmojis = genRenArray(emojis);



module.exports = {
    name: 'playwolf',
    description: "this command will start the Werewolf",
    async execute(message, Discord, client) {
        const playingWolf = message.guild.roles.cache.find(role => role.name === "PlayingWolf");
        const guard = message.guild.roles.cache.find(role => role.name === "守衛");
        const wolf = message.guild.roles.cache.find(role => role.name === "狼人");
        const prophet = message.guild.roles.cache.find(role => role.name === "預言家");
        let introEmbed = IntroEmbed(Discord);
        let messageEmbed = await message.channel.send(introEmbed);
        messageEmbed.react(joinGameEmoji);
        messageEmbed.react(startGameEmoji);
        client.on('messageReactionAdd', async (reaction, user) => {
            if (reaction.message.partial) await reaction.message.fetch();
            if (reaction.partial) await reaction.fetch();
            if (user.bot) return;
            if (!reaction.message.guild) return;
            if (reaction.message.channel.id == channel && reaction.emoji.name === startGameEmoji && !gameStarted) {
                message.channel.send('Total No. of player: ' + playerNo);
                message.channel.send('Game Start!');
                gameStarted = true;
                if (gameStarted) {
                    console.log('Game Started');
                    sendEmbed(message, client, Discord);
                }
            }
            if (reaction.message.channel.id == channel && reaction.emoji.name === joinGameEmoji && !gameStarted) {
                await reaction.message.guild.members.cache.get(user.id).roles.add(playingWolf);
                player[playerNo].pID = user.id;
                player[playerNo].pEmoji = ranEmojis[playerNo];
                player[playerNo].pRole = ranRoles[playerNo].rName;
                player[playerNo].pIntro = ranRoles[playerNo].rIntro;
                player[playerNo].pImage = ranRoles[playerNo].rImage;
                player[playerNo].pSkill = ranRoles[playerNo].rSkill;
                playerNo++;
                message.channel.send('Number of player: ' + playerNo);
            } else {
                return;
            }
        });
        client.on('messageReactionRemove', async (reaction, user) => {
            if (reaction.message.partial) await reaction.message.fetch();
            if (reaction.partial) await reaction.fetch();
            if (user.bot) return;
            if (!reaction.message.guild) return;
            if (reaction.message.channel.id == channel && reaction.emoji.name === joinGameEmoji && !gameStarted) {
                await reaction.message.guild.members.cache.get(user.id).roles.remove(playingWolf);
                player[--playerNo].pID = null;
                player[playerNo].pEmoji = null;
                player[playerNo].pRole = null;
                player[playerNo].pIntro = null;
                player[playerNo].pImage = null;
                player[playerNo].pSkill = null;
                message.channel.send('Number of player: ' + playerNo);
            } else {
                return;
            }
        });
    }

}

function IntroEmbed(Discord) {
    let embed = new Discord.MessageEmbed()
        .setColor('#474a4b')
        .setTitle('WereWolf')
        .setDescription('This is a embed of member to join game\n\n'
            + 'hit the \'🤓 \' for joining the game!\n\nhit the \'🤝 \' to start the game!')
        .setThumbnail('https://i.pinimg.com/736x/5c/a1/42/5ca142d34fd1903773b4f4e6f43d9045.jpg')
        .addFields(
            { name: 'Rule1', value: 'Try Hard' },
            { name: 'Rule2', value: 'Do not unmute youself until you turn' },
        )
        .setImage('https://p2.bahamut.com.tw/B/2KU/10/e076fc69d16fcdc1d1eb3050ba162fq5.JPG')
        .setFooter('Make sure to add a emoji on this embed if you wanna play.');
    return embed;
}

function genRenArray(array) {
    var ranArray = [],
        i = array.length,
        j = 0;
    while (i--) {
        j = Math.floor(Math.random() * (i));
        ranArray.push(array[j]);
        array.splice(j, 1);
    };
    return ranArray;
}

async function sendEmbed(message, client, Discord) {
    for (let i = 0; i < playerNo; i++) {
        playerAndEmoji += ' | ' + '<@' + player[i].pID + '>' + ':' + player[i].pEmoji;
    } playerAndEmoji += ' | ';
    for (let i = 0; i < playerNo.length; i++) {
        if (player[i].pRole === "平民") {
            let votingEmbed = VotingEmbed(Discord, player[i]);
            let pmEmbed = await client.users.cache.get(player[i].ID).send(votingEmbed);
            for (let j = 0; j < playerNo; j++) {
                pmEmbed.react(player[j].pEmoji);
            }
        }
    }
    for (let i = 0; i < rChannel.length; i++) {
        votingEmbed = VotingEmbed(Discord, rChannel[i]);
        channelEmbed = await client.channels.cache.get(rChannel[i].cID).send(votingEmbed);
        for (let j = 0; j < playerNo; j++) {
            channelEmbed.react(player[j].pEmoji);
        }
    }
}
function VotingEmbed(Discord, rChannel) {
    let embed = new Discord.MessageEmbed()
        .setColor('#474a4b')
        .setTitle("角色與簡介----------")
        .setDescription('你的身份是 : ' + rChannel.cName + '\n\n')
        .setThumbnail('https://i.pinimg.com/736x/5c/a1/42/5ca142d34fd1903773b4f4e6f43d9045.jpg')
        .addFields(
            { name: '簡介:', value: rChannel.cIntro },
            { name: '符號與玩家:', value: playerAndEmoji },
            { name: '技能:', value: rChannel.cSkill }
        )
        .setImage(rChannel.cImage)
        .setFooter('Aware of the time limit');
    return embed;
}