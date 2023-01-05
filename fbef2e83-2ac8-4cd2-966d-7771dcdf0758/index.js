// discord.js 클래스
const { Client, Intents, Collection } = require('discord.js');
const { token, channelId } = require(__dirname + '/config.json');
// embed
const { createEmbed } = require(__dirname + '/embed/welcomEmbed.js');
// DB
const db_config = require(__dirname + '/DB/DBConnection.js');
const conn = db_config.init();
// student info
let id, name;

const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MEMBERS] });

// command 파일 읽기/
const fs = require('fs');

client.commands = new Collection();
const commandFiles = fs.readdirSync(__dirname + '/commands')
    .filter(file => file.endsWith('.js'));
// fs.readSync => 디렉토리에 있는 파일 이름을 배열로 반환
// .js로 끝나는 파일만 filter로 선택

for (const file of commandFiles) {
    const command = require(__dirname + `/commands/${file}`);

    client.commands.set(command.data.name, command);
}

client.once('ready', async () => {
    console.log(`Ready!\nLogged in as ${client.user.tag}`);
    try {
        conn.connect();
        console.log("Connected MySQL!");
    } catch (e) {
        console.error(e);
    }
})

client.on('interactionCreate', async interaction => {
    // console.log(interaction);
    if (interaction.isSelectMenu() || interaction.commandName === 'insert') {
        if (interaction.isSelectMenu()) {
            const track = interaction.values;
            const sql = `insert into std_list(sid, sname, track) values('${id}', '${name}', '${track}');`;
            conn.query(sql, function (error, result, field) {
                if (error) console.log(error);
                else console.log('SQL Success!');
                console.log(result);
            });
            await interaction.update({ content: `Success! Welcome ${name} in Root!`, components: [] });
        }
        else {
            const command = client.commands.get(interaction.commandName);

            console.log(`${interaction.user.tag} in #${interaction.channel.name} triggered an interaction.\n`
                + `command used: ${interaction.commandName}`);

            try {
                await command.execute({client, interaction});

                // console.log(interaction);
            } catch (error) {
                console.error(error);
                await interaction.reply({content: 'The was error while executing this command!', ephemeral: true});
            }

            const stdID = command.getID()
            id = stdID.id;
            name = stdID.name;
        }
    }
    else if (interaction.isCommand()) {

        const command = client.commands.get(interaction.commandName);

        if (!command) return;

        console.log(`${interaction.user.tag} in #${interaction.channel.name} triggered an interaction.\n`
            + `command used: ${interaction.commandName}`);

        try {
            await command.execute({client, interaction});

            // console.log(interaction);
        } catch (error) {
            console.error(error);
            await interaction.reply({content: 'The was error while executing this command!', ephemeral: true});
        }
    }
});

// add member event
client.on('guildMemberAdd', async member => {
    console.log('guildMemberAdd Event Triggered!');

    await client.channels.cache.get(channelId).send({ embeds: [createEmbed({ member })] });
});

// events 파일 읽기
// const eventFiles = fs.readdirSync(__dirname + '/events')
//     .filter(file => file.endsWith('.js'));
//
// for (const file of eventFiles) {
//     const event = require(__dirname + `/events/${file}`);
//     // console.log(event);
//     if (event.once) {
//         client.once(event.name, async (...args) => event.execute(...args));
//     } else {
//         client.on(event.name, async (...args) => event.execute(...args));
//     }
// }

// client login
client.login(token);