from selenium import webdriver
import time

try:
    link="http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("div.first_block div.first_class input.first")
    input1.send_keys("First")
    input2 = browser.find_element_by_css_selector("div.first_block div.second_class input")
    input2.send_keys("Last")
    input3 = browser.find_element_by_css_selector("div.first_block div.third_class input")
    input3.send_keys("to@me.com")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()
