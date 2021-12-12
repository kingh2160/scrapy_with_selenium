from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

filepath = 'twitterurl.txt'
head = 'https://socialblade.com/twitter/user/'

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('disable-gpu')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

df = pd.DataFrame(columns = ['SUBSCRIBERS', 'UPLOADS', 'DATE'])

with open(filepath, 'r') as file:
    channels = file.readlines()

flag = 0
for channel in channels:
    target = head + channel
    flag = flag + 1
    #print(flag)
    driver.get(url=target)
    driver.implicitly_wait(10)
    sub = driver.find_element(By.XPATH, '/html/body/div[11]/div[2]/div/div[3]/div[2]/span[2]')
    date = driver.find_element(By.XPATH, '//*[@id="YouTubeUserTopInfoBlock"]/div[6]/span[2]')
    upload = driver.find_element(By.XPATH, '//*[@id="YouTubeUserTopInfoBlock"]/div[5]/span[2]')
    df = df.append({ 'SUBSCRIBERS':sub.text, 'UPLOADS':upload.text, 'DATE':date.text }, ignore_index=True)
df.to_csv('twitter.csv', encoding='utf-8')
driver.close()