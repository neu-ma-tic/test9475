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

import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.EventPriority;
import org.bukkit.event.Listener;
import org.bukkit.event.entity.PlayerDeathEvent;
import org.bukkit.event.player.AsyncPlayerChatEvent;
import org.bukkit.event.player.PlayerJoinEvent;
import org.bukkit.event.player.PlayerQuitEvent;

import io.github.lxgaming.discordbot.DiscordBotCore;
import io.github.lxgaming.discordbot.entries.Message;

public class PlayerListener implements Listener {
	
	@EventHandler(priority = EventPriority.MONITOR)
	public void onPlayerChat(AsyncPlayerChatEvent event) {
		if (event.isCancelled() && !DiscordBotCore.getInstance().getConfiguration().isForceChat()) {
			return;
		}
		
		Player player = event.getPlayer();
		String permission = DiscordBotCore.getInstance().getConfiguration().getChannels().get("Global").getPermission();
		boolean hasPermission = false;
		
		if (permission == null || permission.trim().equals("") || permission.trim().equals("null")) {
			hasPermission = false;
		} else if (permission.equals("*") || player.hasPermission(permission)) {
			hasPermission = true;
		}
		
		if (!DiscordBotCore.getInstance().getConfiguration().isPlayerChat() || !hasPermission || DiscordBotCore.getInstance().getDatabaseManager().checkDatabase(player.getUniqueId())) {
			return;
		}
		
		Message message = new Message()
				.setChannel(DiscordBotCore.getInstance().getConfiguration().getChannels().get("Global").getChannel())
				.setFormat(DiscordBotCore.getInstance().getConfiguration().getChannelFormat().get("Global"))
				.setName(player.getName())
				.setNick(player.getDisplayName())
				.setServer("Unknown")
				.setMessage(event.getMessage())
				.setDiscord(true)
				.setMinecraft(false)
				.setConsole(false)
				.setRedis(false);
		
		if (player.getServer() != null && player.getServer().getName() != null) {
			message.setServer(player.getServer().getName());
		}
		
		DiscordBotCore.getInstance().getMessageSender().sendMessage(message);
		return;
	}
	
	@EventHandler(priority = EventPriority.MONITOR)
	public void onPlayerJoin(PlayerJoinEvent event) {
		if (!DiscordBotCore.getInstance().getConfiguration().isPlayerJoin() || event.getPlayer().hasPermission("DiscordBot.Silent")) {
			return;
		}
		
		Message message = new Message()
				.setChannel(DiscordBotCore.getInstance().getConfiguration().getChannels().get("InGame").getChannel())
				.setFormat(DiscordBotCore.getInstance().getConfiguration().getChannelFormat().get("InGame"))
				.setName(event.getPlayer().getName())
				.setNick(event.getPlayer().getDisplayName())
				.setServer("Unknown")
				.setMessage("Joined")
				.setDiscord(true)
				.setMinecraft(false)
				.setConsole(false)
				.setRedis(false);
		
		if (event.getPlayer().getServer() != null && event.getPlayer().getServer().getName() != null) {
			message.setServer(event.getPlayer().getServer().getName());
		}
		
		DiscordBotCore.getInstance().getMessageSender().sendMessage(message);
		return;
	}
	
	@EventHandler(priority = EventPriority.MONITOR)
	public void onPlayerDeath(PlayerDeathEvent event) {
		if (!DiscordBotCore.getInstance().getConfiguration().isPlayerDeath() || event.getEntity().hasPermission("DiscordBot.Silent")) {
			return;
		}
		
		Message message = new Message()
				.setChannel(DiscordBotCore.getInstance().getConfiguration().getChannels().get("InGame").getChannel())
				.setFormat(DiscordBotCore.getInstance().getConfiguration().getChannelFormat().get("InGame"))
				.setName(event.getEntity().getName())
				.setNick(event.getEntity().getDisplayName())
				.setServer("Unknown")
				.setMessage(event.getDeathMessage())
				.setDiscord(true)
				.setMinecraft(false)
				.setConsole(false)
				.setRedis(false);
		
		if (event.getEntity().getServer() != null && event.getEntity().getServer().getName() != null) {
			message.setServer(event.getEntity().getServer().getName());
		}
		
		DiscordBotCore.getInstance().getMessageSender().sendMessage(message);
		return;
	}
	
	@EventHandler(priority = EventPriority.MONITOR)
	public void onPlayerQuit(PlayerQuitEvent event) {
		if (!DiscordBotCore.getInstance().getConfiguration().isPlayerQuit() || event.getPlayer().hasPermission("DiscordBot.Silent")) {
			return;
		}
		
		Message message = new Message()
				.setChannel(DiscordBotCore.getInstance().getConfiguration().getChannels().get("InGame").getChannel())
				.setFormat(DiscordBotCore.getInstance().getConfiguration().getChannelFormat().get("InGame"))
				.setName(event.getPlayer().getName())
				.setNick(event.getPlayer().getDisplayName())
				.setServer("Unknown")
				.setMessage("Quit")
				.setDiscord(true)
				.setMinecraft(false)
				.setConsole(false)
				.setRedis(false);
		
		if (event.getPlayer().getServer() != null && event.getPlayer().getServer().getName() != null) {
			message.setServer(event.getPlayer().getServer().getName());
		}
		
		DiscordBotCore.getInstance().getMessageSender().sendMessage(message);
		return;
	}
}