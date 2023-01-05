const { MessageEmbed, Collection } = require('discord.js');
const settings = require('../../assets/settings.json');

module.exports.run = async (client, interaction) => {
    let member = interaction.member;
    let guild = interaction.guild;

    if (interaction.isCommand()) {
        const command = client.slashCommands.get(interaction.commandName);
        if(!command) {
            return interaction.reply({embeds: [
                new MessageEmbed()
                    .setColor('RED')
                    .setDescription('⛔ An error occured while running this command!')
            ], ephemeral: true }) && client.slashCommands.delete(interaction.commandName);
        } else {
            if (!client.cooldowns.has(command.name)) {
                client.cooldowns.set(command.name, new Collection());
            }
            const now = Date.now();
            const timestamps = client.cooldowns.set(command.name);
            const cdAmount = command.cooldown;
            
            if (timestamps.has(member.id)) {
                const expirationTime = timestamps.get(member.id) + cdAmount;
                if (now < expirationTime) {
                    const timeLeft = (expirationTime - now) / 1000;
                    let coolDown = new MessageEmbed()
                        .setColor(client.color.errorcolor)
                        .setTitle('Cooldown!')
                        .setDescription(`You need to wait **${timeLeft.toFixed(2)}** seconds!`)
                    return interaction.reply({ embeds: [coolDown], ephemeral: true });
                }
            } else {
                timestamps.set(member.id, now);
                setTimeout(() => timestamps.delete(member.id), cdAmount);
            
                neededPermissions = [];
                command.userPermissions.forEach((perm) => {
                    if (!interaction.channel.permissionsFor(member).has(perm)) neededPermissions.push(perm);
                });
            
                if (neededPermissions.length > 0) {
                    let noPerms = new MessageEmbed()
                        .setColor(client.color.errorcolor)
                        .setTitle('No Permission')
                        .setDescription(`You need the following permissions: \`${neededPermissions.join(', ')}\``)
                    return interaction.reply({ embeds: [noPerms], ephemeral: true });
                } else {
                    try {
                        const options = interaction.options;
                        command.run(interaction, options);
                    } catch (err) {
                        client.logger.error(`An error occurred when trying to run a Interaction\n\n${err}`);
                        return interaction.reply({embeds: [
                            new MessageEmbed()
                                .setColor('RED')
                                .setDescription('⛔ An error occured while running this command!')
                        ], ephemeral: true })
                    }
                    return;
                }
            }
        }
    } else if(interaction.isButton()){ 
        if(interaction.channel.id === settings.verify_ID){
            if(interaction.customId === 'verification'){
                let guestRole = guild.roles.cache.get(settings.guest_ID)
                if(guestRole) { 
                    if(member.roles.cache.has(settings.guest_ID)){ 
                        let embed = new MessageEmbed()
                            .setColor(client.colors.errorcolor)
                            .setDescription(`❌ **You already passed  the verification process! ${member}**`)
                        return interaction.reply({ embeds: [embed],  ephemeral: true })
                    } else {
                        member.roles.add(guestRole)
                        let embed = new MessageEmbed()
                            .setColor(client.colors.succescolor)
                            .setDescription(`✅ **You have succesfully been verified! ${member}**`)
                        return interaction.reply({ embeds: [embed],  ephemeral: true })
                    }
                }
            }
        }
    } else if(interaction.isSelectMenu()){
        if(interaction.channel.id === settings.roles_ID){
            if(interaction.customId === 'color-roles'){
                let role = guild.roles.cache.get(interaction.values[0])
                if(role) {
                    for(let i = 0; i < settings.color_roles.length; i++){
                        if(member.roles.cache.has(settings.color_roles[i])){
                            member.roles.remove(settings.color_roles[i])
                        }
                    }
                    member.roles.add(role)
                    let embed = new MessageEmbed()
                        .setColor(client.colors.succescolor)
                        .setDescription(`✅ **You have succesfully __recieved__ ${role}!**`)
                    return interaction.reply({ embeds: [embed],  ephemeral: true })
                }
            } else if(interaction.customId === 'discord-pings'){ 
                let role = guild.roles.cache.get(interaction.values[0])
                if(role) {
                    if(!member.roles.cache.has(role.id)){ 
                        member.roles.add(role)
                        let embed = new MessageEmbed()
                            .setColor(client.colors.succescolor)
                            .setDescription(`✅ **You have succesfully __recieved__ ${role}!**`)
                        return interaction.reply({ embeds: [embed],  ephemeral: true })
                    } else {
                        member.roles.remove(role)
                        let embed = new MessageEmbed()
                            .setColor(client.colors.succescolor)
                            .setDescription(`✅ **You have succesfully __removed__ ${role}!**`)
                        return interaction.reply({ embeds: [embed],  ephemeral: true })
                    }
                }
            } else if(interaction.customId === 'polygon-ranks'){  
                let role = guild.roles.cache.get(interaction.values[0])
                if(role) {
                    for(let i = 0; i < settings.level_roles.length; i++){
                        if(member.roles.cache.has(settings.level_roles[i])){
                            member.roles.remove(settings.level_roles[i])
                        }
                    }
                    member.roles.add(role)
                    let embed = new MessageEmbed()
                        .setColor(client.colors.succescolor)
                        .setDescription(`✅ **You have succesfully __recieved__ ${role}!**`)
                    return interaction.reply({ embeds: [embed],  ephemeral: true })
                }
            } else if(interaction.customId === 'region-roles'){  
                let role = guild.roles.cache.get(interaction.values[0])
                if(role) {
                    for(let i = 0; i < settings.region_roles.length; i++){
                        if(member.roles.cache.has(settings.region_roles[i])){
                            member.roles.remove(settings.region_roles[i])
                        }
                    }
                    member.roles.add(role)
                    let embed = new MessageEmbed()
                        .setColor(client.colors.succescolor)
                        .setDescription(`✅ **You have succesfully __recieved__ ${role}!**`)
                    return interaction.reply({ embeds: [embed],  ephemeral: true })
                }
            }
        }
    }
    return;
}