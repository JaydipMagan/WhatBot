from selenium import webdriver
from selenium.webdriver.common.by import By
from os import path
from os import getcwd
from getpass import getuser
import time


def read_latest_msg(group_name):
    group = chrome.find_element_by_xpath('//span[@title="{}"]'.format(group_name))
    group.click()

    msg_in = chrome.find_elements(By.CLASS_NAME,"message-in")[-1]
    msg_span = msg_in.find_element(By.CLASS_NAME,"eRacY")
    print(msg_span.text)

def read_msgs(group_name):
    group = chrome.find_element_by_xpath('//span[@title="{}"]'.format(group_name))
    group.click()

    msgs_in = chrome.find_elements(By.CLASS_NAME,"message-in")
    for msg in msgs_in:
        msg_span = msg.find_element(By.CLASS_NAME,"eRacY")
        print(msg_span.text)

def send_msg(message,group_name):
    group = chrome.find_element_by_xpath('//span[@title="{}"]'.format(group_name))
    group.click()

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

    stop = False
    while not stop:
        # send_msg(input("message?"),"Testing")
        read_latest_msg("Testing")
        if input("stop?")=="y":
            stop = True

    chrome.close()
