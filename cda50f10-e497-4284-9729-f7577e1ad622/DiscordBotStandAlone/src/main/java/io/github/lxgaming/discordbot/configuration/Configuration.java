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
import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;

import com.google.gson.Gson;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

import io.github.lxgaming.discordbot.DiscordBot;
import io.github.lxgaming.discordbot.entries.Config;
import io.github.lxgaming.discordbot.util.LogHelper;

public class Configuration {
	
	private File configFile;
	private Config config;
	
	public Configuration() {
		configFile = new File("config.json");
		config = new Config();
	}
	
	public void loadConfiguration() {
		try {
			if (!configFile.exists()) {
				configFile.createNewFile();
				InputStream inputStream = DiscordBot.class.getResourceAsStream("/config.json");
				Files.copy(inputStream, configFile.toPath(), StandardCopyOption.REPLACE_EXISTING);
				LogHelper.info("Successfully created configuration file.");
			}
			
			JsonObject jsonObject = new JsonParser().parse(new String(Files.readAllBytes(configFile.toPath()), StandardCharsets.UTF_8)).getAsJsonObject();
			setConfig(new Gson().fromJson(jsonObject, Config.class));
			
			LogHelper.info("Successfully loaded configuration file.");
		} catch (IOException | OutOfMemoryError | RuntimeException ex) {
			LogHelper.error("Exception loading configuration file!");
			ex.printStackTrace();
		}
		return;
	}
	
	public Config getConfig() {
		return config;
	}
	
	private void setConfig(Config config) {
		this.config = config;
	}
}