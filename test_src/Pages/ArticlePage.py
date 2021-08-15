from test_src.Pages.base_commands import BaseCommands
from test_src.Data.test_data import ArticlePgWebElements


class ArticlePage(BaseCommands):

    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    """Page Actions for the Article Page"""

    """this used to check Article Title is displayed"""
    def is_article_title_displayed(self):
        return self.get_element_text(ArticlePgWebElements.article_title)

    """this used to check Article is displayed"""
    def is_article_displayed(self):
        return self.get_element_text(ArticlePgWebElements.article)

    """this used to check Edit Article button is displayed"""
    def is_edit_article_btn_displayed(self):
        return self.is_element_displayed(ArticlePgWebElements.edit_article_btn)

    """this used to click in Edit Article button"""
    def click_edit_article_btn(self):
        self.do_click(ArticlePgWebElements.edit_article_btn)

    """this used to check Delete Article button is displayed"""
    def is_delete_article_btn_displayed(self):
        return self.is_element_displayed(ArticlePgWebElements.delete_article_btn)

    """this used to click Delete Article button"""
    def click_delete_article_btn(self):
        self.do_click(ArticlePgWebElements.delete_article_btn)

    """this used to check Log out button is displayed"""
    def is_log_out_btn_is_displayed(self):
        return self.is_element_displayed(ArticlePgWebElements.log_out_btn)

    """this used to click on the Log out button"""
    def click_log_out_btn(self):
        return self.do_click(ArticlePgWebElements.log_out_btn)
