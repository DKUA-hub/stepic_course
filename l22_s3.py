from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

lnk = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(lnk)
    add1 = int(browser.find_element_by_id("num1").text)
    add2 = int(browser.find_element_by_id("num2").text)
    x = add1 + add2
    print("%s + %s = %s" % (add1, add2, x))

    ## The first way
    #browser.find_element_by_tag_name("select").click()

    ## when you know order
    ##browser.find_element_by_css_selector("option:nth-child(5)").click()

    ## when you know value
    #browser.find_element_by_css_selector("[value='%s']" % (x)).click()

    ## The second way
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value("%s" % x)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
