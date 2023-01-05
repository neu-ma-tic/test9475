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

import io.github.lxgaming.discordbot.configuration.Configuration;
import io.github.lxgaming.discordbot.discord.Discord;
import io.github.lxgaming.discordbot.entries.Config;

public class DiscordBot {
	
	private static DiscordBot instance;
	private Configuration configuration;
	private Discord discord;
	
	public DiscordBot() {
		instance = this;
		configuration = new Configuration();
		discord = new Discord();
	}
	
	public void loadDiscordBot() {
		getConfiguration().loadConfiguration();
		getDiscord().loadDiscord();
	}
	
	public static DiscordBot getInstance() {
		return instance;
	}
	
	private Configuration getConfiguration() {
		return configuration;
	}
	
	public Config getConfig() {
		if (getConfiguration() != null) {
			return getConfiguration().getConfig();
		}
		return null;
	}
	
	public Discord getDiscord() {
		return discord;
	}
}