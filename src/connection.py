import discord
from discord.ext import commands, tasks

from src import constants
from src.bot import bot


@tasks.loop(count=1)
async def wait_until_ready() -> None:
    '''Event that waits until the bot is ready'''
    await bot.wait_until_ready()

    # Log bot information
    #logging.info(f'Logged in as {bot.user.name}#{bot.user.discriminator}')
    print(f'Logged in as {bot.user.name}#{bot.user.discriminator}')

    cogs = list({cog.value for cog in constants.Cogs})
    for cog in cogs:
        await bot.load_extension(cog)
    #logging.info(f'Loaded extension {cog}')
    print(f'Loaded extensions')
    return

@bot.event
async def on_connect() -> None:
    '''Event that runs when the bot connects to the Discord API'''

    # Log bot information
    #logging.info(f'Connected to Discord API')
    print(f'Connected to Discord API')

    return

@bot.event 
async def on_login() -> None:
    '''Event that runs when the bot logs in'''

    # Log bot information
    #logging.info(f'Logged in to Discord API')
    print(f'Logged in to Discord API')

    return

@bot.event
async def on_error(event, *args, **kwargs) -> None:
    '''Event that runs when an error occurs'''

    # Log error
    #logging.error(f'An error occurred: {event}')
    print(f'An error occurred: {event}')
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')

    return