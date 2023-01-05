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

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import org.apache.commons.lang3.StringUtils;

import io.github.lxgaming.discordbot.DiscordBot;
import io.github.lxgaming.discordbot.discord.util.DiscordUtil;
import io.github.lxgaming.discordbot.entries.ICommand;
import io.github.lxgaming.discordbot.util.LogHelper;
import net.dv8tion.jda.core.entities.Member;
import net.dv8tion.jda.core.entities.Message;
import net.dv8tion.jda.core.entities.TextChannel;

public class Command {
	
	private List<ICommand> registeredCommands;
	
	public Command() {
		registeredCommands = new ArrayList<ICommand>();
	}
	
	public void registerCommands() {
		getRegisteredCommands().add(new ClearCommand());
		getRegisteredCommands().add(new HelpCommand());
		getRegisteredCommands().add(new InfoCommand());
		getRegisteredCommands().add(new JoinCommand());
		getRegisteredCommands().add(new NowPlayingCommand());
		getRegisteredCommands().add(new PlayCommand());
		getRegisteredCommands().add(new QueueCommand());
		getRegisteredCommands().add(new RemoveCommand());
		getRegisteredCommands().add(new RepeatCommand());
		getRegisteredCommands().add(new ShuffleCommand());
		getRegisteredCommands().add(new SkipCommand());
		getRegisteredCommands().add(new SourcesCommand());
		getRegisteredCommands().add(new StopCommand());
		getRegisteredCommands().add(new VolumeCommand());
	}
	
	public void execute(TextChannel textChannel, Member member, Message message) {
		List<String> arguments;
		if (message.getContent().startsWith(DiscordBot.getInstance().getConfig().getCommandPrefix())) {
			arguments = getValidArguments(DiscordUtil.filter(message.getContent().substring(DiscordBot.getInstance().getConfig().getCommandPrefix().length())).split(" "));
		} else {
			arguments = getValidArguments(DiscordUtil.filter(message.getContent().substring(1)).split(" "));
		}
		
		if (arguments == null || arguments.size() < 1) {
			return;
		}
		
		for (Iterator<ICommand> iterator = getRegisteredCommands().iterator(); iterator.hasNext();) {
			ICommand command = iterator.next();
			if (checkCommandName(arguments.get(0), command.getName()) || checkCommandAliases(arguments.get(0), command.getAliases())) {
				LogHelper.debug("Processing Command '" + message.getContent() + "' For '" + member.getEffectiveName() + "'.");
				arguments.remove(0);
				command.execute(textChannel, member, message, arguments);
				DiscordBot.getInstance().getDiscord().getMessageSender().addMessage(message);
				return;
			}
		}
	}
	
	private List<String> getValidArguments(String... arguments) {
		List<String> list = new ArrayList<String>();
		
		for (String string : arguments) {
			if (StringUtils.isBlank(string)) {
				continue;
			}
			list.add(string);
		}
		
		return list;
	}
	
	private boolean checkCommandName(String target, String name) {
		if (target == null || target.equals("") || name == null || name.equals("")) {
			return false;
		}
		
		if (target.equalsIgnoreCase(name)) {
			return true;
		}
		return false;
	}
	
	private boolean checkCommandAliases(String target, List<String> aliases) {
		if (aliases == null || aliases.isEmpty() || target == null || target.equals("")) {
			return false;
		}
		
		for (Iterator<String> iterator = aliases.iterator(); iterator.hasNext();) {
			String alias = iterator.next();
			if (target.equalsIgnoreCase(alias)) {
				return true;
			}
		}
		return false;
	}
	
	public List<ICommand> getRegisteredCommands() {
		return registeredCommands;
	}
}