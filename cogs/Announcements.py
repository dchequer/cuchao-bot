import discord
from discord.ext import commands

class Announcements(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Announcements cog loaded')

    @commands.command()
    async def announce(self, ctx: commands.Context, *, content: str) -> None:
        '''Announces the content'''
        await ctx.send(content)

async def setup(bot):
    await bot.add_cog(Announcements(bot))

async def teardown(bot):
    await bot.remove_cog('Announcements')
