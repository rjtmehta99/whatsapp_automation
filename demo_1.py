from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pandas as pd
import time

def send_message(recipient, message):
    try:
        time.sleep(5)
        
        search_bar = browser.find_element_by_xpath('//div[@contenteditable = "true"]')
            
        search_bar.send_keys(recipient)
        
        search_bar.send_keys(Keys.ENTER)
        
        time.sleep(3)
        
        msg_bar = browser.find_elements_by_xpath('//div[@contenteditable = "true"]')[1]
        
        msg_bar.send_keys(message)
        
        msg_bar.send_keys(Keys.ENTER)
        
        time.sleep(5)
        
        return 'Sent Successfully'
    
    except Exception as e:
        print('Error encountered: ', e)
        
        return 'Error Encountered'

df = pd.read_csv('data.csv')

browser = webdriver.Firefox()

URL = 'https://web.whatsapp.com/'

browser.get(URL)

time.sleep(10)

df['status'] = df.apply(lambda row: send_message(row['recipient'], row['message']), axis = 1)

browser.quit()

df.to_csv('data.csv', index = False)