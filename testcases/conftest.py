import pytest
from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver

@pytest.fixture()
def setupcon(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#@pytest.hookimpl(tryfirst=True)
#def pytest_runtest_makereport(item,call):
    #if call.when == 'call' and call.excinfo is not None:
        #driver = item.funcargs.get('setupcon')
        #driver.save_screenshot("screenshots/firstfail.png")
