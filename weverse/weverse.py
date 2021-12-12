from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

f = open('LOGIN.txt', 'r')
EMAIL = f.readline()
PASSWORD = f.readline()
filepath = 'weverseurl.txt'
head = 'https://www.weverse.io/'

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('disable-gpu')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

df = pd.DataFrame(columns = ['SUBSCRIBERS'])

with open(filepath, 'r') as file:
    channels = file.readlines()

flag = 0
for idx in range(len(channels)):
    target = head + channels[idx]
    flag = flag + 1
    #print(flag)
    driver.get(url=target)
    if( idx == 0 ):
        driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]").click()
        driver.switch_to.window(driver.window_handles[1])
        id_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/form/div[1]/input')
        id_input.send_keys(EMAIL)
        pw_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/form/div[2]/input')
        pw_input.send_keys(PASSWORD)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div/form/div[3]/button').click()
        driver.switch_to.window(driver.window_handles[0])
    driver.implicitly_wait(10)
    sub = driver.find_element(By.XPATH, '//*[@id="root"]/div/section/aside/div/div[1]')
    df = df.append({ 'SUBSCRIBERS':sub.text  }, ignore_index=True)
df.to_csv('weverse.csv', encoding='utf-8')
driver.close()