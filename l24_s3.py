from selenium import webdriver
import time

lnk = "http://suninjuly.github.io/wait1.html"

try:
    browser = webdriver.Chrome()
    browser.get(lnk)

    time.sleep(1)
    browser.find_element_by_tag_name("button").click()

    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text
finally:
    browser.quit()
