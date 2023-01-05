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

import java.util.LinkedList;
import java.util.List;
import java.util.function.Consumer;

import io.github.lxgaming.discordbot.DiscordBot;
import net.dv8tion.jda.core.MessageBuilder;
import net.dv8tion.jda.core.entities.Message;
import net.dv8tion.jda.core.entities.MessageEmbed;
import net.dv8tion.jda.core.entities.TextChannel;

public class MessageSender {
	
	private List<Message> messages;
	
	public MessageSender() {
		messages = new LinkedList<Message>();
	}
	
	public void sendMessage(TextChannel textChannel, MessageEmbed messageEmbed, boolean autoDelete) {
		sendMessage(textChannel, new MessageBuilder().setEmbed(messageEmbed).build(), autoDelete);
	}
	
	public void sendMessage(TextChannel textChannel, Message message, boolean autoDelete) {
		textChannel.sendMessage(message).queue(new Consumer<Message>() {
			
			@Override
			public void accept(Message message) {
				if (DiscordBot.getInstance().getConfig().isDeleteMessages() && autoDelete) {
					getMessages().add(message);
				}
			}
		});
	}
	
	public void addMessage(Message message) {
		if (DiscordBot.getInstance().getConfig().isDeleteInvoking()) {
			getMessages().add(message);
		}
	}
	
	public List<Message> getMessages() {
		return messages;
	}
}