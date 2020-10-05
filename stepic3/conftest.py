from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

def pytest_addoption(parser):
    parser.addoption('--language', action = 'store', default='es',
                     help = 'Choose language: es, ru')

@pytest.fixture(scope='function')
def browser(request):
    print("\nStarting fixture")
    lang = request.config.getoption('language')
    print(f"\nUser's language is {lang}")
    if lang == 'es' or lang == 'ru':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': lang})
        browser = webdriver.Chrome(options=options)
    else:
        print("\nERROR: -language must be es or ru")
    yield browser
    print("\nBye..")
    browser.quit()
