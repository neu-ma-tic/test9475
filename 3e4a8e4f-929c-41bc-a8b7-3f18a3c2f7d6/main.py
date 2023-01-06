import webhook
import multiprocessing
import os
import time

import discord
from replit import db

import commands
import routine
import server
import utils
import api
import notify

client = discord.Client()
chain = commands.get_all(
    commands.api_key(
        commands.reset_timer(
            commands.get_boss(
                commands.when_boss(
                    commands.sub_boss(
                        commands.unsub_boss(
                            commands.set_timer(commands.default()))))))))


@client.event
async def on_ready():
	utils.status(False)
	utils.logger('BOT: logged')
	for boss in utils.BOSSES:
		db[boss] = utils.get_timer(boss)


@client.event
async def on_message(message):
	if db['429']:
		utils.status(True)
		time.sleep(utils._429)
		utils.status(False)
		return

	if message.author == client.user or message.channel.name != 'timer-bot' or webhook.USERNAME in str(
	    message.author):
		return
	utils.logger(f'{message.author}: {message.content}')
	msg = utils.Message(message.content.split(' '), message.author)
	global chain
	msg_to_send = chain.send(msg)
	try:
		if msg_to_send['type'] == 'all':
			await message.channel.send(msg_to_send['msg'])
		elif msg_to_send['type'] == 'dm':
			await message.author.send(msg_to_send['msg'])
	except discord.errors.HTTPException as e:
		message_error = str(e)
		utils.logger(message_error)
		if '429' in message_error:
			utils.status(True)
			time.sleep(utils._429)
			utils.status(False)
		elif '50007' in message_error:
			api.delete(message.author.name)
			utils.logger('50007')
			await message.channel.send(
			    f'{message.author.mention} I can not dm you')


delete_logs = multiprocessing.Process(target=routine.delete_logs)
delete_logs.daemon = True
delete_logs.start()
server_s = multiprocessing.Process(target=server.run)
server_s.daemon = True
server_s.start()
if db['notifier']:
	notifier = multiprocessing.Process(target=notify.start_notifier)
	notifier.daemon = True
	notifier.start()
delete_old_timers = multiprocessing.Process(target=routine.delete_old_timers)
delete_old_timers.daemon = True
delete_old_timers.start()
try:
	client.run(os.getenv('TOKEN'))
except discord.errors.HTTPException as e:
	message_error = str(e)
	utils.logger(message_error)
	if '429' in message_error:
		utils.status(True)
		time.sleep(utils._429)
		utils.status(False)
