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

import java.util.HashMap;
import java.util.List;

import io.github.lxgaming.discordbot.entries.Channel;
import io.github.lxgaming.discordbot.entries.MessageFormat;

public class DiscordBotConfiguration {
	
	private String discordBotVersion = "DiscordBot v0.9.0";
	private String jdaVersion = "JDA v3.0.BETA2";
	
	private String token;
	private boolean redisEnabled;
	private String commandPrefix;
	private boolean connectionMessage;
	private boolean sendDiscord;
	private boolean sendMinecraft;
	private boolean sendConsole;
	private boolean forceChat;
	private boolean allowCommands;
	private boolean userAvatarUpdate;
	private boolean userGameUpdate;
	private boolean userNameUpdate;
	private boolean userOnlineStatusUpdate;
	private boolean voiceDeafen;
	private boolean voiceMute;
	private boolean playerChat;
	private boolean playerJoin;
	private boolean playerDeath;
	private boolean playerQuit;
	
	private List<String> database;
	
	private MessageFormat readyFormat;
	private MessageFormat userAvatarUpdateFormat;
	private MessageFormat userGameUpdateFormat;
	private MessageFormat userNameUpdateFormat;
	private HashMap<String, MessageFormat> userOnlineStatusUpdateFormat;
	private HashMap<String, MessageFormat> voiceDeafenFormat;
	private HashMap<String, MessageFormat> voiceMuteFormat;
	private HashMap<String, MessageFormat> playerFormat;
	private HashMap<String, MessageFormat> channelFormat;
	private HashMap<String, MessageFormat> commandFormat;
	
	private String guildId;
	private HashMap<String, Channel> channels;
	
	public String getDiscordBotVersion() {
		return this.discordBotVersion;
	}
	
	public String getJDAVersion() {
		return this.jdaVersion;
	}
	
	public String getToken() {
		return token;
	}
	
	public void setToken(String token) {
		this.token = token;
	}
	
	public boolean isRedisEnabled() {
		return redisEnabled;
	}
	
	public void setRedisEnabled(boolean redisEnabled) {
		this.redisEnabled = redisEnabled;
	}
	
	public String getCommandPrefix() {
		return commandPrefix;
	}
	
	public void setCommandPrefix(String commandPrefix) {
		this.commandPrefix = commandPrefix;
	}
	
	public boolean isConnectionMessage() {
		return connectionMessage;
	}
	
	public void setConnectionMessage(boolean connectionMessage) {
		this.connectionMessage = connectionMessage;
	}
	
	public boolean isSendDiscord() {
		return sendDiscord;
	}
	
	public void setSendDiscord(boolean sendDiscord) {
		this.sendDiscord = sendDiscord;
	}
	
	public boolean isSendMinecraft() {
		return sendMinecraft;
	}
	
	public void setSendMinecraft(boolean sendMinecraft) {
		this.sendMinecraft = sendMinecraft;
	}
	
	public boolean isSendConsole() {
		return sendConsole;
	}
	
	public void setSendConsole(boolean sendConsole) {
		this.sendConsole = sendConsole;
	}
	
	public boolean isForceChat() {
		return forceChat;
	}
	
	public void setForceChat(boolean forceChat) {
		this.forceChat = forceChat;
	}
	
	public boolean isAllowCommands() {
		return allowCommands;
	}
	
	public void setAllowCommands(boolean commands) {
		this.allowCommands = commands;
	}
	
	public boolean isUserAvatarUpdate() {
		return userAvatarUpdate;
	}
	
	public void setUserAvatarUpdate(boolean userAvatarUpdate) {
		this.userAvatarUpdate = userAvatarUpdate;
	}
	
	public boolean isUserGameUpdate() {
		return userGameUpdate;
	}
	
	public void setUserGameUpdate(boolean userGameUpdate) {
		this.userGameUpdate = userGameUpdate;
	}
	
	public boolean isUserNameUpdate() {
		return userNameUpdate;
	}
	
	public void setUserNameUpdate(boolean userNameUpdate) {
		this.userNameUpdate = userNameUpdate;
	}
	
	public boolean isUserOnlineStatusUpdate() {
		return userOnlineStatusUpdate;
	}
	
	public void setUserOnlineStatusUpdate(boolean userOnlineStatusUpdate) {
		this.userOnlineStatusUpdate = userOnlineStatusUpdate;
	}
	
