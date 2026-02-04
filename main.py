import discord
from dotenv import load_dotenv
import os
import random
import json

with open("quotes.json", "r") as f:
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

@tree.command(name="quote", description="Gives a random Shortcat quote without context.")
async def quote(interaction: discord.Interaction):
    embed_output = discord.Embed(
        title="Random Shortcat quote",
        description=f"\"{random.choice(quotes_list)}\"",
        color=discord.Color.from_rgb(231,181,69)
    )
    await interaction.response.send_message(embed=embed_output)

client.run(token)
