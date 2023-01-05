/*
 * Copyright 2017 Alex Thomson
 * 
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 * http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package io.github.lxgaming.discordbot.commands;

import org.bukkit.ChatColor;
import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;

import io.github.lxgaming.discordbot.DiscordBot;
import io.github.lxgaming.discordbot.DiscordBotCore;
import io.github.lxgaming.discordbot.entries.Message;

public class DiscordChatCommand implements CommandExecutor {
	
	private final String name;
	private final String permission;
	
	public DiscordChatCommand(String name, String command, String permission, String[] aliases) {
		this.name = name;
		this.permission = permission;
		DiscordBot.getInstance().getCommandManager().registerCommand(aliases);
	}
	
	public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {
		if (!sender.hasPermission(this.permission)) {
			sender.sendMessage(ChatColor.RED + "You do not have permission!");
			return true;
		}
		
		StringBuilder stringBuilder = new StringBuilder();
		for (String arg : args) {
			stringBuilder.append(arg + " ");
		}
		
		if (stringBuilder.toString().trim().length() == 0) {
			sender.sendMessage(ChatColor.RED + "Message cannot be blank!");
			return true;
		}
		
		Message message = new Message()
				.setChannel(DiscordBotCore.getInstance().getConfiguration().getChannels().get(this.name).getChannel())
				.setFormat(DiscordBotCore.getInstance().getConfiguration().getChannelFormat().get(this.name))
				.setName(sender.getName())
				.setNick("")
				.setServer("Unknown")
				.setMessage(stringBuilder.toString().trim())
				.setDiscord(true)
				.setMinecraft(true)
				.setConsole(true)
				.setRedis(true);
		
		if (sender instanceof Player) {
			Player player = (Player) sender;
			
			if (DiscordBotCore.getInstance().getDatabaseManager().checkDatabase(player.getUniqueId())) {
				player.sendMessage(ChatColor.RED + "DiscordChat disabled. '/DiscordBot Toggle' to enable");
				return true;
			}
			
			message.setName(player.getName()).setNick(player.getDisplayName());
			
			if (player.getServer() != null && player.getServer().getName() != null) {
				message.setServer(player.getServer().getName());
			}
		}
		
		DiscordBotCore.getInstance().getMessageSender().sendMessage(message);
		return true;
	}
}
