from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

filepath = 'melonids.txt'
head = 'https://xn--o39an51b2re.com/melon/artiststream/'

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

df = pd.DataFrame(columns = ['LISTENER', 'STREAMING'])

with open(filepath, 'r') as file:
    channels = file.readlines()

for channel in channels:
    target = head + channel
    driver.get(url=target)
    driver.implicitly_wait(10)
    listener = driver.find_element(By.XPATH, '//*[@id="main-wrapper"]/div/div[2]/div[2]/div/div/div/ul/li[3]')
    streaming = driver.find_element(By.XPATH, '//*[@id="main-wrapper"]/div/div[2]/div[2]/div/div/div/ul/li[4]')
    df = df.append({ 'LISTENER':listener.text, 'STREAMING':streaming.text }, ignore_index=True)
df.to_csv('melon.csv', encoding='utf-8')
driver.close()