import requests
from selenium.webdriver.common.by import By
import random
import time

def get_quote():
    response = requests.get("https://labs.bible.org/api/?passage=random")
    phrase = response.text.replace('<b>', '').replace('</b>', ' -').replace("“", "")
    return phrase


def enter_user_name(driver, user):
    for i in range(4):
        try:
            active_field = driver.find_element(By.NAME, "text")
            active_field.click()
            active_field.send_keys(user)
            time.sleep(random.randint(0, 5))
            active_field = driver.find_element(By.XPATH,
                                               '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
            active_field.click()
            return True
        except:
            time.sleep(random.randint(0, 5))
            continue
    return False

def enter_user_pass(driver, password):
    for i in range(4):
        try:
            active_field = driver.find_element(By.NAME, "password")
            active_field.click()
            active_field.send_keys(password)
            time.sleep(random.randint(0, 5))

            active_field = driver.find_element(By.XPATH,
                                               '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
            active_field.click()
            return True
        except:
            time.sleep(random.randint(0, 5))
            continue
    return False


