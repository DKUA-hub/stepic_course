from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

def pytest_addoption(parser):
    parser.addoption('--language', action = 'store', default=None,
                     help = 'Choose language..')

@pytest.fixture(scope='function')
def browser(request):
    lang = request.config.getoption('language')
    """
    if lang == 'es' or lang == 'ru':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': lang})
        browser = webdriver.Chrome(options=options)
    else:
        print("\nERROR: -language must be es or ru")
    """
    options = Options()
    print(options)
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
