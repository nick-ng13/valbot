import discord
import responses
import os

from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('C:/Users/Nicholas/Desktop/valbot/secrets.env')
load_dotenv(dotenv_path=dotenv_path)

KEY = 'DISCORD_TOKEN'
DISCORD_TOKEN = os.getenv(KEY)

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    bot = discord.Client(intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running!')

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
                
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    bot.run(DISCORD_TOKEN)