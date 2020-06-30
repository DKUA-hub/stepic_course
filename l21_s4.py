from selenium import webdriver
import math
import time

def calc(x):
    y = str(math.log(abs(12*math.sin(int(x)))))
    print("y=", y)
    return y

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_css_selector("[value='robots']")
    option2.click()

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    print("x=", x)
    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    time.sleep(2)
    button.click()

finally:
    time.sleep(10)
    browser.quit()
