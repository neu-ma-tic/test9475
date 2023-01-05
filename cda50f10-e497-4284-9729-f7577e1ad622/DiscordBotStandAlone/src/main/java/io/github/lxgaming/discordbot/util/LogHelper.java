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

import java.text.SimpleDateFormat;
import java.util.Calendar;

import io.github.lxgaming.discordbot.DiscordBot;

public class LogHelper {
	
	public static void info(String string) {
		System.out.println("[" + new SimpleDateFormat("HH:mm:ss").format(Calendar.getInstance().getTime()) + "] [Info] [" + Thread.currentThread().getName() + "]: " + string);
	}
	
	public static void warn(String string) {
		System.out.println("[" + new SimpleDateFormat("HH:mm:ss").format(Calendar.getInstance().getTime()) + "] [Warn] [" + Thread.currentThread().getName() + "]: " + string);
	}
	
	public static void error(String string) {
		System.out.println("[" + new SimpleDateFormat("HH:mm:ss").format(Calendar.getInstance().getTime()) + "] [Error] [" + Thread.currentThread().getName() + "]: " + string);
	}
	
	public static void debug(String string) {
		if (DiscordBot.getInstance().getConfig() != null && DiscordBot.getInstance().getConfig().isDebug()) {
			System.out.println("[" + new SimpleDateFormat("HH:mm:ss").format(Calendar.getInstance().getTime()) + "] [Debug] [" + Thread.currentThread().getName() + "]: " + string);
		}
	}
}