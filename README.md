# WhatBot
Whatsapp bot for group chats. It uses web scraping to send messages to group chats.

# Dependencies 

Package dependencies can be found in the `requirements.txt` file.
## Chrome
Please use chrome as it is the most supported by Selenium. Will switch to FireFox ASAP.

To find out what version of Chrome you have
enter this in url search field :

`chrome://settings/help`

Use this link to download the corresponding drivers :

`https://sites.google.com/a/chromium.org/chromedriver/downloads`

Extract the driver into this directory.

# How to run

1.Create a virtual enviroment : 

`python3 -m venv whatbot_env`

2.Activate the virtual enviroment :

`source whatbot_env/bin/activate`

3.You must have chromedriver in the same directory as main.py. Make sure it is called `chromedriver`

4.Install the python packages using the requirements file:

`pip3 install -r requirements.txt`

5.Please put your reddit app client id and client secret in the `conf.ini` file. Use the link below to create a new one.

`https://old.reddit.com/prefs/apps/`

6.Run the bot give the name of the group chat the --cache flag. Cache will just 
try use the existing user profile on chrome so you don't have to keep scanning the QR code.
Example :

`python3 main.py "group name" -c`

You can specify your OS using the -s flag by default it is linux.

`python main.py "group name" -c -s mac`

7.Deactivate the virtual enviroment after running bot just run :

`deactivate`

# Current features 
* help command - will show the commands available
* @all - will send a @ to every member of the group chat
* request meme from reddit - will go to a subreddit and download a meme
* create a meme - will allow you to make a meme using templates

# Upcoming features 
* request football scores - will allow you to get latest scores or for specific football team

# Future work

Developing a bot which runs on android

Hosting the bot on a web server for 24/7 availability

Website to easily configure the bot
