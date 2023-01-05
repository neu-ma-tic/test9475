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

import java.util.HashMap;

public class Message {
	
	private String channel;
	private MessageFormat format;
	private String name;
	private String nick;
	private String server;
	private String message;
	private boolean discord;
	private boolean minecraft;
	private boolean console;
	private boolean redis;
	private HashMap<String, String> data;
	
	public Message setChannel(String channel) {
		this.channel = channel;
		return this;
	}
	
	public String getChannel() {
		return this.channel;
	}
	
	public Message setFormat(MessageFormat format) {
		this.format = format;
		return this;
	}
	
	public MessageFormat getFormat() {
		return this.format;
	}
	
	public Message setName(String name) {
		this.name = name;
		return this;
	}
	
	public String getName() {
		return this.name;
	}
	
	public Message setNick(String nick) {
		this.nick = nick;
		return this;
	}
	
	public String getNick() {
		return this.nick;
	}
	
	public Message setServer(String server) {
		this.server = server;
		return this;
	}
	
	public String getServer() {
		return this.server;
	}
	
	public Message setMessage(String message) {
		this.message = message;
		return this;
	}
	
	public String getMessage() {
		return this.message;
	}
	
	public Message setDiscord(boolean discord) {
		this.discord = discord;
		return this;
	}
	
	public boolean sendDiscord() {
		return this.discord;
	}
	
	public Message setMinecraft(boolean minecraft) {
		this.minecraft = minecraft;
		return this;
	}
	
	public boolean sendMinecraft() {
		return this.minecraft;
	}
	
	public Message setConsole(boolean console) {
		this.console = console;
		return this;
	}
	
	public boolean sendConsole() {
		return this.console;
	}
	
	public Message setRedis(boolean redis) {
		this.redis = redis;
		return this;
	}
	
	public boolean sendRedis() {
		return this.redis;
	}
	
	public Message setData(HashMap<String, String> data) {
		this.data = data;
		return this;
	}
	
	public HashMap<String, String> getData() {
		return this.data;
	}
}