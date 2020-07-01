from selenium import webdriver
from os import path
from os import getcwd
import time


local_path = path.abspath(getcwd())
driver_path = local_path+"/chromedriver" 

chrome = webdriver.Chrome(driver_path)
chrome.get("https://web.whatsapp.com/")

print("scan the QR code and press ENTER")
input("")
time.sleep(2)


group_name = "Testing"
group = chrome.find_element_by_xpath('//span[@title="{}"]'.format(group_name))
group.click()

type_field = chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
type_field.send_keys("This is a test.")

send_button = chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
send_button.click()

