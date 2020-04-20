import discord
import configparser
import os
import mongoengine as db
from acbot.acbot import ACBot

config = configparser.ConfigParser()
config.read('config.ini')

db.connect(
    config['db']['name'], 
    host=config['db']['host'], 
    port=int(config['db']['port']),
    username=config['db']['username'],
    password=config['db']['password'],
    authentication_source=config['db']['authentication_source']
)

bot = ACBot(command_prefix=config['bot']['command_prefix'])

# Load extensions
bot.load_extension('acbot.cogs.turnips')

bot.run(config['bot']['token'])
