module.exports = {
    name: 'schedule',
    description: 'Just a command to see the schedule.  ',
    async execute(client, message, args, Discord){
        if (args[0] === 'siege') {
            sundayval = 'siege';
            mondayval = 'siege';
            tuesdayval = 'siege';
            wednesdayval = 'siege';
            thursdayval = 'siege';
            fridayval = 'siege'
            saturdayval = 'siege';

            const scheduleEmbed = new Discord.MessageEmbed()
            .setTitle('Schedule')
            .setColor('#8210B6')
            .addFields(
                {name: 'Sunday', value: sundayval},
                {name: 'Monday', value: mondayval},
                {name: 'Tuesday', value: tuesdayval},
                {name: 'Wednesday', value: wednesdayval},
                {name: 'Thursday', value: thursdayval},
                {name: 'Friday', value: fridayval},
                {name: 'Saturday', value: saturdayval}
            )
            .setImage('https://i.imgur.com/ZTzFqlH.png')
            
            message.channel.send(scheduleEmbed);

            return;



        } if (args[0] === 'valorant') {           
            sundayval = 'val';
            mondayval = 'val';
            tuesdayval = 'val';
            wednesdayval = 'val';
            thursdayval = 'val';
            fridayval = 'val'
            saturdayval = 'val';



            const scheduleEmbed = new Discord.MessageEmbed()
        .setTitle('Schedule')
        .setColor('#8210B6')
        .addFields(
            {name: 'Sunday', value: sundayval},
            {name: 'Monday', value: mondayval},
            {name: 'Tuesday', value: tuesdayval},
            {name: 'Wednesday', value: wednesdayval},
            {name: 'Thursday', value: thursdayval},
            {name: 'Friday', value: fridayval},
            {name: 'Saturday', value: saturdayval}
        )
        .setImage('https://i.imgur.com/ZTzFqlH.png')
        
        message.channel.send(scheduleEmbed);



        return;


        } else {
            const scheduleerr = new Discord.MessageEmbed()
            .setColor('#8210B6')
            .setTitle('Error')
            .setDescription('Please provide a valid game with a schedule. (^schedule siege/valorant)')

            message.channel.send(scheduleerr);
            return;
        }
        
        
        
      
    }
}
