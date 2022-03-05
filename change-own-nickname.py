import discord
from discord.ext import commands

bot = commands.Bot(description="A bot that changes the Users nickname by command", command_prefix="?")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("?Nick "):
        args = message.content.split("?Nick ")
        await message.author.edit(nick=args[1])

@bot.event
async def on_ready():
    print("Bot up and running!")


bot.run('')  # < Place ur Token in here
