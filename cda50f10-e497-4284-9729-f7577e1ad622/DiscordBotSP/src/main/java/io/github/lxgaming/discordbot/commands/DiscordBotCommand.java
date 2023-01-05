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

public class DiscordBotCommand implements CommandExecutor {
	
	public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {
		if (!cmd.getName().equalsIgnoreCase("discordbot")) {
			return false;
		}
		
		if (args.length == 0) {
			sender.sendMessage(ChatColor.GOLD + "===== " + ChatColor.GREEN + "DiscordBot - Spigot Edition" + ChatColor.GOLD + " ===== ");
			sender.sendMessage(ChatColor.GOLD + "Version - " + ChatColor.AQUA + DiscordBotCore.getInstance().getConfiguration().getDiscordBotVersion());
			sender.sendMessage(ChatColor.GOLD + "API - " + ChatColor.AQUA + DiscordBotCore.getInstance().getConfiguration().getJDAVersion());
			sender.sendMessage(ChatColor.GOLD + "Author - " + ChatColor.AQUA + "LX_Gaming");
			return true;
		}
		
		if (args.length == 1 && args[0].equalsIgnoreCase("reload") && sender.hasPermission("DiscordBot.Reload")) {
			DiscordBot.getInstance().reloadDiscordBot();
			sender.sendMessage(ChatColor.GREEN + "Reload Config.");
			return true;
		}
		
		if (!(sender instanceof Player)) {
			sender.sendMessage(ChatColor.RED + "Command cannot be run from Console!");
			return true;
		}
		
		Player player = (Player) sender;
		if (args.length == 1 && (args[0].equalsIgnoreCase("toggle") || args[0].equalsIgnoreCase("t")) && player.hasPermission("DiscordBot.Toggle")) {
			DiscordBotCore.getInstance().getDatabaseManager().togglePlayerDatabase(player.getUniqueId());
			return true;
		}
		return false;
	}
}