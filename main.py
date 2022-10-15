from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time
from misc import get_quote, enter_user_name, enter_user_pass
import os
from datetime import datetime

user = os.environ.get("USER")
password = os.environ.get("PASS")

url = 'https://twitter.com/login'
#############
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)
############
chrome_driver_path = 'C:/temp/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
driver.maximize_window()
driver.get(url)
time.sleep(5)

# enter user name
if not enter_user_name(driver, user):
    # print("couldn't supply username")
    exit()

# enter password
time.sleep(random.randint(0, 5))
# enter_user_pass(driver, password)
if not enter_user_pass(driver, password):
    # print("couldn't supply password")
    exit()

# print('logged in...')
time.sleep(random.randint(0, 5))
#loop
for i in range(2):
    # print(f"try {str(i + 1)}")
    try:
        active_field = driver.find_element(By.CSS_SELECTOR, ".public-DraftStyleDefault-block")
        active_field.click()
        # print("selected tweet box")
        active_field.click()
        active_field.send_keys(get_quote())

    except:
        driver.get('https://twitter.com/home')
        # print("failed on partial class name")

    time.sleep(random.randint(0,20))
    try:
        active_field = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div")
        active_field.click()
        # print("clicked")
        active_field.click()
    except:
        driver.get('https://twitter.com/home')
        # print("failed on click")
    time_waiste = random.randint(0, 10000)
    print(f"waiting {str(time_waiste / 60)} minutes")

    now = datetime.now()

    print("Current Time =", now.strftime("%H:%M:%S"))
    time.sleep(time_waiste)

driver.quit()

