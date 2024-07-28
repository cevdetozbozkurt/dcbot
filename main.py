import discord
from dotenv import load_dotenv
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

load_dotenv()
TOKEN = os.getenv("TOKEN")

@client.event
async def on_ready():
    print('We habe logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)
