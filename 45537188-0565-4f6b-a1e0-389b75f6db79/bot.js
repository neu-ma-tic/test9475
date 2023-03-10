(async () => {
    let process = require('process');
    process.on('uncaughtException', function(err) {
        console.log(`Error!`);
        console.log(err);
    });
    const events = require('events');
    const {
        exec
    } = require("child_process")
    let Discord = require("discord.js")
    let Database = require("easy-json-database")
    let {
        MessageEmbed,
        MessageButton,
        MessageActionRow,
        Intents,
        Permissions,
        MessageSelectMenu
    } = require("discord.js")
    let logs = require("discord-logs")
    let Invite = require("discord-inviter-tracker")
    const ms = require("ms")
    let https = require("https")
    let fs = require('fs');
    const devMode = typeof __E_IS_DEV !== "undefined" && __E_IS_DEV;
    const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
    const s4d = {
        Discord,
        database: new Database(`./database.json`),
        fire: null,
        joiningMember: null,
        reply: null,
        tokenInvalid: false,
        tokenError: null,
        player: null,
        manager: null,
        Inviter: null,
        message: null,
        notifer: null,
        checkMessageExists() {
            if (!s4d.client) throw new Error('You cannot perform message operations without a Discord.js client')
            if (!s4d.client.readyTimestamp) throw new Error('You cannot perform message operations while the bot is not connected to the Discord API')
        }
    };
    s4d.client = new s4d.Discord.Client({
        intents: [Object.values(s4d.Discord.Intents.FLAGS).reduce((acc, p) => acc | p, 0)],
        partials: ["REACTION", "CHANNEL"]
    });
    s4d.client.on('ready', () => {
        console.log(s4d.client.user.tag + " is alive!")
    })
    logs(s4d.client);
    s4d.Inviter = new Invite(s4d.client)
    s4d.Inviter.on("WARN", function(e) {
        console.log('WARN: ' + e)
    })
    var randomcevap;

    function listsGetRandomItem(list, remove) {
        var x = Math.floor(Math.random() * list.length);
        if (remove) {
            return list.splice(x, 1)[0];
        } else {
            return list[x];
        }
    }


    await s4d.client.login((process.env.token)).catch((e) => {
        s4d.tokenInvalid = true;
        s4d.tokenError = e;
        if (e.toString().toLowerCase().includes("token")) {
            throw new Error("An invalid bot token was provided!")
        } else {
            throw new Error("Privileged Gateway Intents are not enabled! Please go to https://discord.com/developers and turn on all of them.")
        }
    });

    const http = require('http');
    const server = http.createServer((req, res) => {
        res.writeHead(200);
        res.end('This site was created to keep bot on 25/8');
    });
    server.listen(3000);

    s4d.client.on('messageCreate', async (s4dmessage) => {
        if (!((s4dmessage.author).bot)) {
            if (!s4d.database.has(String(('xp-' + String(s4dmessage.member.id))))) {
                s4d.database.set(String(('xp-' + String(s4dmessage.member.id))), 0);
            }
            if (!s4d.database.has(String(('level-' + String(s4dmessage.member.id))))) {
                s4d.database.set(String(('level-' + String(s4dmessage.member.id))), 1);
            }
            if (!s4d.database.has(String(('xpcooldown-' + String(s4dmessage.member.id))))) {
                s4d.database.set(String(('xpcooldown-' + String(s4dmessage.member.id))), (Math.floor(new Date().getTime() / 1000)));
            }
            if ((Math.floor(new Date().getTime() / 1000)) > s4d.database.get(String(('xpcooldown-' + String(s4dmessage.member.id))))) {
                s4d.database.set(String(('xp-' + String(s4dmessage.member.id))), (s4d.database.get(String(('xp-' + String(s4dmessage.member.id)))) + 10));
                s4d.database.set(String(('xpcooldown-' + String(s4dmessage.member.id))), ((Math.floor(new Date().getTime() / 1000)) + 20));
            }
            if (s4d.database.get(String(('xp-' + String(s4dmessage.member.id)))) > 150 * s4d.database.get(String(('level-' + String(s4dmessage.member.id))))) {
                s4d.database.set(String(('xp-' + String(s4dmessage.member.id))), 0);
                s4d.database.set(String(('level-' + String(s4dmessage.member.id))), (s4d.database.get(String(('level-' + String(s4dmessage.member.id)))) + 1));
                s4dmessage.channel.send({
                    content: String(([s4dmessage.author, ', ``', s4d.database.get(String(('level-' + String(s4dmessage.member.id)))), '. `` **seviyeye ula??t??n!**', ''].join('')))
                });
            }
            if ((s4dmessage.content).toLowerCase() == String(s4d.database.get(String(('Prefix-' + String((s4dmessage.guild || {}).id))))) + 'seviyem' || (s4dmessage.content).toLowerCase() == String(s4d.database.get(String(('Prefix-' + String((s4dmessage.guild || {}).id))))) + 'rank' || (s4dmessage.content).toLowerCase() == String(s4d.database.get(String(('Prefix-' + String((s4dmessage.guild || {}).id))))) + 'seviye') {
                let rank = new MessageEmbed()
                rank.addField('Seviyen', ['**', s4d.database.get(String(('level-' + String(s4dmessage.member.id)))), '**'].join(''), true);
                rank.addField('Xp\'in', ['**', s4d.database.get(String(('xp-' + String(s4dmessage.member.id)))), '**'].join(''), true);
                rank.addField('Yeni Seviyeye Ula??mak i??in gereken XP', ['**', 150 * s4d.database.get(String(('level-' + String(s4dmessage.member.id)))) - s4d.database.get(String(('xp-' + String(s4dmessage.member.id)))), '**'].join(''), false);
                s4dmessage.channel.send({
                    embeds: [rank]
                });
            }
        }

    });

    s4d.client.on('interactionCreate', async (interaction) => {
        if ((interaction.customId).slice(-1) == 'k') {
            (((interaction.guild).members.cache.get((String((interaction.customId)).replaceAll('k', String('')))) || await (interaction.guild).members.fetch((String((interaction.customId)).replaceAll('k', String('')))))).roles.add(((interaction.guild).roles.cache.get('991770569819312198')));
            (((interaction.guild).members.cache.get((String((interaction.customId)).replaceAll('k', String('')))) || await (interaction.guild).members.fetch((String((interaction.customId)).replaceAll('k', String('')))))).roles.add(((interaction.guild).roles.cache.get('986683864955121725')));
            (((interaction.guild).members.cache.get((String((interaction.customId)).replaceAll('k', String('')))) || await (interaction.guild).members.fetch((String((interaction.customId)).replaceAll('k', String('')))))).roles.remove(((interaction.guild).roles.cache.get('991692264642453555')));
            await interaction.reply({
                ephemeral: true,
                content: (String((((interaction.guild).members.cache.get((String((interaction.customId)).replaceAll('k', String('')))) || await (interaction.guild).members.fetch((String((interaction.customId)).replaceAll('k', String(''))))).user).username) + '  kullan??c??s??n?? ``10-12`` tayfa olarak kaydettim'),
                components: []
            });
        }
        if ((interaction.customId).slice(-1) == 'o') {
            (((interaction.guild).members.cache.get((String((interaction.customId)).replaceAll('o', String('')))) || await (interaction.guild).members.fetch((String((interaction.customId)).replaceAll('o', String('')))))).roles.add(((interaction.guild).roles.cache.get('991770736379310250')));
            (((interaction.guild).members.cache.get((String((interaction.customId)).replaceAll('o', String('')))) || await (interaction.guild).members.fetch((String((interaction.customId)).replaceAll('o', String('')))))).roles.add(((interaction.guild).roles.cache.get('986683864955121725')));
            (((interaction.guild).members.cache.get((String((interaction.customId)).replaceAll('o', String('')))) || await (interaction.guild).members.fetch((String((interaction.customId)).replaceAll('o', String('')))))).roles.remove(((interaction.guild).roles.cache.get('991692264642453555')));
            await interaction.reply({
                ephemeral: true,
                content: (String((((interaction.guild).members.cache.get((String((interaction.customId)).replaceAll('o', String('')))) || await (interaction.guild).members.fetch((String((interaction.customId)).replaceAll('o', String(''))))).user).username) + '  kullan??c??s??n?? ``13-17`` tayfa olarak kaydettim'),
                components: []
            });
        }
        if ((interaction.customId).slice(-1) == 'b') {
            (((interaction.guild).members.cache.get((String((interaction.customId)).replaceAll('b', String('')))) || await (interaction.guild).members.fetch((String((interaction.customId)).replaceAll('b', String('')))))).roles.add(((interaction.guild).roles.cache.get('991770800539570227')));
            (((interaction.guild).members.cache.get((String((interaction.customId)).replaceAll('b', String('')))) || await (interaction.guild).members.fetch((String((interaction.customId)).replaceAll('b', String('')))))).roles.add(((interaction.guild).roles.cache.get('986683864955121725')));
            (((interaction.guild).members.cache.get((String((interaction.customId)).replaceAll('b', String('')))) || await (interaction.guild).members.fetch((String((interaction.customId)).replaceAll('b', String('')))))).roles.remove(((interaction.guild).roles.cache.get('991692264642453555')));
            await interaction.reply({
                ephemeral: true,
                content: (String((((interaction.guild).members.cache.get((String((interaction.customId)).replaceAll('b', String('')))) || await (interaction.guild).members.fetch((String((interaction.customId)).replaceAll('b', String(''))))).user).username) + '  kullan??c??s??n?? ``18+`` tayfa olarak kaydettim'),
                components: []
            });
        }
        if ((interaction.customId).slice(-1) == 'r') {
            s4d.client.channels.cache.get('992829644560662578').send({
                content: String((String(((interaction.guild).members.cache.get((String((interaction.customId)).replaceAll('r', String('')))) || await (interaction.guild).members.fetch((String((interaction.customId)).replaceAll('r', String(''))))).user) + ' reddedildin!'))
            });
            await interaction.reply({
                ephemeral: true,
                content: (String((((interaction.guild).members.cache.get((String((interaction.customId)).replaceAll('r', String('')))) || await (interaction.guild).members.fetch((String((interaction.customId)).replaceAll('r', String(''))))).user).username) + ' kullan??c??s??n?? reddetdim'),
                components: []
            });
        }

    });

    s4d.client.on('ready', async () => {
        if (false) {}

    });

    s4d.client.on('messageCreate', async (s4dmessage) => {
        if (s4dmessage.author.bot) {
            return;
        }
        if (((s4dmessage.channel).id) == '991757119953059861') {
            s4d.database.set(String(('KayitForm-' + String(s4dmessage.member.id))), (s4dmessage.content));
            s4dmessage.delete();
            let Form = new MessageEmbed()
            Form.setTitle(s4dmessage.member.user.username);
            Form.addField('Formu', String(s4d.database.get(String(('KayitForm-' + String(s4dmessage.member.id))))), false);
            s4d.client.channels.cache.get('991802602159349820').send({
                embeds: [Form],
                components: [(new MessageActionRow()
                    .addComponents(new MessageButton()
                        .setCustomId((String(s4dmessage.member.id) + 'k'))
                        .setLabel('10-12 Tayfa')
                        .setStyle(('SUCCESS')),
                        new MessageButton()
                        .setCustomId((String(s4dmessage.member.id) + 'o'))
                        .setLabel('13-17 Tayfa ')
                        .setStyle(('SUCCESS')),
                        new MessageButton()
                        .setCustomId((String(s4dmessage.member.id) + 'b'))
                        .setLabel('18+ Tayfa')
                        .setStyle(('SUCCESS')),
                        new MessageButton()
                        .setCustomId((String(s4dmessage.member.id) + 'r'))
                        .setLabel('Reddet')
                        .setStyle(('DANGER')),
                    ))]
            }).then(async m => {

            });
        }

    });

    s4d.Inviter.on('UserInvited', async function(member, uses, inviter, invite) {
        if (!((inviter) == null)) {
            if (!((inviter) == (member.user))) {
                s4d.client.channels.cache.get('992830450785595392').send({
                    content: String(([member.user, ' sunucuya kat??ld??, onu davet eden ki??i **', (inviter).username, '** ??uan ', uses, ' daveti var.'].join('')))
                });
            } else {
                s4d.client.channels.cache.get('992830450785595392').send({
                    content: String((String(member.user) + ' sunucuya kat??ld??, kendi kendini davet etti!'))
                });
            }
        } else {
            s4d.client.channels.cache.get('992830450785595392').send({
                content: String((String(member.user) + ' sunucuya kat??ld??, onu davet eden ki??iyi bulamad??m!'))
            });
        }

    });

    s4d.client.on('messageCreate', async (s4dmessage) => {
        if (s4dmessage.author.bot) {
            return;
        }
        if (!s4d.database.has(String(('Prefix-' + String((s4dmessage.guild).id))))) {
            s4d.database.set(String(('Prefix-' + String((s4dmessage.guild).id))), '!');
        }
        if ((((s4dmessage.content).toLowerCase()) || '').startsWith((String(s4d.database.get(String(('Prefix-' + String((s4dmessage.guild).id))))) + 'tekrarla') || '')) {
            s4d.database.set(String(('soyle' + String(s4dmessage.member.id))), ((s4dmessage.content).split(' ')));
            s4d.database.get(String(('soyle' + String(s4dmessage.member.id)))).shift();
            s4d.database.set(String(('soyle' + String(s4dmessage.member.id))), (s4d.database.get(String(('soyle' + String(s4dmessage.member.id)))).join(' ')));
            s4dmessage.delete();
            (s4dmessage.channel).sendTyping();
            s4dmessage.channel.send({
                content: String(([s4d.database.get(String(('soyle' + String(s4dmessage.member.id)))), ' ||Komutu Kullanan Ki??i - ', s4dmessage.author, '||'].join('')))
            });
        }
        if ((((s4dmessage.content).toLowerCase()) || '').startsWith((String(s4d.database.get(String(('Prefix-' + String((s4dmessage.guild).id))))) + 'otocevap') || '')) {
            if (!s4d.database.has(String('otocevap'))) {
                s4d.database.set(String('otocevap'), false);
            }
            if ((s4dmessage.content).split(' ').slice(-1)[0].toLowerCase() == 'a??') {
                if (s4d.database.get(String('otocevap')) == false) {
                    s4d.database.set(String('otocevap'), true);
                    s4dmessage.reply({
                        content: String('Otocevap a????ld??'),
                        allowedMentions: {
                            repliedUser: true
                        }
                    });
                } else {
                    s4dmessage.reply({
                        content: String('Otocevap zaten a????k!'),
                        allowedMentions: {
                            repliedUser: true
                        }
                    });
                }
            } else if ((s4dmessage.content).split(' ').slice(-1)[0].toLowerCase() == 'kapat') {
                if (s4d.database.get(String('otocevap')) == true) {
                    s4d.database.set(String('otocevap'), false);
                    s4dmessage.reply({
                        content: String('Otocevap kapat??ld??'),
                        allowedMentions: {
                            repliedUser: true
                        }
                    });
                } else {
                    s4dmessage.reply({
                        content: String('Otocevap zaten kapal??!'),
                        allowedMentions: {
                            repliedUser: true
                        }
                    });
                }
            }
        }
        if ((s4dmessage.content) == '<@987436391459881010>') {
            randomcevap = ['Efendim?', 'efendim?', 'Noldu?', 'Buyur?', 'Noldu knk?'];
            s4dmessage.channel.send({
                content: String((String(listsGetRandomItem(randomcevap, false))))
            });
        }
        if ((((s4dmessage.content).toLowerCase()) || '').startsWith((String(s4d.database.get(String(('Prefix-' + String((s4dmessage.guild).id))))) + 'param') || '')) {
            if (((s4dmessage).mentions.users.size) == 0) {
                if (!s4d.database.has(String(('Para-' + String(s4dmessage.member.id))))) {
                    s4d.database.set(String(('Para-' + String(s4dmessage.member.id))), 0);
                }
                s4dmessage.channel.send({
                    content: String((['**', s4dmessage.member.user.username, ', senin ??uanda** ``', s4d.database.get(String(('Para-' + String(s4dmessage.member.id)))), '`` **paran var.**'].join('')))
                });
            } else if (((s4dmessage).mentions.users.size) == 1) {
                if (!s4d.database.has(String(('Para-' + String((s4dmessage.mentions.members.first().user).id))))) {
                    s4d.database.set(String(('Para-' + String((s4dmessage.mentions.members.first().user).id))), 0);
                }
                s4dmessage.channel.send({
                    content: String((['**', (s4dmessage.mentions.members.first().user).username, ', isimli ki??inin ??uanda** ``', s4d.database.get(String(('Para-' + String((s4dmessage.mentions.members.first().user).id)))), '`` **paras?? var.**'].join('')))
                });
            }
        }

    });

    s4d.client.on('messageCreate', async (s4dmessage) => {
        if (s4dmessage.author.bot) {
            return;
        }
        if (!(s4d.database.get(String('otocevap')) == false)) {
            if ((s4dmessage.content).toLowerCase() == 'sa') {
                s4dmessage.channel.send({
                    content: String('Aleyk??m Selam Ho??geldin')
                });
            }
            if ((String(((s4dmessage.content).toLowerCase())).includes(String('bar????'))) || (String(((s4dmessage.content).toLowerCase())).includes(String('baris')))) {
                randomcevap = ['bar???? kim?', 'f??rat kim?', 'katil bar????', 'bar???? ??ld??m???', 'kimle bar??????yim?'];
                s4dmessage.channel.send({
                    content: String((String(listsGetRandomItem(randomcevap, false))))
                });
            }
            if ((String(((s4dmessage.content).toLowerCase())).includes(String('savc??'))) || (String(((s4dmessage.content).toLowerCase())).includes(String('f??rat')))) {
                randomcevap = ['f??rat kar??s??n?? ??ld??rd?? as??l katil f??rat, y-yoksa bar????m?? ??ld??rd??? birisi bunu bana a????kalayabilirmi acaba?', 'f??ratla bar???? evlendi.', 'f??rat ??ok haval?? de??ilmi? ' + String(s4dmessage.author), 'f??rb??g', 'f??rbar', 'cumhuriyyet savc??s?? bar???? bulut', 'https://i.ytimg.com/vi/2ItW-afYoFM/hqdefault.jpg?sqp=-oaymwEcCOADEI4CSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCQIZ5o9jZ921lZ0lYB5MzI0OzAWg', 'ALLAHIM HAYIR'];
                s4dmessage.channel.send({
                    content: String((String(listsGetRandomItem(randomcevap, false))))
                });
            }
            if ((String(((s4dmessage.content).toLowerCase())).includes(String('b??ge'))) || (String(((s4dmessage.content).toLowerCase())).includes(String('buge')))) {
                randomcevap = ['m??ge', 'b??ge kim?', ':hearts: b??ge', 'barb??g', 'b??ge zahitin kar??s?? de??ilmi ya?', 'b??ge ka?? ya????nda?', 'savb??g', 'baget han??m', 'sbaghet han??m ', 'hacb??g', 'b??gsas', ':spaghetti: ', 'ben b??genin sevgilisi ' + String(s4dmessage.author), 'sen b??gemisin? ' + String(s4dmessage.author), 'b??genin ger??ek sevgilisi bar???? lan'];
                s4dmessage.channel.send({
                    content: String((String(listsGetRandomItem(randomcevap, false))))
                });
            }
            if ((String(((s4dmessage.content).toLowerCase())).includes(String('sinyor'))) || (String(((s4dmessage.content).toLowerCase())).includes(String('efkan')))) {
                randomcevap = ['sinyor i??ime siniyor', 'efkan??n da???? var', 'sinyorun s??z??n kesme tamamm???', 'sinyor :hearts: zahit', 'sinyor ??o??h ya??hu??u??lu ya', 'sinyor killed by rafi. Rafi has 1 kill', 'b??gEfka', 'YOKSA SENDEM?? KARTER??N ??YES??M??S??N LAN? ' + String(s4dmessage.author), 'sinyor sonunda ??ld??', 'sinyorun ad??n?? a??z??na alma sen! ' + String(s4dmessage.author), 'sinyor kim?', 'sinyor k??t?? birisimi anlatasana heyecanlan??yorum'];
                s4dmessage.channel.send({
                    content: String((String(listsGetRandomItem(randomcevap, false))))
                });
            }
            if ((String(((s4dmessage.content).toLowerCase())).includes(String('f??rbar'))) || (String(((s4dmessage.content).toLowerCase())).includes(String('barf??r'))) || (String(((s4dmessage.content).toLowerCase())).includes(String('barfir'))) || (String(((s4dmessage.content).toLowerCase())).includes(String('firbar')))) {
                randomcevap = ['evet evet EVET herzaman #f??rbar', 'bar???? ve f??rat evlenmeli bence', '??OK ??OK ??OK! f??rat ve bar???? shipi ba??l??yor..', 'buraya bir f??rbar emojisi koyal??m :barfir: ', 'f??rat ve bar???? birbirine ??ok yak??????yo????', 'bence zahf??r', 'yaz??k bar????a sasha ile bar???? daha iyi', 'bence f??r' + String((s4dmessage.author).username)];
                s4dmessage.channel.send({
                    content: String((String(listsGetRandomItem(randomcevap, false))))
                });
            }
            if ((String(((s4dmessage.content).toLowerCase())).includes(String('sava??'))) || (String(((s4dmessage.content).toLowerCase())).includes(String('savas')))) {
                randomcevap = ['kimle sava??im?', 'ben sava????m', 'sen kimsin?', 'iyi ??ocuk', 'sava?? nas??l biri anlatsana heyecanlan??yorum.', 'o kadar iyisinkii', 'sava?? ??ld??', 'sava?? b??geyi haketmiyo', 'sava?? b??geyi hakediyo', 'sava????n bavulu nerde', 'sava?? nerde?', 'https://media.discordapp.net/attachments/865202817887371274/1007766000378335262/unknown.png'];
                s4dmessage.channel.send({
                    content: String((String(listsGetRandomItem(randomcevap, false))))
                });
            }
            if (String(((s4dmessage.content).toLowerCase())).includes(String('tahir'))) {
                randomcevap = ['tahir benim a??k??m', 'tahir kim la?', 'ben tahirim', 'tahir b??genin kar??s?? de??ilmi ya?', 'tahir f??rat??n arkada???? dimi?', 'tahir isimli ki??ii dizide varm??yd?? ya? yoktu san??r??m, ha vard??.'];
                s4dmessage.channel.send({
                    content: String((String(listsGetRandomItem(randomcevap, false))))
                });
            }
            if (String(((s4dmessage.content).toLowerCase())).includes(String('sasha'))) {
                randomcevap = ['su??i', '??a??a', 'sasha kim?', ':sushi:', 'sasham?? dedin sen?', 'ben sashay??m'];
                s4dmessage.channel.send({
                    content: String((String(listsGetRandomItem(randomcevap, false))))
                });
            }
        }

    });

    s4d.client.on('interactionCreate', async (interaction) => {

    });

    s4d.Inviter.on('UserLeave', async function(member, uses, inviter, invite) {
        if (!((inviter) == null)) {
            if (!((inviter) == (member.user))) {
                s4d.client.channels.cache.get('992830450785595392').send({
                    content: String(([(member.user).username, ' sunucudan ayr??ld??, **', inviter, '** taraf??ndan davet edildi.'].join('')))
                });
            } else {
                s4d.client.channels.cache.get('992830450785595392').send({
                    content: String((String((member.user).username) + ' sunucudan ayr??ld??, kendi taraf??ndan davet edildi!'))
                });
            }
        } else {
            s4d.client.channels.cache.get('992830450785595392').send({
                content: String((String((member.user).username) + ' sunucudan ayr??ld??, onu davet eden ki??iy bulamad??m!'))
            });
        }

    });

    s4d.client.on('messageCreate', async (s4dmessage) => {
        if (s4dmessage.author.bot) {
            return;
        }
        if ((s4dmessage.channel) == s4d.client.channels.cache.get('1002998250355294429')) {
            if (s4d.database.get(String('KelimeDurum')) == true) {
                if ((s4dmessage.content).toLowerCase() == s4d.database.get(String('Kelime')).toLowerCase()) {
                    s4dmessage.reply({
                        content: String((['Tebrikler, ', s4dmessage.author, ', kelimeyi buldun!'].join(''))),
                        allowedMentions: {
                            repliedUser: true
                        }
                    });
                    s4d.database.set(String('KelimeDurum'), false);
                    s4d.client.channels.cache.get('1002998250355294429').permissionOverwrites.edit(((s4d.client.guilds.cache.get('986634992371236914')) || {}).id, {
                        SEND_MESSAGES: false
                    });
                }
            }
        }
        if ((s4dmessage.channel).type === "DM") {
            if ((s4dmessage.author) == (s4d.client.users.cache.get(String('589861038610972691')))) {
                if ((s4dmessage.content).toLowerCase() == 'kelime oyunu') {
                    if (!s4d.database.has(String('KelimeDurum'))) {
                        s4d.database.set(String('KelimeDurum'), false);
                    }
                    if (s4d.database.get(String('KelimeDurum')) == false) {
                        (s4dmessage.channel).send(String('Kelimeyi se??')).then(() => {
                            (s4dmessage.channel).awaitMessages({
                                filter: (m) => m.author.id === (s4dmessage.author).id,
                                time: (2 * 60 * 1000),
                                max: 1
                            }).then(async (collected) => {
                                s4d.reply = collected.first().content;
                                s4d.message = collected.first();
                                s4dmessage.channel.send({
                                    content: String('Kelime oyunu ba??lat??ld??!')
                                });
                                s4d.database.set(String('Kelime'), (s4d.reply));
                                s4d.database.set(String('KelimeDurum'), true);
                                s4d.client.channels.cache.get('1002998250355294429').send({
                                    content: String('> Oyun ba??lad??, kelimeyi ilk bulan kazan??r')
                                });
                                s4d.client.channels.cache.get('1002998250355294429').permissionOverwrites.edit(((s4d.client.guilds.cache.get('986634992371236914')) || {}).id, {
                                    SEND_MESSAGES: true
                                });
                                s4d.reply = null;
                            }).catch(async (e) => {
                                console.error(e);
                                s4dmessage.channel.send({
                                    content: String('Cevap vermedi??in i??in s??ren doldu!')
                                });
                            });
                        })
                    } else {
                        s4dmessage.channel.send({
                            content: String('Zaten mevcut bir kelime oyunu a????k!')
                        });
                    }
                }
            }
        }

    });

    return s4d
})();