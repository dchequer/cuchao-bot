import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('General cog loaded')

    


def setup(bot):
    bot.add_cog(General(bot))