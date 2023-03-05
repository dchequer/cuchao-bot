import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('General cog loaded')

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready')
        print(f'Logged in as {self.bot.user.name}#{self.bot.user.discriminator}')



def setup(bot):
    bot.add_cog(General(bot))