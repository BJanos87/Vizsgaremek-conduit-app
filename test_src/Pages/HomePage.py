from test_src.Pages.base_commands import BaseCommands
from test_src.Data.test_data import HomePgWebElements
from test_src.Data.test_data import TestData


class HomePage(BaseCommands):

    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.get_url(TestData.BASE_URL)

    """Page Actions for Home Page"""

    """this used to reload Home Page"""
    def reload_home_page(self):
        self.driver.get(TestData.BASE_URL)

    """this used to get the current page url"""
    def get_home_page_url(self):
        return self.get_current_url()

    """this used to get the current page title"""
    def get_home_page_title(self):
        return self.get_current_title()

    """this used to get list of the cookies from Home Page"""
    def get_cookie_status_from_homepage(self):
        return len(self.get_cookies_list())

    """this used to check value of the cookie"""
    def check_value_cookie_from_homepage(self):
        cookie = self.check_value_cookie()
        return cookie["value"]

    """this used to click on cookie accept button on Home Page"""
    def click_cookie_accept_btn(self):
        self.do_click(HomePgWebElements.cookie_accept_btn)

    """this used to check sign up button is displayed"""
    def is_sign_up_btn_displayed(self):
        return self.is_element_displayed(HomePgWebElements.sign_up_btn)

    """this used to sign up to app"""
    def click_sign_up_btn(self):
        self.do_click(HomePgWebElements.sign_up_btn)

    """this used to check sign in button is displayed"""
    def is_sign_in_btn_displayed(self):
        return self.is_element_displayed(HomePgWebElements.sign_in_btn)

    """this used to sign in to app"""
    def click_sign_in_btn(self):
        return self.do_click(HomePgWebElements.sign_in_btn)
