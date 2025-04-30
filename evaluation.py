from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
import time
import random

username = input("username: ")
password = input("password: ")

def resource_path(relative_path):
    return os.path.join(getattr(sys, '_MEIPASS', os.path.abspath(".")), relative_path)

driver_path = resource_path("chromedriver.exe")

driver = webdriver.Chrome(
    service=Service(driver_path),
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
        
    buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, f"//input[contains(@value, '_e_teacher')]")))
    buttons += wait.until(EC.presence_of_all_elements_located((By.XPATH, f"//input[contains(@value, '_e_teacher')]")))

    for button in buttons:
        wait.until(EC.element_to_be_clickable(button))
        button.click()

    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))) 
    time.sleep(2)
    submit_button.click()
    i += 1

driver.quit()
