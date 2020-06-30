from selenium import webdriver
import time
import math

lnk = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(lnk)
    x = browser.find_element_by_id("input_value").text
    #What is ln(abs(12*sin(x))), where x = 843?
    y = str(math.log(abs(12*math.sin(int(x)))))

    input = browser.find_element_by_tag_name("input")
    input.send_keys(y)

    ## First way to scroll
    #browser.execute_script("window.scrollBy(0, 100);") # scroll by 100px
    button = browser.find_element_by_css_selector("button.btn")
    ## Second way to scroll (requires element that's why we defined  button)
    #browser.execute_script("return arguments[0].scrollIntoView({block : 'center'});", button)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    button.click()

finally:
    time.sleep(10)
    browser.quit()
