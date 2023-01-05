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

import com.imaginarycode.minecraft.redisbungee.RedisBungee;
import com.imaginarycode.minecraft.redisbungee.RedisBungeeAPI;

import io.github.lxgaming.discordbot.commands.DiscordBotCommand;
import io.github.lxgaming.discordbot.configuration.Config;
import io.github.lxgaming.discordbot.listeners.DiscordBotListener;
import io.github.lxgaming.discordbot.listeners.PlayerListener;
import io.github.lxgaming.discordbot.listeners.RedisListener;
import net.md_5.bungee.api.plugin.Plugin;

public class DiscordBot extends Plugin {
	
	private static DiscordBot instance;
	private Config config;
	private RedisBungeeAPI redisBungee;
	
	@Override
	public void onEnable() {
		instance = this;
		new DiscordBotCore(getLogger());
		DiscordBotCore.getInstance().preInit();
		this.config = new Config();
		this.config.loadConfig();
		
		DiscordBotCore.getInstance().init();
		DiscordBotCore.getInstance().getEventManager().addListener(new DiscordBotListener());
		
		getProxy().getPluginManager().registerCommand(this, new DiscordBotCommand());
		getProxy().getPluginManager().registerListener(this, new PlayerListener());
		DiscordBotCore.getInstance().postInit();
		loadRedis();
	}
	
	@Override
	public void onDisable() {
		DiscordBotCore.getInstance().shutdown();
		
		if (redisBungee != null) {
			redisBungee.unregisterPubSubChannels("DiscordBot");
			redisBungee = null;
		}
		instance = null;
	}
	
	public void reloadDiscordBot() {
		this.config.loadConfig();
		DiscordBotCore.getInstance().getChannelManager().setupChannels();
	}
	
	private void loadRedis() {
		if (!DiscordBotCore.getInstance().getConfiguration().isRedisEnabled()) {
			return;
		}
		
		redisBungee = RedisBungee.getApi();
		redisBungee.registerPubSubChannels("DiscordBot");
		getProxy().getPluginManager().registerListener(this, new RedisListener());
		getLogger().info("Redis Enabled.");
	}
	
	public static DiscordBot getInstance() {
		return instance;
	}
	
	public Config getConfiguration() {
		return this.config;
	}
	
	public RedisBungeeAPI getRedisBungee() {
		return this.redisBungee;
	}
}