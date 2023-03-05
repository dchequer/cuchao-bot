import discord
from discord.ext import commands
from discord.ext import tasks

from src.__main__ import handler as logger

class Tournaments(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def tournaments(self, ctx: commands.Context):
        await ctx.send('settings up tournaments')
    

async def setup(bot: commands.Bot):
    await bot.add_cog(Tournaments(bot))
    