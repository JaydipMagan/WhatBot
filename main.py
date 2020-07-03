from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from os import path
from os import getcwd
from getpass import getuser
import time

# find the total number of members in the group
def find_total_memebers():
    group_header = chrome.find_element_by_xpath('//*[@id="main"]/header')
    group_header.click()
    close_button = chrome.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/header/div/div[1]/button')
    time.sleep(0.5)
    total = chrome.find_element_by_css_selector('#app > div > div > div.YD4Yw > div._1-iDe._14VS3 > span > div > span > div > div > div._1TM40 > div:nth-child(5) > div._1Gecv > div > div > div._3HPyS._1e77x')
    close_button.click()
    return total.text

# @ everyone in the group chat
def at_all():
    type_field = chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    actions = ActionChains(chrome) 
    for i in range(total_members-1):
        actions.send_keys("@")
        actions.send_keys(Keys.ARROW_DOWN*i)
        actions.send_keys(Keys.TAB)
    actions.perform()
    type_field.send_keys(Keys.ENTER)

#Get all the participants name
def get_names():
    div = chrome.find_element_by_class_name('_3xjAz')
    span = div.find_element_by_class_name('_3Whw5')

    # create the list of names because get_attribute function doesnt return correct format
    names = []
    buffer = ""
    for c in span.get_attribute('title'):
        print(c)
        if c==",":
            names.append(buffer.lstrip(" "))
            buffer=""
        else:
            buffer+=c
    return names

#Uses the search bar to find and open chat
def open_chat(name):
    search_field = chrome.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    search_field.send_keys()

    chat = chrome.find_element_by_xpath('//span[@title="{}"]'.format(name))
    chat.click()

def read_latest_msg(group_name):
    msg_in = chrome.find_elements(By.CLASS_NAME,"message-in")[-1]
    msg_span = msg_in.find_element(By.CLASS_NAME,"eRacY")
    msg_hash = hash(msg_span.text)
    if msg_span.text[:3]=="@JD":
        print("bot called")
    if msg_span.text=="@all" and prev_msg!=msg_hash:
        print("detected")
        at_all()
    return msg_hash
def read_msgs(group_name):
    open_chat(group_name)

    msgs_in = chrome.find_elements(By.CLASS_NAME,"message-in")
    for msg in msgs_in:
        msg_span = msg.find_element(By.CLASS_NAME,"eRacY")


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

    # Set options and use cache of the chrome browser
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir='+chrome_profile_linux)
    options.add_argument('--profile-directory=Default')

    # open chrome and whatsapp
    chrome = webdriver.Chrome(driver_path,options=options)
    chrome.get("https://web.whatsapp.com/")

    print("press ENTER once whatsapp has loaded.")
    input("")

    open_chat("Preets mango lassis")
    total_members = int(find_total_memebers().rstrip(" participants"))
    print(total_members)
    stop = False    
    prev_msg = 0
    while not stop:
        msg = read_latest_msg("Preets mango lassis")
        prev_msg = msg
    chrome.close()
