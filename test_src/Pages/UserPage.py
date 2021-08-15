from test_src.Pages.base_commands import BaseCommands
from test_src.Data.test_data import UserPgWebElements


class UserPage(BaseCommands):

    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    """Page Actions for User Page"""

    """this used to check Test Post is displayed"""
    def is_test_post_displayed(self):
        return self.get_element_text(UserPgWebElements.test_post)

    """this used to click on the Test Post"""
    def click_test_post(self):
        return self.do_click(UserPgWebElements.test_post)

    """this used to check Home Button is displayed"""
    def is_home_btn_displayed(self):
        return self.is_element_displayed(UserPgWebElements.home_btn)

    """this used to click on the Home Button"""
    def click_home_btn(self):
        return self.do_click(UserPgWebElements.home_btn)
