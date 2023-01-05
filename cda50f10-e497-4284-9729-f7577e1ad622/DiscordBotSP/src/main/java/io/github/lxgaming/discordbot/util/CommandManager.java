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

import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.util.Arrays;

import org.bukkit.Bukkit;
import org.bukkit.command.CommandMap;
import org.bukkit.command.PluginCommand;
import org.bukkit.plugin.Plugin;
import org.bukkit.plugin.SimplePluginManager;

import io.github.lxgaming.discordbot.DiscordBot;

public class CommandManager {
	
	public void registerCommand(String... aliases) {
		PluginCommand pluginCommand = getCommand(aliases[0], DiscordBot.getInstance());
		pluginCommand.setAliases(Arrays.asList(aliases));
		getCommandMap().register(DiscordBot.getInstance().getDescription().getName(), pluginCommand);
	}
	
	private PluginCommand getCommand(String name, Plugin plugin) {
		try {
			Constructor<PluginCommand> constructor = PluginCommand.class.getDeclaredConstructor(String.class, Plugin.class);
			constructor.setAccessible(true);
			return constructor.newInstance(name, plugin);
		} catch (IllegalAccessException | IllegalArgumentException | InstantiationException | InvocationTargetException | NoSuchMethodException | SecurityException ex) {
			DiscordBot.getInstance().getLogger().severe("Exception getting command!");
			ex.printStackTrace();
		}
		return null;
	}
	
	private CommandMap getCommandMap() {
		if (!(Bukkit.getPluginManager() instanceof SimplePluginManager)) {
			return null;
		}
		
		try {
			Field field = SimplePluginManager.class.getDeclaredField("commandMap");
			field.setAccessible(true);
			return (CommandMap) field.get(Bukkit.getPluginManager());
		} catch (IllegalAccessException | IllegalArgumentException | NoSuchFieldException | SecurityException ex) {
			DiscordBot.getInstance().getLogger().severe("Exception getting commandMap!");
			ex.printStackTrace();
		}
		return null;
	}
}
