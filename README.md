NotiBot - A Discord bot for my class server

NotiBot is a bot that posts updates from my university website (http://iustlive.com/Index/Default.aspx) on the 'Updates' channel of the server.
It looks for updates on the website once every eight hours and if there are any, it posts them.
It also allows the members of the servers to get upto 25 latest posts from the university website on demand by using specific commands.
For this project, I used Python 3.8 along with the following external libraries(I have not mentioned their dependencies):
BeautifulSoup4, discord.py, requests and lxml. For a detailed list, see 'requirements.txt'(It includes every library/framework that I have installed in my Python environment when only a few of them are required to get the bot running. So, forgive me for that. I didn't do the project in a separate virtual environment.). 

My project runs two Python scripts, 'scrape.py' and 'bot.py'. 'scrape.py' scrapes the latest posts from the university website and stores the results in a csv file.
'bot.py' is the main bot script. It calls 'scrape.py' whenever needed and handles the functioning of the bot.
I have removed the channel ID and the token from 'bot.py' for obvious reasons.

Well, that is about it. Wander through the code for more.

Thank you!

