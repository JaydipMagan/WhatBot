# WhatBot
Whatsapp bot for group chats. It uses web scraping to send messages to group chats.

# Dependencies 
## Python 3 
Use latest version of Python3

## Pip3 
Must have the lastest version of pip to install the python packages

## Chrome
Please use chrome as it is the most supported by Selenium. Will switch to FireFox ASAP.

To find out what version of Chrome you have
enter this in url search field `chrome://settings/help`

Use this link to download the corresponding drivers :
`https://sites.google.com/a/chromium.org/chromedriver/downloads`

Extract the driver into this directory.

## Selenium

To install Selenium `pip3 install selenium`

# How to run

You must have chromedriver in the same directory as main.py.

To run the bot give the name of the group chat and 0 or 1 if you want to use cache. Cache will just try use the existing user profile
on chrome so you don't have to keep scanning the QR code.

`python main.py name="group_name" cache=0" 

# Current features 
* @all - will send a @ to every member of the group chat

# Upcoming features 
* request meme from reddit - will go to a subreddit and download a meme
* create a meme - will allow you to make a meme using templates
* help command - will show the commands available

# Future work

Developing a bot which runs on android

Hosting the bot on a web server for 24/7 availability

Website to easily configure the bot
