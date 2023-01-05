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

import io.github.lxgaming.discordbot.DiscordBot;
import io.github.lxgaming.discordbot.entries.Group;
import net.dv8tion.jda.core.entities.Member;
import net.dv8tion.jda.core.entities.Role;

public class Permission {
	
	public boolean checkMember(Member member, String command) {
		Group group = findUserGroup(member);
		if (group == null) {
			return false;
		}
		
		if (group.isIgnoreNonVoice() && !member.getVoiceState().inVoiceChannel()) {
			return false;
		}
		
		if (!checkCommand(group, member, command)) {
			return false;
		}
		
		//TODO
		return false;
	}
	
	public boolean checkCommand(Group group, Member member, String command) {
		if (group == null || group.getUsers() == null || member == null || command == null) {
			return false;
		}
		
		if (group.getCommandWhitelist().contains(command) && !group.getCommandBlacklist().contains(command)) {
			return true;
		}
		return false;
	}
	
	private Group findUserGroup(Member member) {
		for (Group group : DiscordBot.getInstance().getConfig().getGroups()) {
			if (!group.getUsers().isEmpty() && group.getUsers().contains(member.getUser().getId())) {
				return group;
			}
			
			for (Role role : member.getRoles()) {
				if (!group.getRoles().isEmpty() && group.getRoles().contains(role.getId())) {
					return group;
				}
			}
		}
		return null;
	}
}