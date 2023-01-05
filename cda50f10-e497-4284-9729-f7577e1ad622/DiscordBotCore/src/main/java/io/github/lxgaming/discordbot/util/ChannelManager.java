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

package io.github.lxgaming.discordbot.util;

import java.util.Iterator;
import java.util.Map.Entry;

import io.github.lxgaming.discordbot.DiscordBotCore;
import io.github.lxgaming.discordbot.entries.Channel;
import net.dv8tion.jda.core.entities.Guild;

public class ChannelManager {
	
	public void setupChannels() {
		for (Iterator<Entry<String, Channel>> iterator = DiscordBotCore.getInstance().getConfiguration().getChannels().entrySet().iterator(); iterator.hasNext();) {
			Entry<String, Channel> entry = iterator.next();
			String channelId = entry.getValue().getChannel();
			
			if (channelId == null || channelId.equalsIgnoreCase("") || channelId.equalsIgnoreCase("null")) {
				DiscordBotCore.getInstance().getLogger().warning("Channel not set for '" + entry.getKey() + "'!");
				continue;
			}
			
			if (!channelId.matches("[0-9]+")) {
				if (DiscordBotCore.getInstance().getJDA().getTextChannelsByName(channelId, false).isEmpty()) {
					DiscordBotCore.getInstance().getLogger().warning("Could not find TextChannel with name of '" + channelId + "'!");
					DiscordBotCore.getInstance().getLogger().warning("Please make sure the bot has permissions to view this channel!");
					continue;
				}
				
				DiscordBotCore.getInstance().getConfiguration().getChannels().get(entry.getKey()).setChannel(DiscordBotCore.getInstance().getJDA().getTextChannelsByName(channelId, false).get(0).getId());
			}
			
			if (DiscordBotCore.getInstance().getJDA().getTextChannelById(channelId) == null) {
				DiscordBotCore.getInstance().getLogger().warning("Could not find TextChannel with Id of '" + channelId + "'!");
				DiscordBotCore.getInstance().getLogger().info("List of available TextChannels " + DiscordBotCore.getInstance().getJDA().getTextChannels());
				continue;
			}
			
			String permission = entry.getValue().getPermission();
			String[] commands = entry.getValue().getCommand().replace(" ", "").split(",");
			
			DiscordBotCore.getInstance().getEventManager().onCommandRegister(entry.getKey(), commands[0], permission, commands);
			DiscordBotCore.getInstance().getLogger().info("Registered channel '" + entry.getKey() + "'.");
		}
		return;
	}
	
	public Guild getGuild() {
		String guildId = DiscordBotCore.getInstance().getConfiguration().getGuildId();
		if (guildId == null || guildId.trim().equals("") || guildId.equals("null")) {
			guildId = DiscordBotCore.getInstance().getJDA().getGuilds().get(0).getId();
		}
		
		if (!guildId.matches("[0-9]+") && !DiscordBotCore.getInstance().getJDA().getGuildsByName(guildId, false).isEmpty()) {
			guildId = DiscordBotCore.getInstance().getJDA().getGuildsByName(guildId, false).get(0).getId();
		}
		
		if (DiscordBotCore.getInstance().getJDA().getGuildById(guildId) != null) {
			DiscordBotCore.getInstance().getConfiguration().setGuildId(guildId);
			return DiscordBotCore.getInstance().getJDA().getGuildById(guildId);
		}
		
		DiscordBotCore.getInstance().getLogger().warning("Unable to get Guild Id!");
		return null;
	}
	
	public Channel getChannel(String string) {
		if (!string.matches("[0-9]+")) {
			return DiscordBotCore.getInstance().getConfiguration().getChannels().get(string);
		}
		
		for (Iterator<Entry<String, Channel>> iterator = DiscordBotCore.getInstance().getConfiguration().getChannels().entrySet().iterator(); iterator.hasNext();) {
			Entry<String, Channel> entry = iterator.next();
			
			if (entry.getValue().getChannel().equals(string)) {
				return entry.getValue();
			}
		}
		return null;
	}
	
	public String getChannelId(String name) {
		if (DiscordBotCore.getInstance().getConfiguration().getChannels().containsKey(name)) {
			return DiscordBotCore.getInstance().getConfiguration().getChannels().get(name).getChannel();
		}
		return null;
	}
	
	public String getChannelName(String id) {
		for (Iterator<Entry<String, Channel>> iterator = DiscordBotCore.getInstance().getConfiguration().getChannels().entrySet().iterator(); iterator.hasNext();) {
			Entry<String, Channel> entry = iterator.next();
			
			if (entry.getValue().getChannel().equals(id)) {
				return entry.getKey();
			}
		}
		return null;
	}
}