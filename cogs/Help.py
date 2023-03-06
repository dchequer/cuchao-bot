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
        emojis: List[Tuple[str, str]] = constants.Emojis            # List of emojis, each emoji is a tuple of (name, emoji)
        embed = discord.Embed(title='Emojis', description='List of emojis', color=0xcb0b7a)
        #embed.set_image(url="https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg")
        #embed.set_thumbnail(url="https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aHVtYW58ZW58MHx8MHx8&w=1000&q=80")
        #print(emojis)
        for emoji_name, emoji_code in emojis:
            print(emoji_name, emoji_code)
            embed.add_field(name=emoji_name, value=emoji_code, inline=False)
        await ctx.send(embed=embed, silent=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot))