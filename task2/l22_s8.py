from selenium import webdriver
import os
import time

lnk = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(lnk)

    input1 = browser.find_element_by_css_selector("input[name='firstname']")
    input1.send_keys("Firstname")
    browser.find_element_by_css_selector("input[name='lastname']").send_keys("Lastname")
    browser.find_element_by_css_selector("input[name='email']").send_keys("email@mail.com")

    dirpath = os.path.abspath(os.path.dirname(__file__))
    filename = os.path.join(dirpath, "file.txt")
    print("filename = %s" % filename)

    browser.find_element_by_css_selector("input[type='file']").send_keys(filename)
    browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(10)
    browser.quit()
