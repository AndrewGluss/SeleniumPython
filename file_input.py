from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name_input = browser.find_element(By.NAME, 'firstname')
    name_input.send_keys('Andrew')

    surname_input = browser.find_element(By.NAME, 'lastname')
    surname_input.send_keys('Glukhov')

    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys('glukhov2008@yandex.ru')

    attach_el = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = 'first_attempt.txt'
    file_path = os.path.join(current_dir, file_name)
    attach_el.send_keys(file_path)

    button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    button.click()
finally:
    time.sleep(10)
    
    browser.quit()
