import configparser
import argparse
import requests
import praw 
import re
import os
class meme:
    def __init__(self):
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
        
        
    def parse(self,string):
        parser = argparse.ArgumentParser()
        req_args = parser.add_argument_group("required arguments")
        req_args.add_argument('-s',"--subreddit",type=str,help="The subreddit you want to download the image from",required=True)
        req_args.add_argument('-a',"--amount",type=int,help="The amount of images you want to download",required=True)
        req_args.add_argument('-t',"--time",type=str,help="Time frame  ",choices=["h","d","w","m","y"], required=True)
        
        try:
            args = parser.parse_args(string.split())
            self.sub = args.subreddit
            self.amount = args.amount
            self.time = args.time
            self.images_path = f'images/{self.sub}/'
            return self.start()
        except Exception as e:
            return e
    
    def help(self):
        message = "@JD meme [subreddit name] [time frame {h,d,w,m,a}] - Returns a meme from Reddit. If no subreddit given default is /memes"
        return message

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
                        return "image exists"
            if len(images):
                if not os.path.exists(self.images_path):
                    os.makedirs(self.images_path)
                self.download_images(images)
                    
        except Exception as e:
            print("download failed",e)