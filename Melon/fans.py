from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

filepath = 'melonids.txt'
head = 'https://www.melon.com/artist/timeline.htm?artistId='

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

df = pd.DataFrame(columns = ['FANS'])

with open(filepath, 'r') as file:
    channels = file.readlines()

for channel in channels:
    target = head + channel
    driver.get(url=target)
    driver.implicitly_wait(10)
    fans = driver.find_element(By.XPATH, '//*[@id="d_like_count"]')
    df = df.append({ 'FANS':fans.text }, ignore_index=True)
df.to_csv('fans.csv', encoding='utf-8')
driver.close()