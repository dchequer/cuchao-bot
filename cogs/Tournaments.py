import discord
from discord.ext import commands
from discord.ext import tasks

from src.__main__ import handler as logger
from src import constants

class Tournaments(commands.Cog):
    ROLES_MESSAGE_ID = 0
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def tournaments(self, ctx: commands.Context):
        await ctx.send('settings up tournaments')
    
    @commands.command()
    async def choose_roles(self, ctx: commands.Context):
        '''
        Send a message with a list of games and their corresponding emojis.
        Message is sent to the channel the command was sent in.
        '''
        embed = discord.Embed(title='Choose your roles', description='React with the games you like play', color=constants.Colours.blue)
        for emoji_name, emoji_code in zip(constants.Emojis.game_names, constants.Emojis.game_emojis):
            embed.add_field(name=emoji_name, value=emoji_code, inline=False)

        sent = await ctx.send(embed=embed, silent=True)
        self.ROLES_MESSAGE_ID = sent.id

        for emoji_code in constants.Emojis.game_emojis:        # add the emojis to the message
            await sent.add_reaction(emoji_code)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction: discord.Reaction, user: discord.User):
        if user.bot:                                            # ignore bots
            return
    
        if reaction.message.id == self.ROLES_MESSAGE_ID:        # check if the emoji is in the list of emojis
            if reaction.emoji.name not in constants.Emojis.game_names:
                await reaction.remove(user)
                return


            game_name = reaction.emoji.name                     # get the game name -> get id -> get role -> add role                    
            role_id = constants.Roles[game_name]
            role = self.bot.get_guild(constants.Guild.id).get_role(role_id)
            await user.add_roles(role, reason='User chose role', atomic=True)
    

async def setup(bot: commands.Bot):
    await bot.add_cog(Tournaments(bot))
    