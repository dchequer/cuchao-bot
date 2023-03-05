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

async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot))