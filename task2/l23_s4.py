from selenium import webdriver
import time
import math

link="http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_tag_name('button').click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = int(browser.find_element_by_id("input_value").text)
    y = str(math.log(abs(12*math.sin(x))))

    input = browser.find_element_by_tag_name("input")
    input.send_keys(y)

    browser.find_element_by_tag_name('button').click()


finally:
    time.sleep(10)
    browser.quit()
