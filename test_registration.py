import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistration(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH,
                                      "//input[@placeholder='Input your first name']")  # (By.CSS_SELECTOR, "[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH,
                                      "//input[@placeholder='Input your last name']")  # "(By.CSS_SELECTOR, [placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH,
                                      "//input[@placeholder='Input your email']")  # (By.CSS_SELECTOR, "[placeholder='Input your email']")
        input3.send_keys("Smolensk")
        # На всякий случай заполняю необязательные поля при регистрации
        input4 = browser.find_element(By.XPATH,
                                      "//input[@placeholder='Input your phone:']")  # (By.CSS_SELECTOR, "[placeholder='Input your phone:']")
        input4.send_keys("88005553535")
        input4 = browser.find_element(By.XPATH,
                                      "//input[@placeholder='Input your address:']")  # (By.CSS_SELECTOR, "[placeholder='Input your address:']")
        input4.send_keys("My address Soviet Union")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element(By.XPATH, "//input[@placeholder = 'Input your first name']")
        first_name.send_keys('Petr')
        last_name = browser.find_element(By.XPATH, "//input[@placeholder = 'Input your last name']")
        last_name.send_keys('Vasilev')
        email1 = browser.find_element(By.XPATH, "//input[@placeholder = 'Input your email']")
        email1.send_keys('V@gmail.com')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text


if "__name__" == "__main__":
    unittest.main()