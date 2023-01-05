module.exports ={
    commands: ['clear', 'purge', 'nuke'], // You Can Keep Any Name
    permissions: 'ADMINISTRATOR', // You Can Keep Any Permission
    permissionError: 'You Cant Use It', 
    description: 'Deletes Message', //Optional
    callback: (message, args) => {
        message.delete()
        const amount = parseInt(args[0]) + 1;

        if (isNaN(amount)) {
            return message.channel.send('Musíte zadat 1-99.')
            .then(msg => {
                msg.delete({ timeout: 10000 });
            })
    .catch();
        } else if (amount <= 1 || amount > 100) {
            return message.channel.send('Můžete smazat jen 1 až 99.')
            .then(msg => {
                msg.delete({ timeout: 10000 });
            })
    .catch();
        }

        message.channel.bulkDelete(amount, true).catch(err => {
            console.error(err);
            message.channel.send('Došlo k chybě při mazání zpráv.')
            .then(msg => {
                msg.delete({ timeout: 10000 });
            })
    .catch();
        })
    }
}