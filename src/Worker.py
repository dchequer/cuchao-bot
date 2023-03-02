import discord
from discord.ext import commands
import json
import logging

from typing import Optional
from Questionnaire import Questionnaire
from discord import ui, app_commands

description = 'A bot that does stuff'
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

intents = discord.Intents.all()
cogs = ['Greetings', 'Roles', 'Announcements']
p = '+'
with open('prefix.txt') as f:
    p = f.read()

bot = commands.Bot(command_prefix='+', description=description, intents=intents)

@bot.event
async def on_ready() -> None:
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    #await dependencies()

@bot.command()
async def ping(ctx: commands.Context) -> None:
    '''Pong!'''
    await ctx.send('Pong!')

@bot.command()
async def echo(ctx: commands.Context, *, content: str) -> None:
    '''Echoes the content'''
    await ctx.send(content)

@bot.command()
async def prefix(ctx: commands.Context, *, prefix: Optional[str] = None) -> None:
    '''
    Changes the prefix if the user has the right permissions and one is given
    Otherwise, just returns the current prefix
    
    Parameters
    ----------
    prefix: str
        The new prefix

    Returns
    -------
    None
    '''
    if prefix is None:
        await ctx.send(f'Current prefix: {bot.command_prefix}')
        return
    
    bot.command_prefix = prefix
    with open('prefix.txt', 'w') as f:
        f.write(prefix)
    await ctx.send(f'Prefix changed to {prefix}')

@bot.command()
async def load(ctx: commands.Context, cog: str) -> None:
    '''
    Reloads an extension
    
    Parameters
    ----------
    cog: str
        The name of the cog to reload

    Returns
    -------
    None
    '''
    #print('loading extension', cog)
    await bot.load_extension(f'cogs.{cog}')

@bot.command()
async def unload(ctx: commands.Context, cog: str) -> None:
    '''
    Unloads an extension
    
    Parameters
    ----------
    cog: str
        The name of the cog to unload

    Returns
    -------
    None
    '''
    #print('unloading extension', cog)
    await bot.unload_extension(f'cogs.{cog}')

@bot.command()
async def reload(ctx: commands.Context, cog: str) -> None:
    '''
    Reloads an extension
    
    Parameters
    ----------
    cog: str
        The name of the cog to reload

    Returns
    -------
    None
    '''
    #print('reloading extension', cog)
    await unload(ctx, cog)
    await load(ctx, cog)

@bot.command()
async def load_all(ctx: commands.Context) -> None:
    '''
    Reloads all extensions
    
    Parameters
    ----------
    None

    Returns
    -------
    None
    '''
    #print('loading all extensions')
    for cog in cogs:
        await load(ctx, cog)

@bot.command()
async def unload_all(ctx: commands.Context) -> None:
    '''
    Unloads all extensions
    
    Parameters
    ----------
    None

    Returns
    -------
    None
    '''
    #print('unloading all extensions')
    for cog in cogs:
        await unload(ctx, cog)

@bot.command()
async def reload_all(ctx: commands.Context) -> None:
    '''
    Reloads all extensions
    
    Parameters
    ----------
    None

    Returns
    -------
    None
    '''
    #print('reloading all extensions')
    for cog in cogs:
        await reload(ctx, cog)

@bot.command(name='test', aliases=['q'], description='Starts a questionnaire')
async def test(ctx: commands.Context) -> None:
    '''Starts a questionnaire'''
    
    await ctx.interaction.response.send_modal(Questionnaire())



if __name__ == '__main__':
    with open('tokens.json') as f:
        tokens: dict = json.load(f)
        discord_token = tokens['discord token']
    handler: logging.FileHandler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

    bot.run(token=discord_token, reconnect=True, log_handler=handler, log_level=logging.DEBUG)


    