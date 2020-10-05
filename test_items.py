link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_items(browser):

    browser.get(link)
    browser.find_element_by_css_selector("#add_to_basket_form > button")
