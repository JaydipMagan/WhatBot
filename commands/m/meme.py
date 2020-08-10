import configparser
import ArgumentParser
import requests
import praw 
import re
import os
import random 

class meme:
    def __init__(self):
        self.help_message = "meme - Returns a meme from Reddit."
        self.usage_message = "Try follow : meme [subreddit name] [-t time frame {h,d,w,m,a}] [-o order {top,new,hot}]"
        self.name = "meme"
        
        config = configparser.ConfigParser()
        config.read("conf.ini")
        self.reddit = praw.Reddit(client_id=config['REDDIT']['client_id'],
                                  client_secret=config['REDDIT']['client_secret'],
                                  user_agent='Whatbot by u/JaydipMagan')
        self.timeframe = {'h': "hour",
                          'd': "day",
                          'w': "week",
                          'm': "month",
                          'y': "year",
                          'a': "all"}
        self.sub = "memes"
        self.time = "h"
        self.amount = 1
        self.order = None
        self.images_path = f'commands/m/images/{self.sub}/'
        
    def parse_args(self,string):
        print("got ",string)
        if string=="":
            return self.random()
        parser = ArgumentParser.ArgumentParser()
        pos_args = parser.add_argument_group("Positional arguments")
        opt_args = parser.add_argument_group("Optional arguments")
        pos_args.add_argument("subreddit",type=str,help="The subreddit you want to download the image from",default="memes")
        opt_args.add_argument('-a',"--amount",type=int,help="The amount of images you want to download",required=False,default=1)
        opt_args.add_argument('-t',"--time",type=str,help="Time frame",choices=["h","d","w","m","y"], required=False,default="h")
        opt_args.add_argument('-o',"--order",type=str,help="Order",choices=["new","top","hot"], required=False)
        
        try:
            args = parser.parse_args(string.split())
        except SystemExit as e:
            # print(e)
            return {"media":"error","text":self.usage_message,"media_location":""}
        
        self.sub = args.subreddit
        self.amount = args.amount
        self.time = args.time
        self.order = args.order
        self.images_path = f'commands/m/images/{self.sub}/'
        
        if self.order==None or self.order=="top":
            return self.top()
        elif self.order=="new":
            return self.new()
        elif self.order=="hot":
            return self.hot()
    
    def help_message(self):
        return self.help_message

    def download_images(self,images):
        for image in images:
            self.download_image(image)
            
    def download_image(self,image):
        print("downloading image...")
        r = requests.get(image['url'])
        with open(image['fname'],'wb') as f:
            f.write(r.content)
        print("Download complete")
        
    def get_link(self,submission):
        if not submission.stickied and submission.url.endswith(('jpg', 'jpeg', 'png')) and not submission.over_18:
            author_name = "u/"+submission.author.name if submission.comments else ""
            fname = self.images_path + re.search('(?s:.*)\w/(.*)', submission.url).group(1)
            return {"url":submission.url,"fname":fname,"author":author_name}

    def get_image(self,order):
        images = []
        orders = {"top":self.reddit.subreddit(self.sub).top(time_filter=self.timeframe[self.time]),
                  "new":self.reddit.subreddit(self.sub).new(),
                  "hot":self.reddit.subreddit(self.sub).hot()}
        try:
            count = 0
            submissions = orders[order]
            for submission in submissions:
                if submission.over_18:
                    return {"media":"text","text":"We don't do that here...Yet!","media_location":""}
                    
                if not submission.stickied and submission.url.endswith(('jpg', 'jpeg', 'png')):
                    author_name = "u/"+submission.author.name
                    fname = self.images_path + re.search('(?s:.*)\w/(.*)', submission.url).group(1)
                    if not os.path.isfile(fname):
                        images.append({'url':submission.url,'fname':fname,'author':author_name})
                        count+=1
                        if count>=self.amount:
                            break
                    else:
                        return {"media":"image-text","text":author_name,"media_location":fname}
                    
            if len(images):
                if not os.path.exists(self.images_path):
                    os.makedirs(self.images_path)
                self.download_images(images)
                return {"media":"image-text","text":images[0]['author'],"media_location":images[0]['fname']}
                    
        except Exception as e:
            print(e)
            return {"media":"error","text":e,"media_location":""}
        
    def random(self):
        submissions = self.reddit.subreddit(self.sub).top(time_filter=self.timeframe[self.time],limit=10)
        image_links = list(map(self.get_link,submissions))
        random_int = random.randint(0,len(image_links))
        image = image_links[random_int]
        if not os.path.exists(self.images_path):
            os.makedirs(self.images_path)
        self.download_image(image)
        return {"media":"image-text","text":image["author"],"media_location":image["fname"]}
    
    def top(self):
        return self.get_image("top")    
    
    def new(self):
        return self.get_image("new")

    def hot(self):
        return self.get_image("hot")