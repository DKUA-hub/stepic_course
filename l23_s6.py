from selenium import webdriver
import time
import math

link="http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_tag_name('button').click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = int(browser.find_element_by_id("input_value").text)
    y = str(math.log(abs(12*math.sin(x))))

    input = browser.find_element_by_tag_name("input")
    input.send_keys(y)

    browser.find_element_by_tag_name('button').click()


finally:
    time.sleep(10)
    browser.quit()
