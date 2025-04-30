from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

username = input("username: ")
password = input("password: ")

driver_path = '/usr/bin/chromedriver'

options = Options()

driver = webdriver.Chrome(
    service=Service(driver_path),
    options=options
)

wait = WebDriverWait(driver, 20)

driver.get('https://qec.su.edu.pk')

username_field = wait.until(EC.presence_of_element_located((By.ID, 'phone')))
password_field = wait.until(EC.presence_of_element_located((By.ID, 'password')))
login_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))

username_field.send_keys(username)
password_field.send_keys(password)
login_button.click()

surveys = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, 'evaluation/create')]")))

i = 0 

while i < 8:
    try:
        surveys = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, 'evaluation/create')]")))
        surveys[i].click()
    except:
        pass

    n = 96
    while n < 117:
        buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, f"//input[contains(@value, {n}) and contains(@value, 'teacher')]")))
        choice = random.randint(0, 4)
        buttons[choice].click()
        n += 1

    n = 117
    while n < 144:
        buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, f"//input[contains(@value, {n}) and contains(@value, 'course')]")))
        choice = random.randint(0, 4)
        buttons[choice].click()
        n += 1

    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))) 
    time.sleep(2)
    submit_button.click()   

driver.quit()
