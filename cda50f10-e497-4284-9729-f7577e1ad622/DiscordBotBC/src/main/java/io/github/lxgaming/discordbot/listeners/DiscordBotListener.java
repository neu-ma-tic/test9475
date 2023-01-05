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

import java.util.Iterator;

import com.google.gson.Gson;
import com.google.gson.JsonObject;

import io.github.lxgaming.discordbot.DiscordBot;
import io.github.lxgaming.discordbot.DiscordBotCore;
import io.github.lxgaming.discordbot.commands.DiscordChatCommand;
import io.github.lxgaming.discordbot.entries.AbstractDiscordBotListener;
import io.github.lxgaming.discordbot.entries.Message;
import net.md_5.bungee.api.ProxyServer;
import net.md_5.bungee.api.chat.ComponentBuilder;
import net.md_5.bungee.api.connection.ProxiedPlayer;

public class DiscordBotListener extends AbstractDiscordBotListener {
	
	@Override
	public void onMessageMinecraft(Message message) {
		if (message.sendRedis() && DiscordBot.getInstance().getRedisBungee() != null) {
			JsonObject jsonObject = new JsonObject();
			jsonObject.addProperty("message", message.getMessage());
			jsonObject.addProperty("permission", message.getData().get("Permission"));
			DiscordBot.getInstance().getRedisBungee().sendChannelMessage("DiscordBot", new Gson().toJson(jsonObject));
		}
		
		
		for (Iterator<ProxiedPlayer> iterator = ProxyServer.getInstance().getPlayers().iterator(); iterator.hasNext();) {
			ProxiedPlayer proxiedPlayer = iterator.next();
			
			if (DiscordBotCore.getInstance().getDatabaseManager().checkDatabase(proxiedPlayer.getUniqueId())) {
				return;
			}
			
			if (message.getData().get("Permission").equals("*") || proxiedPlayer.hasPermission(message.getData().get("Permission"))) {
				proxiedPlayer.sendMessage(new ComponentBuilder(message.getMessage()).create());
			}
		}
		return;
	}
	
	@Override
	public void onCommandRegister(String channel, String command, String permission, String... aliases) {
		DiscordBot.getInstance().getProxy().getPluginManager().registerCommand(DiscordBot.getInstance(), new DiscordChatCommand(channel, command, permission, aliases));
		return;
	}
	
	@Override
	public void onCommandReceived(Message message) {
		if (message.getMessage().equals("list")) {
			StringBuilder stringBuilder = new StringBuilder();
			
			for (ProxiedPlayer proxiedPlayer : ProxyServer.getInstance().getPlayers()) {
				stringBuilder.append(proxiedPlayer.getName() + ", ");
			}
			
			if (stringBuilder.toString().endsWith(", ")) {
				stringBuilder.delete(stringBuilder.length() - 2, stringBuilder.length());
			}
			DiscordBotCore.getInstance().getMessageSender().sendMessage(message.setMessage(stringBuilder.toString()));
		}
		return;
	}
	
	@Override
	public void onDatabaseUpdate() {
		DiscordBot.getInstance().getConfiguration().getDatabase().set("DiscordBot.Database", DiscordBotCore.getInstance().getConfiguration().getDatabase());
		DiscordBot.getInstance().getConfiguration().saveFile("database.yml", DiscordBot.getInstance().getConfiguration().getDatabase());
		return;
	}
}