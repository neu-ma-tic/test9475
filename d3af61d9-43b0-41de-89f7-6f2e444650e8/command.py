from googleapi import *

class Command:
  def __init__(self, name, description, callback, num_args=1):
    self.name = name
    self.description = description
    self.callback = callback
    self.num_args = num_args

  async def run(self, channel, args):
    args_len = len(args)
    if args_len == self.num_args or args_len in self.num_args:
      await self.callback(channel, args)
      return

    await channel.send(f'{self.name} is called with incorrect number of arguments! (expected: {self.num_args})')

  async def on_help_callback(channel, args=None):
    async def print_command(command):
      await channel.send(f'{command.name} - {command.description}.')
    
    if len(args) == 0:
      for command in predefined_commands.values():
        await print_command(command)
      return

    command_name = args[0]
    if command_name is not None and command_name in predefined_commands:
      await print_command(predefined_commands[command_name])

  async def on_search_callback(channel, args):
    name = ''
    for arg in args:
      name += arg

    search_results = search(f'{name} смотреть онлайн')
    if search_results is None or search_results.number_of_results == 0:
      await channel.send(f'cannot find anything with the name: {name}.')
      return

    search_result = search_results[0]
    await channel.send(f'{search_result.name}: {search_result.google_link}\n{search_result.description}')

predefined_commands = {
  'help': Command('help', 'prints out list of commands', Command.on_help_callback, [0, 1]),
  'search': Command('search', 'looks up film / tv show by its name', Command.on_search_callback, 1),
}
