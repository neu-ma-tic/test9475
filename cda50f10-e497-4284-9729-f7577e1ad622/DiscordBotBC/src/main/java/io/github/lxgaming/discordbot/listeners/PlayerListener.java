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

package io.github.lxgaming.discordbot.listeners;

import io.github.lxgaming.discordbot.DiscordBotCore;
import io.github.lxgaming.discordbot.entries.Message;
import net.md_5.bungee.api.connection.ProxiedPlayer;
import net.md_5.bungee.api.event.ChatEvent;
import net.md_5.bungee.api.event.PlayerDisconnectEvent;
import net.md_5.bungee.api.event.PostLoginEvent;
import net.md_5.bungee.api.plugin.Listener;
import net.md_5.bungee.event.EventHandler;
import net.md_5.bungee.event.EventPriority;

public class PlayerListener implements Listener {
	
	@EventHandler(priority = EventPriority.HIGHEST)
	public void onPlayerChat(ChatEvent event) {
		if (event.isCommand() || event.getSender() == null) {
			return;
		}
		
		if (event.isCancelled() && !DiscordBotCore.getInstance().getConfiguration().isForceChat()) {
			return;
		}
		
		ProxiedPlayer proxiedPlayer = (ProxiedPlayer) event.getSender();
		String permission = DiscordBotCore.getInstance().getConfiguration().getChannels().get("Global").getPermission();
		boolean hasPermission = false;
		
		if (permission == null || permission.trim().equals("") || permission.trim().equals("null")) {
			hasPermission = false;
		} else if (permission.equals("*") || proxiedPlayer.hasPermission(permission)) {
			hasPermission = true;
		}
		
		if (!DiscordBotCore.getInstance().getConfiguration().isPlayerChat() || !hasPermission || DiscordBotCore.getInstance().getDatabaseManager().checkDatabase(proxiedPlayer.getUniqueId())) {
			return;
		}
		
		Message message = new Message()
				.setChannel(DiscordBotCore.getInstance().getConfiguration().getChannels().get("Global").getChannel())
				.setFormat(DiscordBotCore.getInstance().getConfiguration().getChannelFormat().get("Global"))
				.setName(proxiedPlayer.getName())
				.setNick(proxiedPlayer.getDisplayName())
				.setServer("Unknown")
				.setMessage(event.getMessage())
				.setDiscord(true)
				.setMinecraft(false)
				.setConsole(false)
				.setRedis(false);
		
		if (proxiedPlayer.getServer() != null && proxiedPlayer.getServer().getInfo() != null) {
			message.setServer(proxiedPlayer.getServer().getInfo().getName());
		}
		
		DiscordBotCore.getInstance().getMessageSender().sendMessage(message);
		return;
	}
	
	@EventHandler(priority = EventPriority.HIGHEST)
	public void onPostLogin(PostLoginEvent event) {
		if (event.getPlayer() == null) {
			return;
		}
		
		if (!DiscordBotCore.getInstance().getConfiguration().isPlayerJoin() || event.getPlayer().hasPermission("DiscordBot.Silent")) {
			return;
		}
		
		Message message = new Message()
				.setChannel(DiscordBotCore.getInstance().getConfiguration().getChannels().get("Global").getChannel())
				.setFormat(DiscordBotCore.getInstance().getConfiguration().getPlayerFormat().get("Join"))
				.setName(event.getPlayer().getName())
				.setNick(event.getPlayer().getDisplayName())
				.setServer("Unknown")
				.setMessage("Joined")
				.setDiscord(true)
				.setMinecraft(false)	
				.setConsole(false)
				.setRedis(false);
		
		if (event.getPlayer().getServer() != null && event.getPlayer().getServer().getInfo() != null) {
			message.setServer(event.getPlayer().getServer().getInfo().getName());
		}
		
		DiscordBotCore.getInstance().getMessageSender().sendMessage(message);
		return;
	}
	
	//EventPriority is on Lowest due to LuckPerms unloading player data which causes permissions to be null.
	@EventHandler(priority = EventPriority.LOWEST)
	public void onPlayerDisconnect(PlayerDisconnectEvent event) {
		if (!DiscordBotCore.getInstance().getConfiguration().isPlayerQuit() || event.getPlayer().hasPermission("DiscordBot.Silent")) {
			return;
		}
		
		Message message = new Message()
				.setChannel(DiscordBotCore.getInstance().getConfiguration().getChannels().get("Global").getChannel())
				.setFormat(DiscordBotCore.getInstance().getConfiguration().getPlayerFormat().get("Quit"))
				.setName(event.getPlayer().getName())
				.setNick(event.getPlayer().getDisplayName())
				.setServer("Unknown")
				.setMessage("Quit")
				.setDiscord(true)
				.setMinecraft(false)
				.setConsole(false)
				.setRedis(false);
		
		if (event.getPlayer().getServer() != null && event.getPlayer().getServer().getInfo() != null) {
			message.setServer(event.getPlayer().getServer().getInfo().getName());
		}
		
		DiscordBotCore.getInstance().getMessageSender().sendMessage(message);
		return;
	}
}