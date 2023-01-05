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

import java.util.UUID;

import io.github.lxgaming.discordbot.DiscordBotCore;

public class DatabaseManager {
	
	public boolean checkDatabase(UUID uniqueId) {
		if (DiscordBotCore.getInstance().getConfiguration().getDatabase().contains(uniqueId.toString())) {
			return true;
		}
		return false;
	}
	
	@Deprecated
	public boolean checkDatabase(String uniqueId) {
		if (DiscordBotCore.getInstance().getConfiguration().getDatabase().contains(uniqueId)) {
			return true;
		}
		return false;
	}
	
	public boolean togglePlayerDatabase(UUID uniqueId) {
		if (checkDatabase(uniqueId)) {
			DiscordBotCore.getInstance().getConfiguration().getDatabase().remove(uniqueId.toString());
			DiscordBotCore.getInstance().getEventManager().onDatabaseUpdate();
			return false;
		}
		
		DiscordBotCore.getInstance().getConfiguration().getDatabase().add(uniqueId.toString());
		DiscordBotCore.getInstance().getEventManager().onDatabaseUpdate();
		return true;
	}
}