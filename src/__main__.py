
import logging

from src import constants
from src.bot import bot
from src.connection import *

# Set up logging
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))

# Run bot
print('Starting bot...')
if __name__ == '__main__':
    with open('token.txt', 'r') as f:
        token = f.read()
    bot.run(token=token, reconnect=False, log_handler=handler, log_level=logging.DEBUG)
