import asyncio
import logging
from typing import List

import discord
from discord.ext import commands

from src import constants

# Set up intents
intents: discord.Intents = discord.Intents.all()
intents.message_content = True
intents.members = True
# Set up allowed roles
allowed_roles: List[object] = list({discord.Object(id_) for id_ in constants.MODERATION_ROLES})
# Set up cogs
cogs: List[str] = list({cog.value for cog in constants.Cogs})
# Set up bot
bot = commands.Bot(
    command_prefix=constants.Bot.prefix,
    intents=intents,
    description=constants.Bot.description,
    allowed_mentions=discord.AllowedMentions(everyone=False, users=True, roles=allowed_roles)
)

@bot.event
async def on_ready() -> None:
    '''Event that runs when the bot is ready'''

    # Load cogs
    for cog in cogs:
        await bot.load_extension(cog)

    # Set bot status
    await bot.change_presence(activity=discord.Game(name=constants.Bot.status))

    # Log bot information
    #logging.info(f'Logged in as {bot.user.name}#{bot.user.discriminator}')
    print(f'Logged in as {bot.user.name}#{bot.user.discriminator}')

    return

@bot.event
async def on_connect() -> None:
    '''Event that runs when the bot connects to the Discord API'''

    # Log bot information
    #logging.info(f'Connected to Discord API')
    print(f'Connected to Discord API')

    return

# Set up logging
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))


# Run bot
print('Starting bot...')
if __name__ == '__main__':
    with open('token.txt', 'r') as f:
        token = f.read()
    bot.run(token=token, reconnect=True, log_handler=handler, log_level=logging.DEBUG)
