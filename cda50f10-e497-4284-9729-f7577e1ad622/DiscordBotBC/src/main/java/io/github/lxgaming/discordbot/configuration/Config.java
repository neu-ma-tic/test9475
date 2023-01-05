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

package io.github.lxgaming.discordbot.configuration;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedHashMap;

import com.google.common.io.ByteStreams;

import io.github.lxgaming.discordbot.DiscordBot;
import io.github.lxgaming.discordbot.DiscordBotCore;
import io.github.lxgaming.discordbot.entries.Channel;
import io.github.lxgaming.discordbot.entries.MessageFormat;
import net.md_5.bungee.config.Configuration;
import net.md_5.bungee.config.ConfigurationProvider;
import net.md_5.bungee.config.YamlConfiguration;

public class Config {
	
	private Configuration channels, config, database, messages;
	
	public void loadConfig() {
		if (!DiscordBot.getInstance().getDataFolder().exists()) {
			DiscordBot.getInstance().getDataFolder().mkdir();
		}
		
		this.channels = loadFile("channels.yml");
		this.config = loadFile("config.yml");
		this.database = loadFile("database.yml");
		this.messages = loadFile("messages.yml");
		process();
	}
	
	public Configuration loadFile(String name) {
		try {
			File file = new File(DiscordBot.getInstance().getDataFolder(), name);
			
			if (!file.exists()) {
				file.createNewFile();
				InputStream inputStream = DiscordBot.getInstance().getResourceAsStream(name);
				OutputStream outputStream = new FileOutputStream(file);
				ByteStreams.copy(inputStream, outputStream);
				DiscordBot.getInstance().getLogger().info("Successfully created " + name);
			}
			
			return ConfigurationProvider.getProvider(YamlConfiguration.class).load(file);
		} catch (IOException | NullPointerException | SecurityException ex) {
			DiscordBot.getInstance().getLogger().severe("Exception loading " + name);
			ex.printStackTrace();
		}
		return null;
	}
	
	public void saveFile(String name, Configuration config) {
		try {
			File file = new File(DiscordBot.getInstance().getDataFolder(), name);
			ConfigurationProvider.getProvider(YamlConfiguration.class).save(config, file);
		} catch (IOException | NullPointerException | SecurityException ex) {
			DiscordBot.getInstance().getLogger().severe("Exception saving " + name);
			ex.printStackTrace();
		}
	}
	
	public Configuration getDatabase() {
		return this.database;
	}
	
