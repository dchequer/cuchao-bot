import discord
from discord.ext import commands

class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Roles cog loaded')

    @commands.command()
    async def addrole(self, ctx: commands.Context, role: discord.Role) -> None:
        '''Adds a role to the user'''
        await ctx.author.add_roles(role)
        await ctx.send(f'Added role {role.name}')

    @commands.command()
    async def removerole(self, ctx: commands.Context, role: discord.Role) -> None:
        '''Removes a role from the user'''
        await ctx.author.remove_roles(role)
        await ctx.send(f'Removed role {role.name}')

async def setup(bot):
    await bot.add_cog(Roles(bot))

async def teardown(bot):
    await bot.remove_cog('Roles')
