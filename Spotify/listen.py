
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

filepath = 'spotifyurl.txt'
head = 'https://open.spotify.com/artist/'
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

df = pd.DataFrame(columns = ['LISTENER'])

with open(filepath, 'r') as file:
    channels = file.readlines()

flag = 0
for channel in channels:
    target = head + channel
    flag = flag + 1
    #print(flag)
    driver.get(url=target)
    driver.implicitly_wait(10)
    listener = driver.find_element(By.CLASS_NAME, "Ydwa1P5GkCggtLlSvphs")
    df = df.append({'LISTENER': listener.text}, ignore_index=True)

df.to_csv('spotify.csv', encoding='utf-8')
driver.close()
