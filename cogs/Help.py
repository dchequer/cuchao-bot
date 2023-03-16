from typing import List, Tuple
import discord
from discord.ext import commands
from discord.ext import tasks

from src import constants
from src.__main__ import handler as logger

class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx: commands.Context):
        await ctx.send('help')
    
    @commands.command(name='emojis')
    async def get_emojis(self, ctx: commands.Context):
        '''Show a list of emojis'''
        #emojis: List[Tuple[str, str]] = constants.Emojis            # List of emojis, each emoji is a tuple of (name, emoji)
        emojis = ctx.guild.emojis
        print(emojis)
        embed: discord.Embed = discord.Embed(title='Emojis', description='List of emojis', color=0xcb0b7a)

        for emoji_name, emoji_code in emojis:
            embed.add_field(name=emoji_name, value=emoji_code, inline=False)
        
        await ctx.send(embed=embed, silent=True)

    @commands.command(name='status')
    async def new_status(self, ctx: commands.Context, status: str):
        '''Change the bot's status'''
        await self.bot.change_presence(activity=discord.Game(status))


async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot))