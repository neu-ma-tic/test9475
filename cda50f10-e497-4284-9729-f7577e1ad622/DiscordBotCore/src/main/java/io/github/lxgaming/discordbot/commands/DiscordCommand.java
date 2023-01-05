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

package io.github.lxgaming.discordbot.commands;

import io.github.lxgaming.discordbot.DiscordBotCore;
import io.github.lxgaming.discordbot.entries.Message;
import net.dv8tion.jda.core.entities.Member;
import net.dv8tion.jda.core.entities.TextChannel;

public class DiscordCommand {
	
	public void execute(TextChannel channel, Member member, String command) {
		if (command.equalsIgnoreCase("botinfo")) {
			channel.sendMessage("DiscordBot - Bungeecord Edition, Version " + DiscordBotCore.getInstance().getConfiguration().getDiscordBotVersion() + ", Created by LX_Gaming\nJDA - " + DiscordBotCore.getInstance().getConfiguration().getJDAVersion()).queue();
			return;
		}
		
		if (command.equalsIgnoreCase("website")) {
			channel.sendMessage("``Website:`` **https://lxgaming.github.io/**\n``Source:`` **https://github.com/LXGaming/DiscordBot/**").queue();
			return;
		}
		
		DiscordBotCore.getInstance().getEventManager().onCommandReceived(new Message()
				.setChannel(channel.getId())
				.setFormat(DiscordBotCore.getInstance().getConfiguration().getCommandFormat().get(command.split(" ")[0]))
				.setName(member.getEffectiveName())
				.setNick(member.getNickname())
				.setMessage(command));
	}
}