import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

web_driver = None


@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    global web_driver
    if request.param == "chrome":
        web_driver_options = Options()
        web_driver_options.add_argument('--headless')
        web_driver_options.add_argument('--disable-gpu')
        web_driver = webdriver.Chrome(ChromeDriverManager().install(), options=web_driver_options)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(5)
    yield
    web_driver.close()


@pytest.mark.usefixtures("init_driver")
class PyFix:
    pass
