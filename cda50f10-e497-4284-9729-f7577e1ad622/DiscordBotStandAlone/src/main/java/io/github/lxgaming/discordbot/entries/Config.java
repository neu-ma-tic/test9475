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

import java.util.List;

public class Config {
	
	private boolean debug;
	private String commandPrefix;
	private String guildId;
	private String token;
	private int defaultVolume;
	private boolean deleteMessages;
	private boolean deleteInvoking;
	private int deleteTime;
	private List<Group> groups;
	private List<String> allowedSources;
	
	public boolean isDebug() {
		return debug;
	}
	public String getCommandPrefix() {
		return commandPrefix;
	}
	
	public String getGuildId() {
		return guildId;
	}
	
	public String getToken() {
		return token;
	}
	
	public int getDefaultVolume() {
		return defaultVolume;
	}
	
	public boolean isDeleteMessages() {
		return deleteMessages;
	}
	
	public boolean isDeleteInvoking() {
		return deleteInvoking;
	}
	
	public int getDeleteTime() {
		return deleteTime;
	}
	
	public List<Group> getGroups() {
		return groups;
	}
	
	public List<String> getAllowedSources() {
		return allowedSources;
	}
}