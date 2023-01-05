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

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import io.github.lxgaming.discordbot.entries.AbstractDiscordBotListener;
import io.github.lxgaming.discordbot.entries.Message;

public class EventManager extends AbstractDiscordBotListener {
	
	private List<AbstractDiscordBotListener> listeners;
	
	public EventManager() {
		listeners = new ArrayList<AbstractDiscordBotListener>();
	}
	
	public void addListener(AbstractDiscordBotListener listener) {
		this.listeners.add(listener);
	}
	
	private List<AbstractDiscordBotListener> getListeners() {
		return this.listeners;
	}
	
	@Override
	public void onMessageMinecraft(Message message) {
		for (Iterator<AbstractDiscordBotListener> iterator = getListeners().iterator(); iterator.hasNext();) {
			AbstractDiscordBotListener listener = iterator.next();
			listener.onMessageMinecraft(message);
		}
	}
	
	@Override
	public void onCommandRegister(String name, String command, String permission, String... aliases) {
		for (Iterator<AbstractDiscordBotListener> iterator = getListeners().iterator(); iterator.hasNext();) {
			AbstractDiscordBotListener listener = iterator.next();
			listener.onCommandRegister(name, command, permission, aliases);
		}
	}
	
	@Override
	public void onDatabaseUpdate() {
		for (Iterator<AbstractDiscordBotListener> iterator = getListeners().iterator(); iterator.hasNext();) {
			AbstractDiscordBotListener listener = iterator.next();
			listener.onDatabaseUpdate();
		}
	}
}