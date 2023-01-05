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

public class Channel {
	
	private String name;
	private String command;
	private String channel;
	private boolean chatColor;
	private String permission;
	
	public String getName() {
		return name;
	}
	
	public Channel setName(String name) {
		this.name = name;
		return this;
	}
	
	public String getCommand() {
		return command;
	}
	
	public Channel setCommand(String command) {
		this.command = command;
		return this;
	}
	
	public String getChannel() {
		return channel;
	}
	
	public Channel setChannel(String channel) {
		this.channel = channel;
		return this;
	}
	
	public boolean isChatColor() {
		return chatColor;
	}
	
	public Channel setChatColor(boolean chatColor) {
		this.chatColor = chatColor;
		return this;
	}
	
	public String getPermission() {
		return permission;
	}
	
	public Channel setPermission(String permission) {
		this.permission = permission;
		return this;
	}
}