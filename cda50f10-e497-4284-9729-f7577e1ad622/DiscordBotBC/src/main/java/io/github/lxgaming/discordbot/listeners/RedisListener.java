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

import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.JsonParser;
import com.imaginarycode.minecraft.redisbungee.events.PubSubMessageEvent;

import io.github.lxgaming.discordbot.DiscordBot;
import io.github.lxgaming.discordbot.DiscordBotCore;
import io.github.lxgaming.discordbot.entries.Message;
import net.md_5.bungee.api.plugin.Listener;

public class RedisListener implements Listener {
	
	public void onMessage(PubSubMessageEvent event) {
		try {
			if (!event.getChannel().equals("DiscordBot")) {
				return;
			}
			
			JsonObject jsonObject = new JsonParser().parse(event.getMessage()).getAsJsonObject();
			if (jsonObject == null || !jsonObject.has("format") || !jsonObject.has("name") || !jsonObject.has("nick") || !jsonObject.has("server") || !jsonObject.has("message")) {
				throw new IllegalArgumentException();
			}
			
			DiscordBotCore.getInstance().getMessageSender().sendMessage(new Message()
					.setFormat(DiscordBotCore.getInstance().getConfiguration().getPlayerFormat().get(jsonObject.get("format").getAsString()))
					.setName(jsonObject.get("name").getAsString())
					.setNick(jsonObject.get("nick").getAsString())
					.setServer(jsonObject.get("server").getAsString())
					.setMessage(jsonObject.get("message").getAsString())
					.setDiscord(false)
					.setMinecraft(true)
					.setConsole(false)
					.setRedis(false));
		} catch (IllegalArgumentException | JsonParseException ex) {
			DiscordBot.getInstance().getLogger().warning("Exception reading redis message!");
			ex.printStackTrace();
		}
		return;
	}
}