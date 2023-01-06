const { PREFIX } = process.env;

module.exports = (client) => {
  setInterval(() => {
    let members = 0;
    for(const guild of client.guilds.cache){
      members+=guild[1].memberCount
    }
    client.user.setActivity(`${members} users`,{ type: 'WATCHING' });
      
    }, 1000);

    client.user.setStatus('online');

    console.log(`${client.user.tag} ready to use!`);
};