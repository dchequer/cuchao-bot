import discord
from discord.ext import commands

class Greetings(commands.Cog):
    WELCOME_GUILD_ID = 1078937524564656210
    def __init__(self, bot):
        self.bot = bot
        print('Greetings cog loaded')
    

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member) -> None:
        print(f'{member.display_name} has joined the server')
        channel = member.guild.get_channel(self.WELCOME_GUILD_ID)
        if channel is not None:
            await channel.send(f'Welcome {member.mention} to the server!')
            return
        print('No system channel found')

    @commands.command()
    async def test_embed(self, ctx: commands.Context) -> None:
        print('test_embed')
        embed = discord.Embed(title='Test', description='This is a test', color=0x00ff00)
        embed.add_field(name='Test', value='This is a test', inline=False)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def rules(self, ctx: commands.Context) -> None:
        embed = discord.Embed(title='Rules', description='These are the rules', color=0x00ff00)
        embed.add_field(name='Rule 1', value='No gays', inline=False)
        embed.add_field(name='Rule 2', value='Bueno solo adal', inline=False)
        embed.add_field(name='Rule 3', value='POGGGGG', inline=False)

        await ctx.send(embed=embed)
    

async def setup(bot):
    await bot.add_cog(Greetings(bot))

async def teardown(bot):
    await bot.remove_cog('Greetings')
    