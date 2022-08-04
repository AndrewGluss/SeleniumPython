from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    picture = browser.find_element(By.ID, "treasure")
    picture_value = picture.get_attribute("valuex")
    x = picture_value
    y = calc(x)

    y_input = browser.find_element(By.ID, "answer")
    y_input.send_keys(y)

    checkbox_input = browser.find_element(By.ID, "robotCheckbox")
    checkbox_input.click()

    radio_input = browser.find_element(By.ID, "robotsRule")
    radio_input.click()

    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()
finally:
    time.sleep(30)

    browser.quit()
