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

public class Group {
	
	private String name;
	private List<String> commandBlacklist;
	private List<String> commandWhitelist;
	private List<String> roles;
	private List<String> users;
	private boolean ignoreNonVoice;
	private int maxSongs;
	private int maxSongLength;
	private boolean allowPlaylists;
	private int maxPlaylistLength;
	private int skipsRequired;
	private double skipRatio;
	private boolean instantSkip;
	
	public String getName() {
		return name;
	}
	
	public List<String> getCommandBlacklist() {
		return commandBlacklist;
	}
	
	public List<String> getCommandWhitelist() {
		return commandWhitelist;
	}
	
	public List<String> getRoles() {
		return roles;
	}
	
	public List<String> getUsers() {
		return users;
	}
	
	public boolean isIgnoreNonVoice() {
		return ignoreNonVoice;
	}
	
	public int getMaxSongs() {
		return maxSongs;
	}
	
	public int getMaxSongLength() {
		return maxSongLength;
	}
	
	public boolean isAllowPlaylists() {
		return allowPlaylists;
	}
	
	public int getMaxPlaylistLength() {
		return maxPlaylistLength;
	}
	
	public int getSkipsRequired() {
		return skipsRequired;
	}
	
	public double getSkipRatio() {
		return skipRatio;
	}
	
	public boolean isInstantSkip() {
		return instantSkip;
	}
}