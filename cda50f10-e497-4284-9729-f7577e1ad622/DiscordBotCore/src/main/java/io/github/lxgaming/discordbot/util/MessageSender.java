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

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.HashMap;
import java.util.LinkedHashMap;

import org.apache.commons.lang3.StringEscapeUtils;

import io.github.lxgaming.discordbot.DiscordBotCore;
import io.github.lxgaming.discordbot.entries.Channel;
import io.github.lxgaming.discordbot.entries.Message;

public class MessageSender {
	
	public void sendMessage(Message message) {
		new Thread(new Runnable() {
			@Override
			public void run() {
				if (message.sendDiscord() && DiscordBotCore.getInstance().getConfiguration().isSendDiscord()) {
					sendMessageDiscord(message);
				}
				
				if (message.sendMinecraft() && DiscordBotCore.getInstance().getConfiguration().isSendMinecraft()) {
					sendMessageMinecraft(message);
				}
				
				if (message.sendConsole() && DiscordBotCore.getInstance().getConfiguration().isSendConsole()) {
					sendMessageConsole(message);
				}
			}
		}).start();
	}
	
	public void sendMessageDiscord(Message message) {
		if (message.getChannel() == null || message.getChannel().trim().equals("")) {
			DiscordBotCore.getInstance().getLogger().severe("Unable to send message as channel '" + message.getChannel() + "' Has not been setup correctly.");
			return;
		}
		DiscordBotCore.getInstance().getJDA().getTextChannelById(message.getChannel()).sendMessage(getDiscordFormat(message)).queue();
	}
	
	public void sendMessageMinecraft(Message message) {
		Channel channel = DiscordBotCore.getInstance().getConfiguration().getChannels().get(DiscordBotCore.getInstance().getChannelManager().getChannelName(message.getChannel()));
		
		if (channel == null) {
			return;
		}
		
		HashMap<String, String> data = new LinkedHashMap<String, String>();
		data.put("Permission", channel.getPermission());
		
		message.setMessage(getMinecraftFormat(message, channel.isChatColor()));
		message.setData(data);
		
		DiscordBotCore.getInstance().getEventManager().onMessageMinecraft(message);
	}
	
	public void sendMessageConsole(Message message) {
		DiscordBotCore.getInstance().getLogger().info(message.getName() + " - " + message.getMessage());
	}
	
	private String getDiscordFormat(Message message) {
		if (message.getFormat() == null) {
			DiscordBotCore.getInstance().getLogger().severe("Unable to send message as format was blank or null!");
			return null;
		}
		
		String messageFormat = message.getFormat().getDiscordFormat();
		if (messageFormat.equals("") || messageFormat.equals("null")) {
			DiscordBotCore.getInstance().getLogger().severe("'DiscordBot." + message.getFormat().getName() + ".DiscordFormat' is blank or null!");
			return null;
		}
		
		if (message.getNick() == null || message.getNick().equals("")) {
			message.setNick(message.getName());
		}
		
		return messageFormat
				.replace("%time%", new SimpleDateFormat("HH:mm:ss").format(Calendar.getInstance().getTime()))
				.replace("%name%", message.getName())
				.replace("%nick%", message.getNick())
				.replace("%server%", message.getServer())
				.replace("%message%", message.getMessage());
	}
	
	private String getMinecraftFormat(Message message, boolean chatColor) {
		if (message.getFormat() == null) {
			DiscordBotCore.getInstance().getLogger().severe("Unable to send message as format was blank or null!");
			return null;
		}
		
		String messageFormat = message.getFormat().getMinecraftFormat();
		if (messageFormat.equals("") || messageFormat.equals("null")) {
			DiscordBotCore.getInstance().getLogger().severe("'DiscordBot." + message.getFormat() + ".MinecraftFormat' is blank or null!");
			return null;
		}
		
		if (message.getNick() == null || message.getNick().equals("")) {
			message.setNick(message.getName());
		}
		
		if (chatColor) {
			return messageFormat
					.replace("%time%", new SimpleDateFormat("HH:mm:ss").format(Calendar.getInstance().getTime()))
					.replace("%name%", message.getName())
					.replace("%nick%", message.getNick())
					.replace("%server%", message.getServer())
					.replace("%message%", message.getMessage())
					.replace("&", StringEscapeUtils.unescapeJava("\u00A7"));
		}
		return messageFormat
				.replace("%time%", new SimpleDateFormat("HH:mm:ss").format(Calendar.getInstance().getTime()))
				.replace("%name%", message.getName())
				.replace("%nick%", message.getNick())
				.replace("%server%", message.getServer())
				.replace("&", StringEscapeUtils.unescapeJava("\u00A7"))
				.replace("%message%", message.getMessage());
	}
	
	@Deprecated
	public String getCommandFormat(Message message) {
		String messageFormat = message.getFormat().getDiscordFormat();
		if (messageFormat.equals("") || messageFormat.equals("null")) {
			return null;
		}
		
		if (message.getNick() == null || message.getNick().equals("")) {
			message.setNick(message.getName());
		}
		
		return messageFormat
				.replace("%time%", new SimpleDateFormat("HH:mm:ss").format(Calendar.getInstance().getTime()))
				.replace("%name%", message.getName())
				.replace("%nick%", message.getNick())
				.replace("%command%", message.getData().get("command"));
	}
}