	public boolean process() {
		if (this.channels == null || this.config == null || this.database == null || this.messages == null) {
			return false;
		}
		
		DiscordBotCore.getInstance().getConfiguration().setToken(this.config.getString("DiscordBot.Credentials.Token"));
		DiscordBotCore.getInstance().getConfiguration().setRedisEnabled(this.config.getBoolean("DiscordBot.Redis.Enabled"));
		DiscordBotCore.getInstance().getConfiguration().setCommandPrefix(this.config.getString("DiscordBot.Messages.CommandPrefix"));
		DiscordBotCore.getInstance().getConfiguration().setConnectionMessage(this.config.getBoolean("DiscordBot.Messages.ConnectionMessage"));
		DiscordBotCore.getInstance().getConfiguration().setSendDiscord(this.config.getBoolean("DiscordBot.Messages.SendDiscord"));
		DiscordBotCore.getInstance().getConfiguration().setSendMinecraft(this.config.getBoolean("DiscordBot.Messages.SendMinecraft"));
		DiscordBotCore.getInstance().getConfiguration().setSendConsole(this.config.getBoolean("DiscordBot.Messages.SendConsole"));
		DiscordBotCore.getInstance().getConfiguration().setForceChat(this.config.getBoolean("DiscordBot.Messages.ForceChat"));
		DiscordBotCore.getInstance().getConfiguration().setAllowCommands(this.config.getBoolean("DiscordBot.Listeners.AllowCommands"));
		DiscordBotCore.getInstance().getConfiguration().setUserAvatarUpdate(this.config.getBoolean("DiscordBot.Listeners.UserAvatarUpdate"));
		DiscordBotCore.getInstance().getConfiguration().setUserGameUpdate(this.config.getBoolean("DiscordBot.Listeners.UserGameUpdate"));
		DiscordBotCore.getInstance().getConfiguration().setUserNameUpdate(this.config.getBoolean("DiscordBot.Listeners.UserNameUpdate"));
		DiscordBotCore.getInstance().getConfiguration().setUserOnlineStatusUpdate(this.config.getBoolean("DiscordBot.Listeners.UserOnlineStatusUpdate"));
		DiscordBotCore.getInstance().getConfiguration().setVoiceDeafen(this.config.getBoolean("DiscordBot.Listeners.VoiceDeafen"));
		DiscordBotCore.getInstance().getConfiguration().setVoiceMute(this.config.getBoolean("DiscordBot.Listeners.VoiceMute"));
		DiscordBotCore.getInstance().getConfiguration().setPlayerJoin(this.config.getBoolean("DiscordBot.Events.PlayerChat"));
		DiscordBotCore.getInstance().getConfiguration().setPlayerChat(this.config.getBoolean("DiscordBot.Events.PlayerJoin"));
		DiscordBotCore.getInstance().getConfiguration().setPlayerDeath(false);
		DiscordBotCore.getInstance().getConfiguration().setPlayerQuit(this.config.getBoolean("DiscordBot.Events.PlayerQuit"));
		
		DiscordBotCore.getInstance().getConfiguration().setDatabase(this.database.getStringList("DiscordBot.Database"));
		
		DiscordBotCore.getInstance().getConfiguration().setReadyFormat(new MessageFormat()
				.setName("Ready")
				.setMinecraftFormat(this.messages.getString("DiscordBot.Ready.MinecraftFormat"))
				.setDiscordFormat(this.messages.getString("DiscordBot.Ready.DiscordFormat")));
		DiscordBotCore.getInstance().getConfiguration().setUserAvatarUpdateFormat(new MessageFormat()
				.setName("UserAvatarUpdate")
				.setMinecraftFormat(this.messages.getString("DiscordBot.UserAvatarUpdate.MinecraftFormat"))
				.setDiscordFormat(this.messages.getString("DiscordBot.UserAvatarUpdate.DiscordFormat")));
		DiscordBotCore.getInstance().getConfiguration().setUserGameUpdateFormat(new MessageFormat()
				.setName("UserGameUpdate")
				.setMinecraftFormat(this.messages.getString("DiscordBot.UserGameUpdate.MinecraftFormat"))
				.setDiscordFormat(this.messages.getString("DiscordBot.UserGameUpdate.DiscordFormat")));
		DiscordBotCore.getInstance().getConfiguration().setUserNameUpdateFormat(new MessageFormat()
				.setName("UserNameUpdate")
				.setMinecraftFormat(this.messages.getString("DiscordBot.UserNameUpdate.MinecraftFormat"))
				.setDiscordFormat(this.messages.getString("DiscordBot.UserNameUpdate.DiscordFormat")));
		
		HashMap<String, MessageFormat> userOnlineStatusUpdateFormat = new LinkedHashMap<String, MessageFormat>();
		userOnlineStatusUpdateFormat.put("ONLINE", new MessageFormat()
				.setName("UserOnlineStatusUpdate - ONLINE")
				.setMinecraftFormat(this.messages.getString("DiscordBot.UserOnlineStatusUpdate.ONLINE.MinecraftFormat"))
				.setDiscordFormat(this.messages.getString("DiscordBot.UserOnlineStatusUpdate.ONLINE.DiscordFormat")));
		userOnlineStatusUpdateFormat.put("IDLE", new MessageFormat()
				.setName("UserOnlineStatusUpdate - IDLE")
				.setMinecraftFormat(this.messages.getString("DiscordBot.UserOnlineStatusUpdate.IDLE.MinecraftFormat"))
				.setDiscordFormat(this.messages.getString("DiscordBot.UserOnlineStatusUpdate.IDLE.DiscordFormat")));
		userOnlineStatusUpdateFormat.put("DO_NOT_DISTURB", new MessageFormat()
				.setName("UserOnlineStatusUpdate - DO_NOT_DISTURB")
				.setMinecraftFormat(this.messages.getString("DiscordBot.UserOnlineStatusUpdate.DO_NOT_DISTURB.MinecraftFormat"))
				.setDiscordFormat(this.messages.getString("DiscordBot.UserOnlineStatusUpdate.DO_NOT_DISTURB.DiscordFormat")));
		userOnlineStatusUpdateFormat.put("OFFLINE", new MessageFormat()
				.setName("UserOnlineStatusUpdate - OFFLINE")
				.setMinecraftFormat(this.messages.getString("DiscordBot.UserOnlineStatusUpdate.OFFLINE.MinecraftFormat"))
				.setDiscordFormat(this.messages.getString("DiscordBot.UserOnlineStatusUpdate.OFFLINE.DiscordFormat")));
		DiscordBotCore.getInstance().getConfiguration().setUserOnlineStatusUpdateFormat(userOnlineStatusUpdateFormat);
		
		HashMap<String, MessageFormat> voiceDeafenFormat = new LinkedHashMap<String, MessageFormat>();
		voiceDeafenFormat.put("Deafened", new MessageFormat()
				.setName("VoiceDeafen - Deafened")
				.setMinecraftFormat(this.messages.getString("DiscordBot.VoiceDeafen.Deafened.MinecraftFormat"))
				.setDiscordFormat(this.messages.getString("DiscordBot.VoiceDeafen.Deafened.DiscordFormat")));
		voiceDeafenFormat.put("Undeafened", new MessageFormat()
				.setName("VoiceDeafen - Undeafened")
				.setMinecraftFormat(this.messages.getString("DiscordBot.VoiceDeafen.Undeafened.MinecraftFormat"))
				.setDiscordFormat(this.messages.getString("DiscordBot.VoiceDeafen.Undeafened.DiscordFormat")));
		DiscordBotCore.getInstance().getConfiguration().setVoiceDeafenFormat(voiceDeafenFormat);
		
		HashMap<String, MessageFormat> voiceMuteFormat = new LinkedHashMap<String, MessageFormat>();
		voiceMuteFormat.put("Muted", new MessageFormat()
				.setName("VoiceMute - Muted")
				.setMinecraftFormat(this.messages.getString("DiscordBot.VoiceMute.Muted.MinecraftFormat"))
				.setDiscordFormat(this.messages.getString("DiscordBot.VoiceMute.Muted.DiscordFormat")));
		voiceMuteFormat.put("Unmuted", new MessageFormat()
				.setName("VoiceMute - Unmuted")
				.setMinecraftFormat(this.messages.getString("DiscordBot.VoiceMute.Unmuted.MinecraftFormat"))
				.setDiscordFormat(this.messages.getString("DiscordBot.VoiceMute.Unmuted.DiscordFormat")));
		DiscordBotCore.getInstance().getConfiguration().setVoiceMuteFormat(voiceMuteFormat);
		
		HashMap<String, MessageFormat> playerFormat = new LinkedHashMap<String, MessageFormat>();
		playerFormat.put("Join", new MessageFormat()
				.setName("Player - Join")
				.setMinecraftFormat(this.messages.getString("DiscordBot.Player.Join.MinecraftFormat"))
				.setDiscordFormat(this.messages.getString("DiscordBot.Player.Join.DiscordFormat")));
		playerFormat.put("Quit", new MessageFormat()
				.setName("Player - Quit")
				.setMinecraftFormat(this.messages.getString("DiscordBot.Player.Quit.MinecraftFormat"))
				.setDiscordFormat(this.messages.getString("DiscordBot.Player.Quit.DiscordFormat")));
		DiscordBotCore.getInstance().getConfiguration().setPlayerFormat(playerFormat);
		
		HashMap<String, MessageFormat> channelFormat = new LinkedHashMap<String, MessageFormat>();
		for (Iterator<String> iterator = this.messages.getSection("DiscordBot.Channel").getKeys().iterator(); iterator.hasNext();) {
			String channel = iterator.next();
			channelFormat.put(channel, new MessageFormat()
					.setName(channel)
					.setMinecraftFormat(this.messages.getString("DiscordBot.Channel." + channel + ".MinecraftFormat"))
					.setDiscordFormat(this.messages.getString("DiscordBot.Channel." + channel + ".DiscordFormat")));
		}
		DiscordBotCore.getInstance().getConfiguration().setChannelFormat(channelFormat);
		
		HashMap<String, MessageFormat> commandFormat = new LinkedHashMap<String, MessageFormat>();
		for (Iterator<String> iterator = this.messages.getSection("DiscordBot.Command").getKeys().iterator(); iterator.hasNext();) {
			String command = iterator.next();
			commandFormat.put(command, new MessageFormat()
					.setName(command)
					.setMinecraftFormat(this.messages.getString("DiscordBot.Command." + command + ".MinecraftFormat"))
					.setDiscordFormat(this.messages.getString("DiscordBot.Command." + command + ".DiscordFormat")));
		}
		DiscordBotCore.getInstance().getConfiguration().setChannelFormat(commandFormat);
		
		DiscordBotCore.getInstance().getConfiguration().setGuildId(this.channels.getString("DiscordBot.Guild.Id"));
		
		HashMap<String, Channel> channels = new LinkedHashMap<String, Channel>();
		for (Iterator<String> iterator = this.channels.getSection("DiscordBot.Channels").getKeys().iterator(); iterator.hasNext();) {
			String channel = iterator.next();
			channels.put(channel, new Channel()
					.setCommand(this.channels.getString("DiscordBot.Channels." + channel + ".Command"))
					.setChannel(this.channels.getString("DiscordBot.Channels." + channel + ".Channel"))
					.setChatColor(this.channels.getBoolean("DiscordBot.Channels." + channel + ".ChatColor"))
					.setPermission(this.channels.getString("DiscordBot.Channels." + channel + ".Permission")));
		}
		DiscordBotCore.getInstance().getConfiguration().setChannels(channels);
		return true;
	}
}