	public boolean isVoiceDeafen() {
		return voiceDeafen;
	}
	
	public void setVoiceDeafen(boolean voiceDeafen) {
		this.voiceDeafen = voiceDeafen;
	}
	
	public boolean isVoiceMute() {
		return voiceMute;
	}
	
	public void setVoiceMute(boolean voiceMute) {
		this.voiceMute = voiceMute;
	}
	
	public boolean isPlayerChat() {
		return playerChat;
	}
	
	public void setPlayerChat(boolean playerChat) {
		this.playerChat = playerChat;
	}
	
	public boolean isPlayerJoin() {
		return playerJoin;
	}
	
	public void setPlayerJoin(boolean playerJoin) {
		this.playerJoin = playerJoin;
	}
	
	public boolean isPlayerDeath() {
		return playerDeath;
	}
	
	public void setPlayerDeath(boolean playerDeath) {
		this.playerDeath = playerDeath;
	}
	
	public boolean isPlayerQuit() {
		return playerQuit;
	}
	
	public void setPlayerQuit(boolean playerQuit) {
		this.playerQuit = playerQuit;
	}
	
	public List<String> getDatabase() {
		return database;
	}
	
	public void setDatabase(List<String> database) {
		this.database = database;
	}
	
	public MessageFormat getReadyFormat() {
		return readyFormat;
	}
	
	public void setReadyFormat(MessageFormat readyFormat) {
		this.readyFormat = readyFormat;
	}
	
	public MessageFormat getUserAvatarUpdateFormat() {
		return userAvatarUpdateFormat;
	}
	
	public void setUserAvatarUpdateFormat(MessageFormat userAvatarUpdateFormat) {
		this.userAvatarUpdateFormat = userAvatarUpdateFormat;
	}
	
	public MessageFormat getUserGameUpdateFormat() {
		return userGameUpdateFormat;
	}
	
	public void setUserGameUpdateFormat(MessageFormat userGameUpdateFormat) {
		this.userGameUpdateFormat = userGameUpdateFormat;
	}
	
	public MessageFormat getUserNameUpdateFormat() {
		return userNameUpdateFormat;
	}
	
	public void setUserNameUpdateFormat(MessageFormat userNameUpdateFormat) {
		this.userNameUpdateFormat = userNameUpdateFormat;
	}
	
	public HashMap<String, MessageFormat> getUserOnlineStatusUpdateFormat() {
		return userOnlineStatusUpdateFormat;
	}
	
	public void setUserOnlineStatusUpdateFormat(HashMap<String, MessageFormat> userOnlineStatusUpdateFormat) {
		this.userOnlineStatusUpdateFormat = userOnlineStatusUpdateFormat;
	}
	
	public HashMap<String, MessageFormat> getVoiceDeafenFormat() {
		return voiceDeafenFormat;
	}
	
	public void setVoiceDeafenFormat(HashMap<String, MessageFormat> voiceDeafenFormat) {
		this.voiceDeafenFormat = voiceDeafenFormat;
	}
	
	public HashMap<String, MessageFormat> getVoiceMuteFormat() {
		return voiceMuteFormat;
	}
	
	public void setVoiceMuteFormat(HashMap<String, MessageFormat> voiceMuteFormat) {
		this.voiceMuteFormat = voiceMuteFormat;
	}
	
	public HashMap<String, MessageFormat> getPlayerFormat() {
		return playerFormat;
	}
	
	public void setPlayerFormat(HashMap<String, MessageFormat> playerFormat) {
		this.playerFormat = playerFormat;
	}
	
	public HashMap<String, MessageFormat> getChannelFormat() {
		return channelFormat;
	}
	
	public void setChannelFormat(HashMap<String, MessageFormat> channelFormat) {
		this.channelFormat = channelFormat;
	}
	
	public HashMap<String, MessageFormat> getCommandFormat() {
		return commandFormat;
	}
	
	public void setCommandFormat(HashMap<String, MessageFormat> commandFormat) {
		this.commandFormat = commandFormat;
	}
	
	public String getGuildId() {
		return guildId;
	}
	
	public void setGuildId(String guildId) {
		this.guildId = guildId;
	}
	
	public HashMap<String, Channel> getChannels() {
		return channels;
	}
	
	public void setChannels(HashMap<String, Channel> channels) {
		this.channels = channels;
	}
}