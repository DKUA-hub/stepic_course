from selenium import webdriver
import time

lnk = "http://suninjuly.github.io/wait1.html"

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(lnk)

browser.find_element_by_tag_name("button").click()

message = browser.find_element_by_id("verify_message")

assert "successful" in message.text
