import discord
import configparser
import os
from acbot.acbot import ACBot

config = configparser.ConfigParser()
config.read('config.ini')

bot = ACBot(command_prefix=config['bot']['command_prefix'])

# Load extensions
bot.load_extension('acbot.cogs.turnips')

bot.run(config['bot']['token'])
