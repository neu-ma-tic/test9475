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

import io.github.lxgaming.discordbot.DiscordBot;
import io.github.lxgaming.discordbot.DiscordBotCore;
import net.md_5.bungee.api.ChatColor;
import net.md_5.bungee.api.CommandSender;
import net.md_5.bungee.api.chat.ComponentBuilder;
import net.md_5.bungee.api.connection.ProxiedPlayer;
import net.md_5.bungee.api.plugin.Command;

public class DiscordBotCommand extends Command {
	
	public DiscordBotCommand() {
		super("discordbot");
	}
	
	@Override
	public void execute(CommandSender sender, String[] args) {
		if (args.length == 0) {
			sender.sendMessage(new ComponentBuilder("===== ").color(ChatColor.GOLD).append("DiscordBot - Bungeecord Edition").color(ChatColor.GREEN).append(" =====").color(ChatColor.GOLD).create());
			sender.sendMessage(new ComponentBuilder("Version - ").color(ChatColor.GOLD).append(DiscordBotCore.getInstance().getConfiguration().getDiscordBotVersion()).color(ChatColor.AQUA).create());
			sender.sendMessage(new ComponentBuilder("JDA - ").color(ChatColor.GOLD).append(DiscordBotCore.getInstance().getConfiguration().getJDAVersion()).color(ChatColor.AQUA).create());
			sender.sendMessage(new ComponentBuilder("Author - ").color(ChatColor.GOLD).append("LX_Gaming").color(ChatColor.AQUA).create());
			return;
		}
		
		if (args.length == 1 && args[0].equalsIgnoreCase("reload") && sender.hasPermission("DiscordBot.Reload")) {
			DiscordBot.getInstance().reloadDiscordBot();
			sender.sendMessage(new ComponentBuilder("DiscordBot reloaded.").color(ChatColor.GREEN).create());
			return;
		}
		
		if (!(sender instanceof ProxiedPlayer)) {
			sender.sendMessage(new ComponentBuilder("Command cannot be run from Console").color(ChatColor.RED).create());
			return;
		}
		
		ProxiedPlayer proxiedPlayer = (ProxiedPlayer) sender;
		if (args.length == 1 && (args[0].equalsIgnoreCase("toggle") || args[0].equalsIgnoreCase("t")) && proxiedPlayer.hasPermission("DiscordBot.Toggle")) {
			DiscordBotCore.getInstance().getDatabaseManager().togglePlayerDatabase(proxiedPlayer.getUniqueId());
		}
	}
}