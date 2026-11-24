import discord
from dotenv import load_dotenv
import os
import random
import json
import logging

logging.basicConfig(level=logging.DEBUG)

with open("quotes.json", "r") as f: #changed directory
    quotes_list = json.load(f)

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print(f"logged as {client.user}")

@client.event
async def on_error(event, *args, **kwargs):
    print(f'Error in {event}')

@tree.command(name="quote", description="Gives a random Shortcat quote without context.")
async def quote(interaction: discord.Interaction):
    if interaction.user.id == 1400141944818110466 and random.random() > 0.953: #Catterby's ID
        embed_output = discord.Embed(
            title="Random Shortcat quote",
            description="Daisy noises?! That can mean different things to different people",
            color=discord.Color.from_rgb(231,181,69)
        )
    else:
        embed_output = discord.Embed(
            title="Random Shortcat quote",
            description=random.choice(quotes_list),
            color=discord.Color.from_rgb(231,181,69)
        )
    await interaction.response.send_message(embed=embed_output)

client.run(token)
