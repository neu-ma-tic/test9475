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

import io.github.lxgaming.discordbot.DiscordBotCore;
import io.github.lxgaming.discordbot.entries.Message;
import net.md_5.bungee.api.ChatColor;
import net.md_5.bungee.api.CommandSender;
import net.md_5.bungee.api.chat.ComponentBuilder;
import net.md_5.bungee.api.connection.ProxiedPlayer;
import net.md_5.bungee.api.plugin.Command;

public class DiscordChatCommand extends Command {
	
	private final String name;
	
	public DiscordChatCommand(String name, String command, String permission, String[] aliases) {
		super(command, permission, aliases);
		this.name = name;
	}
	
	@Override
	public void execute(CommandSender sender, String[] args) {
		StringBuilder stringBuilder = new StringBuilder();
		for (String arg : args) {
			stringBuilder.append(arg + " ");
		}
		
		if (stringBuilder.toString().trim().length() == 0) {
			sender.sendMessage(new ComponentBuilder("Message cannot be blank!").color(ChatColor.RED).create());
			return;
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
		
		if (sender instanceof ProxiedPlayer) {
			ProxiedPlayer player = (ProxiedPlayer) sender;
			
			if (DiscordBotCore.getInstance().getDatabaseManager().checkDatabase(player.getUniqueId())) {
				player.sendMessage(new ComponentBuilder("DiscordChat disabled. '/DiscordBot Toggle' to enable").color(ChatColor.RED).create());
				return;
			}
			
			message.setName(player.getName()).setNick(player.getDisplayName());
			
			if (player.getServer() != null && player.getServer().getInfo() != null) {
				message.setServer(player.getServer().getInfo().getName());
			}
		}
		
		DiscordBotCore.getInstance().getMessageSender().sendMessage(message);
	}
}