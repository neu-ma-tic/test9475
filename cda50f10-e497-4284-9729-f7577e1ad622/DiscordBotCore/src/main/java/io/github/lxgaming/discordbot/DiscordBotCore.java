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

package io.github.lxgaming.discordbot;

import java.util.logging.Logger;

import javax.security.auth.login.LoginException;

import io.github.lxgaming.discordbot.configuration.DiscordBotConfiguration;
import io.github.lxgaming.discordbot.listeners.BotListener;
import io.github.lxgaming.discordbot.util.ChannelManager;
import io.github.lxgaming.discordbot.util.DatabaseManager;
import io.github.lxgaming.discordbot.util.EventManager;
import io.github.lxgaming.discordbot.util.MessageSender;
import net.dv8tion.jda.core.AccountType;
import net.dv8tion.jda.core.JDA;
import net.dv8tion.jda.core.JDABuilder;
import net.dv8tion.jda.core.exceptions.RateLimitedException;

public class DiscordBotCore {
	
	private static DiscordBotCore instance;
	private Logger logger;
	private DiscordBotConfiguration discordBotConfiguration;
	private ChannelManager channelManager;
	private MessageSender messageSender;
	private DatabaseManager databaseManager;
	private EventManager eventManager;
	private JDA jda;
	
	public DiscordBotCore(Logger logger) {
		instance = this;
		this.logger = logger;
	}
	
	public void preInit() {
		this.discordBotConfiguration = new DiscordBotConfiguration();
	}
	
	public void init() {
		this.channelManager = new ChannelManager();
		this.messageSender = new MessageSender();
		this.databaseManager = new DatabaseManager();
		this.eventManager = new EventManager();
	}
	
	public void postInit() {
		String token = getConfiguration().getToken();
		JDABuilder jdaBuilder = null;
		
		if (token != null && !token.equals("") && !token.equals("null")) {
			jdaBuilder = new JDABuilder(AccountType.BOT).setToken(token);
		}
		
		token = null;
		
		if (jdaBuilder == null) {
			getLogger().severe("Cannot start DiscordBot, No Token / Email and Password provided!");
			return;
		}
		
		try {
			jda = jdaBuilder
					.addEventListener(new BotListener())
					.setAudioEnabled(false)
					.setBulkDeleteSplittingEnabled(false)
					.buildAsync();
		} catch (IllegalArgumentException | LoginException | RateLimitedException ex) {
			getLogger().severe("Connection Failed! Invalid BotToken");
			ex.printStackTrace();
		}
	}
	
	public void shutdown() {
		if (jda != null) {
			jda.shutdown(true);
			jda = null;
		}
		
		instance = null;
	}
	
	public static DiscordBotCore getInstance() {
		return instance;
	}
	
	public Logger getLogger() {
		return this.logger;
	}
	
	public DiscordBotConfiguration getConfiguration() {
		return this.discordBotConfiguration;
	}
	
	public ChannelManager getChannelManager() {
		return this.channelManager;
	}
	
	public MessageSender getMessageSender() {
		return this.messageSender;
	}
	
	public DatabaseManager getDatabaseManager() {
		return this.databaseManager;
	}
	
	public EventManager getEventManager() {
		return this.eventManager;
	}
	
	public JDA getJDA() {
		return this.jda;
	}
}