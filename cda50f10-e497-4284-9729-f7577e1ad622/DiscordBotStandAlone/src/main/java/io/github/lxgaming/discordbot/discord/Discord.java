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

package io.github.lxgaming.discordbot.discord;

import javax.security.auth.login.LoginException;

import com.sedmelluq.discord.lavaplayer.player.AudioPlayer;
import com.sedmelluq.discord.lavaplayer.player.AudioPlayerManager;
import com.sedmelluq.discord.lavaplayer.player.DefaultAudioPlayerManager;
import com.sedmelluq.discord.lavaplayer.source.AudioSourceManagers;

import io.github.lxgaming.discordbot.DiscordBot;
import io.github.lxgaming.discordbot.discord.commands.Command;
import io.github.lxgaming.discordbot.discord.listeners.AudioListener;
import io.github.lxgaming.discordbot.discord.listeners.DiscordListener;
import io.github.lxgaming.discordbot.discord.util.AudioQueue;
import io.github.lxgaming.discordbot.discord.util.DiscordThread;
import io.github.lxgaming.discordbot.discord.util.MessageSender;
import io.github.lxgaming.discordbot.util.LogHelper;
import net.dv8tion.jda.core.AccountType;
import net.dv8tion.jda.core.JDA;
import net.dv8tion.jda.core.JDABuilder;
import net.dv8tion.jda.core.exceptions.RateLimitedException;

public class Discord {
	
	private JDA jda;
	private Command command;
	private AudioPlayerManager audioPlayerManager;
	private AudioPlayer audioPlayer;
	private AudioQueue audioQueue;
	private MessageSender messageSender;
	private DiscordThread discordThread;
	
	public Discord() {
		command = new Command();
		audioPlayerManager = new DefaultAudioPlayerManager();
		audioQueue = new AudioQueue();
		messageSender = new MessageSender();
		discordThread = new DiscordThread();
	}
	
	public void loadDiscord() {
		try {
			jda = new JDABuilder(AccountType.BOT)
					.setToken(DiscordBot.getInstance().getConfig().getToken())
					.addEventListener(new DiscordListener())
					.setAudioEnabled(true)
					.setBulkDeleteSplittingEnabled(false)
					.buildAsync();
			
			AudioSourceManagers.registerRemoteSources(getAudioPlayerManager());
			audioPlayer = getAudioPlayerManager().createPlayer();
			getAudioPlayer().setVolume(DiscordBot.getInstance().getConfig().getDefaultVolume());
			getAudioPlayer().addListener(new AudioListener());
			getDiscordThread().start();
			getCommand().registerCommands();
			LogHelper.info("Successfully loaded Discord.");
		} catch (LoginException | RateLimitedException | RuntimeException ex) {
			LogHelper.error("Exception loading Discord!");
			ex.printStackTrace();
		}
	}
	
	public JDA getJDA() {
		return jda;
	}
	
	public Command getCommand() {
		return command;
	}
	
	public AudioPlayerManager getAudioPlayerManager() {
		return audioPlayerManager;
	}
	
	public AudioPlayer getAudioPlayer() {
		return audioPlayer;
	}
	
	public AudioQueue getAudioQueue() {
		return audioQueue;
	}
	
	public MessageSender getMessageSender() {
		return messageSender;
	}
	
	public DiscordThread getDiscordThread() {
		return discordThread;
	}
}