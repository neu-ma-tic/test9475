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

package io.github.lxgaming.discordbot.entries;

public class MessageFormat {
	
	private String name;
	private String minecraftFormat;
	private String discordFormat;
	
	public String getName() {
		return name;
	}
	
	public MessageFormat setName(String name) {
		this.name = name;
		return this;
	}
	
	public String getMinecraftFormat() {
		return minecraftFormat;
	}
	
	public MessageFormat setMinecraftFormat(String minecraftFormat) {
		this.minecraftFormat = minecraftFormat;
		return this;
	}
	
	public String getDiscordFormat() {
		return discordFormat;
	}
	
	public MessageFormat setDiscordFormat(String discordFormat) {
		this.discordFormat = discordFormat;
		return this;
	}
}