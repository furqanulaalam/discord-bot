import discord
from discord.ext import commands, tasks
from csv import DictReader
from shutil import copyfile

bot = commands.Bot(command_prefix = '.')

@bot.event
async def on_ready():
    exec(open("scrape.py").read())
    copyfile('notifications.csv','old.csv')
    print("Bot is ready.")
    task.start()

#function for the bio command.
@bot.command()
async def bio(ctx):
    await ctx.send("Hello IUSTIANS! My name is NotiBot(pun intended). I was born on the 26th of July, 2020. I was created by Furkan Nul Aalam. In fact, it wouldn't be wrong to call him my father. My purpose in life is to get you the latest updates from the university website. I can also get you upto 25 notifications(chronologically) from the university website on demand. I will keep functioning until there aren't any drastic changes in the university website. I will look for updates on the university website once every 8 hours and if there are any, I will post them in the appropriate channel. Type '.nhelp' for help. I hope I can be of help to you all. Lastly, I hate people who think WhatsApp is better than Discord. \nThanks!")

#function for the help command.
@bot.command()
async def nhelp(ctx):
    await ctx.send("Here is the list of commands:-\n1. '.notify N' for the N lastest notifications from the university website.\n2.'.bio' for my bio.\n3.'.nhelp' for help.")

#function to get the N latest notifications from the university website.
@bot.command()
async def notify(ctx, *, n):
    try:
        n = int(n)
        if n > 0 and n <= 25:
            
            exec(open("scrape.py").read())
            with open('notifications.csv','r') as noti:
                
                csv_reader = DictReader(noti)
                i = 0
                
                for row in csv_reader:
                    await ctx.send(row['Notifications'])
                    await ctx.send(row['Links'])

                    i += 1

                    if i == n:
                        return 0  

        else:
            await ctx.send("Invalid input.")            

    except:
        await ctx.send("Invalid input.")

#checks the university website for updates every eight hours
@tasks.loop(hours=8)
async def task():
    channel = bot.get_channel(CHANNEL_ID)
    exec(open("scrape.py").read())
    
    stat = False
    with open('notifications.csv','r') as ne:
        new = DictReader(ne)
        
        with open('old.csv','r') as ol:
            old = DictReader(ol)
            
            for rowO in old:
                
                for rowN in new:
                    
                    if rowN != rowO:
                        stat = True
                        await channel.send(rowN['Notifications'])
                        await channel.send(rowN['Links'])
                    
                    else:
                        if stat:
                                copyfile('notifications.csv','old.csv')
                        return 0


bot.run('TOKEN')    

