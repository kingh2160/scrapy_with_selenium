from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

filepath = 'private_case.txt'
head = 'https://www.youtube.com/c/'

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

df = pd.DataFrame(columns = ['VIEWS'])

with open(filepath, 'r') as file:
    channels = file.readlines()

for channel in channels:
    target = head + channel
    driver.get(url=target)
    driver.implicitly_wait(10)
    view = driver.find_element(By.XPATH, '//*[@id="right-column"]/yt-formatted-string[3]')
    df = df.append({ 'VIEWS':view.text }, ignore_index=True)
df.to_csv('private_youtube.csv', encoding='utf-8')
driver.close()