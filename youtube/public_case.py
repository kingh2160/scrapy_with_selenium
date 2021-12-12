from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

filepath = 'public_case.txt'
head = 'https://socialblade.com/youtube/'

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

df = pd.DataFrame(columns = ['SUBSCRIBERS', 'VIEWS', 'DATE', 'UPLOADS'])

with open(filepath, 'r') as file:
    channels = file.readlines()

for channel in channels:
    target = head + channel
    driver.get(url=target)
    driver.implicitly_wait(10)
    sub = driver.find_element(By.XPATH, '//*[@id="YouTubeUserTopInfoBlock"]/div[3]/span[2]')
    view = driver.find_element(By.XPATH, '//*[@id="YouTubeUserTopInfoBlock"]/div[4]/span[2]')
    date = driver.find_element(By.XPATH, '//*[@id="YouTubeUserTopInfoBlock"]/div[7]/span[2]')
    upload = driver.find_element(By.XPATH, '//*[@id="YouTubeUserTopInfoBlock"]/div[2]/span[2]')
    df = df.append({ 'SUBSCRIBERS':sub.text, 'VIEWS':view.text, 'DATE':date.text, 'UPLOADS':upload.text }, ignore_index=True)
df.to_csv('public_youtube.csv', encoding='utf-8')
driver.close()