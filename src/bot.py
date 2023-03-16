from typing import List

import discord
from discord.ext import commands

from src import constants

# Set up intents
intents: discord.Intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True
# Set up allowed roles
allowed_roles: List[object] = list({discord.Object(id_) for id_ in constants.MODERATION_ROLES})
# Set up bot
bot: commands.Bot = commands.Bot(
    command_prefix=constants.Bot.prefix,
    intents=discord.Intents.all(),
    help_command=None
)
