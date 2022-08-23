import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

message = ''

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(message)




@pytest.mark.parametrize("endpoint", ['236895', '236896', '236897', '236898','236899', '236903', '236904', '236905'])
def test_answer(browser, endpoint):
    global message
    link = f"https://stepik.org/lesson/{endpoint}/step/1"
    browser.get(link)
    browser.implicitly_wait(10)
    answer_input = browser.find_element(By.TAG_NAME, "textarea")

    answer_input.send_keys(str(math.log(int(time.time()))))
    send_button = WebDriverWait(browser,5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission'))
    )
    send_button.click()

    feedback = WebDriverWait(browser, 5).until(
         EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    )

    try:
        assert feedback.text == "Correct!"
    except AssertionError:
        message += feedback.text




if __name__ == "__main__":
    pytest.main()