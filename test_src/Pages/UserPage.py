from test_src.Pages.base_commands import BaseCommands
from test_src.Data.test_data import UserPgWebElements


class UserPage(BaseCommands):

    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    """Page Actions for User Page"""

    """this used to check Article Title is displayed"""
    def is_article_title_displayed(self):
        return self.get_element_text(UserPgWebElements.article_title)

    """this used to click on the Article Title"""
    def click_article_title(self):
        return self.do_click(UserPgWebElements.article_title)

    """this used to check Article text is displayed"""
    def is_article_text_displayed(self):
        return self.get_element_text(UserPgWebElements.article_text)

    """this used to check Home Button is displayed"""
    def is_home_btn_displayed(self):
        return self.is_element_displayed(UserPgWebElements.home_btn)

    """this used to click on the Home Button"""
    def click_home_btn(self):
        return self.do_click(UserPgWebElements.home_btn)
