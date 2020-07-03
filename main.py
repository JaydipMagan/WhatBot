from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from os import path
from os import getcwd
from getpass import getuser
from group import group
import time
import sys

#Uses the search bar to find and open chat
def open_chat(name):
    search_field = chrome.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    search_field.send_keys()

    chat = chrome.find_element_by_xpath('//span[@title="{}"]'.format(name))
    chat.click()

def read_latest_msg(group_name):
    msg_in = chrome.find_elements(By.CLASS_NAME,"message-in")[-1]
    msg_span = msg_in.find_element(By.CLASS_NAME,"eRacY")
    print(msg_span.text)

def read_msgs(group_name):
    open_chat(group_name)

    msgs_in = chrome.find_elements(By.CLASS_NAME,"message-in")
    for msg in msgs_in:
        msg_span = msg.find_element(By.CLASS_NAME,"eRacY")
        print(msg_span.text)

# opens chat and sends message
def send_msg(message,group_name):
    open_chat(group_name)

    type_field = chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    type_field.send_keys(message)

    send_button = chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
    send_button.click()

if __name__ == "__main__":
    # construct paths 
    user = getuser()
    local_path = path.abspath(getcwd())
    driver_path = local_path+"/chromedriver" 
    chrome_profile_linux = '/home/{}/.config/google-chrome/default'.format(user)
    chrome_profile_mac = '/Users/{}/Library/Application Support/Google/Chrome/Default'.format(user)
    # chrome_profile_win = 'C:\Users\{}\AppData\Local\Google\Chrome\User Data\Default'.format(user)

    if len(sys.argv)!=3:
        print("Not enough arguments given. python main.py name='group name' cache=0/1")

    # Set options and use cache of the chrome browser
    if sys.argv[2]=="cache=1":
        options = webdriver.ChromeOptions()
        options.add_argument('--user-data-dir='+chrome_profile_linux)
        options.add_argument('--profile-directory=Default')

    # open chrome and whatsapp
    chrome = webdriver.Chrome(driver_path,options=options)
    chrome.get("https://web.whatsapp.com/")

    print("press ENTER once whatsapp has loaded.")
    input("")

    group_name = sys.argv[1].lstrip("name=")
    open_chat(group_name)
    group = group(group_name,chrome)
    print(group.name,group.birth,group.desc,group.size)
    stop = False    
    while not stop:
        group.read_latest_msg(chrome)
    chrome.close()
