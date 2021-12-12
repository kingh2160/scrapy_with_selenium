from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

filepath = 'tiktokurl.txt'
head = 'https://socialblade.com/tiktok/user/'

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('disable-gpu')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

df = pd.DataFrame(columns = ['SUBSCRIBERS', 'LIKES', 'UPLOADS'])

with open(filepath, 'r') as file:
    channels = file.readlines()

flag = 0
for channel in channels:
    target = head + channel
    flag = flag + 1
    #print(flag)
    driver.get(url=target)
    driver.implicitly_wait(20)
    sub = driver.find_element(By.XPATH, '//*[@id="YouTubeUserTopInfoBlock"]/div[3]/span[2]')
    like = driver.find_element(By.XPATH, '//*[@id="YouTubeUserTopInfoBlock"]/div[5]/span[2]')
    upload = driver.find_element(By.XPATH, '//*[@id="YouTubeUserTopInfoBlock"]/div[2]/span[2]')
    df = df.append({ 'SUBSCRIBERS':sub.text, 'LIKES':like.text, 'UPLOADS':upload.text  }, ignore_index=True)
df.to_csv('twitter.csv', encoding='utf-8')
driver.close()