from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 20).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

    book = WebDriverWait(browser,2).until(
    EC.element_to_be_clickable((By.ID, 'book'))
    )
    book.click()

    x = int(browser.find_element_by_id("input_value").text)
    y = str(math.log(abs(12*math.sin(x))))

    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    browser.find_element_by_id('solve').click()

finally:
    time.sleep(10)
    browser.quit()
