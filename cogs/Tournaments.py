import discord
from discord.ext import commands

class Tournaments(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tournaments(self, ctx):
        await ctx.send('settings up tournaments')
    

def setup(bot):
    bot.add_cog(Tournaments(bot))
    