# EVENTS:

@bot.event
async def on_member_join(member:discord.member):
    # Greets new members as they join the server
    channel = bot.get_channel('CHANNEL_TOKEN')
    await channel.send(f'Welcome {member.display_name}!')

@bot.event
async def on_member_remove(member:discord.member):
    # Notifies when someone leaves the server
    channel = bot.get_channel('CHANNEL_TOKEN')
    await channel.send(f'{member.display_name} left the server.')

@bot.event
async def on_ready():
    print('Bot is ready.')
    check_birthdays.start()