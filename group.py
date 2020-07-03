from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
class group:
    def __init__(self,name,chrome):
        print("Creating group object")
        group_header = chrome.find_element_by_xpath('//*[@id="main"]/header')
        group_header.click()
        close_button = chrome.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/header/div/div[1]/button')
        time.sleep(0.5)
        self.name = name
        self.birth = self.find_birth(chrome)
        self.desc = self.find_desc(chrome)
        self.size = self.find_size(chrome)
        self.prev_msg = 0
        close_button.click()
    
    # find the date and time the group chat was created
    def find_birth(self,chrome):
        birth = chrome.find_element_by_css_selector('#app > div > div > div.YD4Yw > div._1-iDe._14VS3 > span > div > span > div > div > div._1TM40 > div._2Bps4._1mTqm._1pDAt > div._1005i > span')
        return birth.text

    # find the date and time the group chat was created
    def find_desc(self,chrome):
        desc = chrome.find_element_by_css_selector('#app > div > div > div.YD4Yw > div._1-iDe._14VS3 > span > div > span > div > div > div._1TM40 > div._2Bps4._1mTqm._2nM3G > div._24nYt > div > div')
        return desc.text

    # find the total number of members in the group
    def find_size(self,chrome):
        total = chrome.find_element_by_css_selector('#app > div > div > div.YD4Yw > div._1-iDe._14VS3 > span > div > span > div > div > div._1TM40 > div:nth-child(5) > div._1Gecv > div > div > div._3HPyS._1e77x')
        return int(total.text.rstrip(" participants"))

    # finds all the participants name
    def find_names(self,chrome):
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

    # send a message to group chat, chat must be open already
    def send_msg(self,message,chrome):
        type_field = chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        type_field.send_keys(message)

        send_button = chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
        send_button.click()

    def read_msgs(self,chrome):
        msgs_in = chrome.find_elements(By.CLASS_NAME,"message-in")
        for msg in msgs_in:
            msg_span = msg.find_element(By.CLASS_NAME,"eRacY")
            print(msg_span.text)

    # read latest message of the current chat
    def read_latest_msg(self,chrome):
            msg_in = chrome.find_elements(By.CLASS_NAME,"message-in")[-1]
            msg_span = msg_in.find_element(By.CLASS_NAME,"eRacY")
            msg_hash = hash(msg_span.text)
            if msg_span.text[:3]=="@JD":
                print("bot called")
            if msg_span.text=="@all" and self.prev_msg!=msg_hash:
                print("detected")
                self.at_all(chrome)
            self.prev_msg = msg_hash
            return msg_hash

    # @ everyone in the group chat
    def at_all(self,chrome):
        type_field = chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        actions = ActionChains(chrome) 
        for i in range(self.size-1):
            actions.send_keys("@")
            actions.send_keys(Keys.ARROW_DOWN*i)
            actions.send_keys(Keys.TAB)
        actions.perform()
        type_field.send_keys(Keys.ENTER)