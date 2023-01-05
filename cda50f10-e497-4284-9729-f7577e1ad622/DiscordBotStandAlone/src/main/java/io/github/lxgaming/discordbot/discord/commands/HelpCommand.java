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

package io.github.lxgaming.discordbot.discord.commands;

import java.util.Iterator;
import java.util.List;

import io.github.lxgaming.discordbot.DiscordBot;
import io.github.lxgaming.discordbot.discord.util.DiscordUtil;
import io.github.lxgaming.discordbot.entries.ICommand;
import net.dv8tion.jda.core.EmbedBuilder;
import net.dv8tion.jda.core.entities.Member;
import net.dv8tion.jda.core.entities.Message;
import net.dv8tion.jda.core.entities.TextChannel;

public class HelpCommand implements ICommand {
	
	@Override
	public void execute(TextChannel textChannel, Member member, Message message, List<String> arguments) {
		EmbedBuilder embedBuilder = new EmbedBuilder();
		embedBuilder.setAuthor(textChannel.getJDA().getSelfUser().getName(), null, textChannel.getJDA().getSelfUser().getEffectiveAvatarUrl());
		embedBuilder.setColor(DiscordUtil.DEFAULT);
		embedBuilder.setTitle("Commands", null);
		
		for (Iterator<ICommand> iterator = DiscordBot.getInstance().getDiscord().getCommand().getRegisteredCommands().iterator(); iterator.hasNext();) {
			ICommand command = iterator.next();
			StringBuilder stringBuilder = new StringBuilder();
			stringBuilder.append("Description - " + command.getDescription() + "\n");
			stringBuilder.append("Usage - " + command.getUsage() + "\n");
			
			if (command.getAliases() != null && !command.getAliases().isEmpty()) {
				stringBuilder.append("Aliases - " + String.join(", ", command.getAliases()));
			}
			embedBuilder.addField(command.getName(), stringBuilder.toString(), false);
		}
		
		embedBuilder.setFooter("<> = Required Argument, [] = Optional Argument", null);
		DiscordBot.getInstance().getDiscord().getMessageSender().sendMessage(textChannel, embedBuilder.build(), true);
	}
	
	@Override
	public String getName() {
		return "DJHelp";
	}
	
	@Override
	public String getDescription() {
		return "Displays helpful information.";
	}
	
	@Override
	public String getUsage() {
		return DiscordBot.getInstance().getConfig().getCommandPrefix() + "DJHelp";
	}
	
	@Override
	public List<String> getAliases() {
		return null;
	}
}