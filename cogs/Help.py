import discord
from discord.ext import commands
from discord.ext import tasks

from src import constants

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        await ctx.send('help')

def setup(bot):
    bot.add_cog(Help(bot))