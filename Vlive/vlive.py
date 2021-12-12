from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

filepath = 'vliveurl.txt'
head = 'https://www.vlive.tv/channel/'

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

df = pd.DataFrame(columns = ['SUBSCRIBERS', 'VIEWS', 'LIKES', 'UPLOADS'])

with open(filepath, 'r') as file:
    channels = file.readlines()

for channel in channels:
    target = head + channel
    driver.get(url=target)
    driver.implicitly_wait(10)
    sub = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/nav/div/span/span')
    view = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[4]/div/div/dl/div[3]/dd')
    like = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[4]/div/div/dl/div[4]/dd')
    upload = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[4]/div/div/dl/div[1]/dd')
    df = df.append({ 'SUBSCRIBERS':sub.text, 'VIEWS':view.text, 'LIKES':like.text, 'UPLOADS':upload.text }, ignore_index=True)
df.to_csv('vlive.csv', encoding='utf-8')
driver.close()