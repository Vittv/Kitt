import discord
from discord.ext import commands
from discord.ext import tasks
from random import randint
from datetime import datetime
from main import birthdays
import pytz

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix=">", intents=intents)


@tasks.loop(hours=12)
# Checks for birthdays every 12 hours
async def check_birthdays():

    today = datetime.now(est).date()
    for user, birthday in birthdays:

        if birthday.month == today.month and birthday.day == today.day:

            channel = bot.get_channel('CHANNEL_TOKEN')  
            await channel.send(f'Happy Birthday, {user.mention}! >w<\nHope you have a great day!')


# Runs the bot
bot.run()
