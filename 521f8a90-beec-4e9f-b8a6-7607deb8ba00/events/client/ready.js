module.exports = (Discord, client) => {
    console.log('Genshin Server Bot is now online!');

    client.user.setActivity('Prefix set to +', {type: 'PLAYING'})
    .then(presence => console.log(`Activity set to ${presence.activities[0].name}`))
    .catch(console.error);
}