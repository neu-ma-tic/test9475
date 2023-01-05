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

import org.bukkit.entity.Player;

import io.github.lxgaming.discordbot.DiscordBot;
import io.github.lxgaming.discordbot.DiscordBotCore;
import io.github.lxgaming.discordbot.commands.DiscordChatCommand;
import io.github.lxgaming.discordbot.entries.AbstractDiscordBotListener;
import io.github.lxgaming.discordbot.entries.Message;

public class DiscordBotListener extends AbstractDiscordBotListener {
	
	@Override
	public void onMessageMinecraft(Message message) {		
		for (Iterator<? extends Player> iterator = DiscordBot.getInstance().getServer().getOnlinePlayers().iterator(); iterator.hasNext();) {
			Player player = iterator.next();
			
			if (DiscordBotCore.getInstance().getDatabaseManager().checkDatabase(player.getUniqueId())) {
				return;
			}
			
			if (message.getData().get("Permission").equals("*") || player.hasPermission(message.getData().get("Permission"))) {
				player.sendMessage(message.getMessage());
			}
		}
		return;
	}
	
	@Override
	public void onCommandRegister(String name, String command, String permission, String... aliases) {
		new DiscordChatCommand(name, command, permission, aliases);
		return;
	}
	
	@Override
	public void onDatabaseUpdate() {
		return;
	}
}