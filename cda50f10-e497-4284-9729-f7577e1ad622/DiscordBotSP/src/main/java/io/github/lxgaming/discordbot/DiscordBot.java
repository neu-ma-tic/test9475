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

import org.bukkit.plugin.java.JavaPlugin;

import io.github.lxgaming.discordbot.commands.DiscordBotCommand;
import io.github.lxgaming.discordbot.configuration.Config;
import io.github.lxgaming.discordbot.listeners.DiscordBotListener;
import io.github.lxgaming.discordbot.listeners.PlayerListener;
import io.github.lxgaming.discordbot.util.CommandManager;

public class DiscordBot extends JavaPlugin {
	
	private static DiscordBot instance;
	private Config config;
	private CommandManager commandManager;
	
	@Override
	public void onEnable() {
		instance = this;
		new DiscordBotCore(getLogger());
		DiscordBotCore.getInstance().preInit();
		this.config = new Config();
		this.config.loadConfig();
		
		DiscordBotCore.getInstance().init();
		DiscordBotCore.getInstance().getEventManager().addListener(new DiscordBotListener());
		
		getCommand("discordbot").setExecutor(new DiscordBotCommand());
		getServer().getPluginManager().registerEvents(new PlayerListener(), this);
		DiscordBotCore.getInstance().postInit();
		getLogger().info("DiscordBot has started!");
	}
	
	@Override
	public void onDisable() {
		DiscordBotCore.getInstance().shutdown();
		instance = null;
		getLogger().info("DiscordBot has stopped!");
	}
	
	public void reloadDiscordBot() {
		this.config.loadConfig();
		DiscordBotCore.getInstance().getChannelManager().setupChannels();
	}
	
	public static DiscordBot getInstance() {
		return instance;
	}
	
	public Config getConfiguration() {
		return this.config;
	}
	
	public CommandManager getCommandManager() {
		return this.commandManager;
	}
}