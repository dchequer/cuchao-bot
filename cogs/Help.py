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
        emojis = ctx.guild.emojis
        embed = discord.Embed(title='Emojis', description='List of emojis', color=0x00ff00)
        for emoji in emojis:
            embed.add_field(name=emoji.name, value=emoji.id, inline=True)
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot))