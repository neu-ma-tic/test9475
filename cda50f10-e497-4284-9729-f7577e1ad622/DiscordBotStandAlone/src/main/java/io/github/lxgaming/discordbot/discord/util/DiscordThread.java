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

package io.github.lxgaming.discordbot.discord.util;

import java.util.Iterator;

import io.github.lxgaming.discordbot.DiscordBot;
import io.github.lxgaming.discordbot.util.LogHelper;
import net.dv8tion.jda.core.entities.Message;

public class DiscordThread extends Thread {
	
	@Override
	public void run() {
		try {
			while (!Thread.currentThread().isInterrupted()) {
				process();
				Thread.sleep(5000);
			}
		} catch (InterruptedException ex) {
			LogHelper.error("Exception in DiscordThread!");
			ex.printStackTrace();
		}
	}
	
	private void process() {
		if (DiscordBot.getInstance().getDiscord().getMessageSender().getMessages() == null || DiscordBot.getInstance().getDiscord().getMessageSender().getMessages().isEmpty()) {
			return;
		}
		
		for (Iterator<Message> iterator = DiscordBot.getInstance().getDiscord().getMessageSender().getMessages().iterator(); iterator.hasNext();) {
			Message message = iterator.next();
			if (message == null || message.getCreationTime() == null) {
				iterator.remove();
				continue;
			}
			
			if (message.getCreationTime().toInstant().toEpochMilli() < (System.currentTimeMillis() - DiscordBot.getInstance().getConfig().getDeleteTime())) {
				message.delete().queue();
				iterator.remove();
			}
		}
		return;
	}
}