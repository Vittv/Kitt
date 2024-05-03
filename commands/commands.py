# COMMANDS:

@bot.command()
async def roll(ctx):
    # Lets the user roll a number from 1 to 100

    roll = randint(1, 100)
    await ctx.send(f'{ctx.author.display_name} rolled {roll}!')

est = pytz.timezone('America/New_York')
birthdays = []

@bot.command()
async def get_birthday(ctx):

    current_time_est = datetime.now(est)

    # Grabs the message's author
    user = ctx.author 

    await ctx.send('Please, type in your birthday (YYYY-MM-DD): ')
    try:
        message = await bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30)
        birthday_date = datetime.strptime(message.content, "%Y-%m-%d").date()
        birthdays.append((user, birthday_date))
        await ctx.send(f'Thank you, {user.mention}. Your birthday has been recorded.')
        return birthday_date
    
    except ValueError:
        print('Invalid date format. Please enter your birthday in (YYYY-MM-DD): ')