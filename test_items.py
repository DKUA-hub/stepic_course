import time
#link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_busket_button(browser):

    browser.get(link)
    time.sleep(10)
    assert browser.find_element_by_css_selector("#add_to_basket_form > button"), "No adding to busket button"
