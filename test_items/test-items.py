import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_button_is_exist(browser):
    browser.get(link)
    
    time.sleep(30)
    
    # методом is_displayed() проверяем наличие кнопки
    buttons = browser.find_elements(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    assert len(buttons) > 0, "Кнопка не найдена"
