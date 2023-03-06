import discord
from discord.ext import commands
from discord.ext import tasks

from src.__main__ import handler as logger
from src import constants

class Tournaments(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def tournaments(self, ctx: commands.Context):
        await ctx.send('settings up tournaments')
    
    @commands.command()
    async def choose_roles(self, ctx: commands.Context, member: discord.Member):
        embed = discord.Embed(title='Choose your roles', description='React with the games you like play', color=constants.Colors.green)
        embed.add_field(name='Overwatch', value=constants.Emojis.overwatch, inline=True)

    

async def setup(bot: commands.Bot):
    await bot.add_cog(Tournaments(bot))
    