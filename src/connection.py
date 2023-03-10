import discord
from discord.ext import commands, tasks

from src import constants
from src.bot import bot
from src.__main__ import handler as logger 


@bot.event
async def on_ready() -> None:
    '''Event that runs when the bot is ready'''
    # Log bot information
    #bot.logger.info(f'Logged in as {bot.user.name}#{bot.user.discriminator}')
    print(f'Logged in as {bot.user.name}#{bot.user.discriminator}')

    cog_names = list({cog.value for cog in constants.Cogs})
    for cog_name in cog_names:
        await bot.load_extension(f'cogs.{cog_name}')

@bot.command(name='reload')
async def reload_all(ctx: commands.Context):
    cogs = list({cog.value for cog in constants.Cogs})
    for cog in cogs:
        await bot.unload_extension(f'cogs.{cog}')
        await bot.load_extension(f'cogs.{cog}')
    await ctx.send('Reloaded all cogs')