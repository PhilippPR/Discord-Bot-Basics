import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(description="A bot that shows how to edit a message send by the bot after a amount of time.", command_prefix="?")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == "?Send":
        themessage = await message.channel.send("> This is a message from the bot. (editing in 30 seconds)") # Sends the first message
        await asyncio.sleep(30) # let the bot wait 30 seconds
        await themessage.edit(content="> Now it's been 30 seconds.") # edit the message
        return


@bot.event
async def on_ready():
    print("Bot up and running!")

bot.run('')  # < Place ur Token in here
