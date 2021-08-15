import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

web_driver = None


@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    global web_driver
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = web_driver
    web_driver.implicitly_wait(5)
    yield
    web_driver.close()


@pytest.mark.usefixtures("init_driver")
class PyFix:
    pass
