import discord
from discord.ext import commnads

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("The bot is running")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, i am pybot")