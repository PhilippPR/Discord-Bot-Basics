import discord
from discord.ext import commands

bot = commands.Bot(description="A bot to check the roles of a user.", command_prefix="?")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == "?Check":
        AdminRoleID = 791500005130633237 # Change this to your own role ID
        role = message.guild.get_role(AdminRoleID)
        if role in message.author.roles:
            await message.channel.send("You got the "+role.name+" role!")
        else:
            await message.channel.send("You don't have the "+role.name+" role!")


@bot.event
async def on_ready():
    print("Bot up and running!")

bot.run('') # < Place ur Token in here