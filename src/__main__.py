import discord
from discord.ext import commands
import json
import logging

from typing import Optional
from Questionnaire import Questionnaire
from discord import ui, app_commands

from src import constants

if __name__ == '__main__':
    intents = discord.Intents.all()
    intents.message_content = True
    intents.members = True

    allowed_roles = list({discord.Object(id_) for id_ in constants.MODERATION_ROLES})
    cogs = list({cog for cog in constants.COGS})

    bot = commands.Bot(
        command_prefix=constants.Bot.prefix,
        intents=intents,
        description=constants.Guild.description,
        allowed_mentions=discord.AllowedMentions(everyone=False, users=True, roles=allowed_roles)
    )
    handler: logging.FileHandler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

    bot.run(token=constants.Bot.token, reconnect=True, log_handler=handler, log_level=logging.DEBUG)
    for cog in cogs:
        bot.load_extension(cog)


    