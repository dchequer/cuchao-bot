import discord
from discord import ui, app_commands

class Questionnaire(ui.Modal, title='Questionnaire Response'):
    #name = ui.TextInput(label='Name')
    answer = ui.TextInput(label='Answer', style=discord.TextStyle.paragraph, placeholder='Enter your answer here', default='No answer given', required=True, min_length=1, max_length=2000)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Thanks for your response, {self.name}!', ephemeral=True)
