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

import com.sedmelluq.discord.lavaplayer.track.AudioTrack;

import net.dv8tion.jda.core.entities.Member;
import net.dv8tion.jda.core.entities.TextChannel;

public class Audio {
	
	private final TextChannel textChannel;
	private final Member member;
	private final AudioTrack audioTrack;
	private boolean played;
	
	public Audio(TextChannel textChannel, Member member, AudioTrack audioTrack) {
		this.textChannel = textChannel;
		this.member = member;
		this.audioTrack = audioTrack;
	}
	
	public TextChannel getTextChannel() {
		return textChannel;
	}
	
	public Member getMember() {
		return member;
	}
	
	public AudioTrack getAudioTrack() {
		return audioTrack;
	}
	
	public boolean hasPlayed() {
		return played;
	}
	
	public Audio setPlayed(boolean played) {
		this.played = played;
		return this;
	}
}