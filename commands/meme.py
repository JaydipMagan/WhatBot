import configparser
import ArgumentParser
import requests
import praw 
import re
import os
    
class meme:
    def __init__(self):
        self.help_message = "meme - Returns a meme from Reddit."
        self.usage_message = "Incorrect usage. Try follow : meme [-s subreddit name] [-t time frame {h,d,w,m,a}]"
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
        self.images_path = 1
        
    def parse_args(self,string):
        print("got ",string)
        parser = ArgumentParser.ArgumentParser()
        req_args = parser.add_argument_group("required arguments")
        req_args.add_argument('-s',"--subreddit",type=str,help="The subreddit you want to download the image from",required=True)
        req_args.add_argument('-a',"--amount",type=int,help="The amount of images you want to download",required=False,default=1)
        req_args.add_argument('-t',"--time",type=str,help="Time frame  ",choices=["h","d","w","m","y"], required=True)
        
        try:
            args = parser.parse_args(string.split())
        except SystemExit as e:
            print(e)
            return ("error",self.usage_message)
        
        self.sub = args.subreddit
        self.amount = args.amount
        self.time = args.time
        self.images_path = f'images/{self.sub}/'
        return self.start()
    
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

    def start(self):
        images = []
        try:
            count = 0
            submissions = self.reddit.subreddit(self.sub).top(time_filter=self.timeframe[self.time])
            
            for submission in submissions:
                if not submission.stickied and submission.url.endswith(('jpg', 'jpeg', 'png')):
                    fname = self.images_path + re.search('(?s:.*)\w/(.*)', submission.url).group(1)
                    if not os.path.isfile(fname):
                        images.append({'url':submission.url,'fname':fname})
                        count+=1
                        if count>=self.amount:
                            break
                    else:
                        return ("image",fname)
            if len(images):
                if not os.path.exists(self.images_path):
                    os.makedirs(self.images_path)
                self.download_images(images)
                return ("image",fname)
                    
        except Exception as e:
            print(e)
            return ("error",e)