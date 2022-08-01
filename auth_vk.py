from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from auth_data import login, password # create file auth_data.py with login='email/phonenumber' password='password'
import time

url = 'https://vk.com/'
driver = webdriver.Chrome(executable_path=r'E:\SeleniumPython\chromedriver.exe')

try:
    driver.get(url=url)
    time.sleep(7)

    email_input = driver.find_element(By.ID, 'index_email')
    email_input.clear()
    email_input.send_keys(login + Keys.ENTER)
    time.sleep(7)

    password_input = driver.find_element(By.NAME, 'password')
    password_input.clear()
    password_input.send_keys(password + Keys.ENTER)
    time.sleep(10)

    #msg_link = driver.find_element(By.ID, "message_outline_20__message_outline_20").click()

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()