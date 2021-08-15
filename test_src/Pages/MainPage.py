from test_src.Pages.base_commands import BaseCommands
from test_src.Data.test_data import MainPgWebElements


class MainPage(BaseCommands):

    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    """Page Actions for Main Page"""

    """this used to check Registration Successful msg is displayed"""
    def is_reg_successful_displayed(self):
        return self.is_element_displayed(MainPgWebElements.reg_successful_msg)

    """this used to check text of the Registration Successful msg"""
    def reg_successful_text(self):
        return self.get_element_text(MainPgWebElements.reg_successful_msg)

    """this used to check Registration Successful accept button is displayed"""
    def is_reg_successful_accept_btn_displayed(self):
        return self.is_element_displayed(MainPgWebElements.reg_successful_accept_btn)

    """this used to click on Registration Successful accept button"""
    def click_reg_successful_accept_btn(self):
        self.do_click(MainPgWebElements.reg_successful_accept_btn)

    """this used to check the correct Username"""
    def is_username_displayed(self):
        return self.get_element_text(MainPgWebElements.username_btn)

    """this used to click on user button"""
    def click_user_btn(self):
        self.do_click(MainPgWebElements.username_btn)

    """this used to check the log out button is displayed"""
    def is_log_out_btn_displayed(self):
        return self.is_element_displayed(MainPgWebElements.log_out_btn)

    """this used to click on log out button"""
    def click_log_out_btn(self):
        self.do_click(MainPgWebElements.log_out_btn)

    """this used to check the New Article button is displayed"""
    def is_new_article_btn_displayed(self):
        return self.is_element_displayed(MainPgWebElements.new_article_btn)

    """this used to click on New Article button"""
    def click_new_article_btn(self):
        self.do_click(MainPgWebElements.new_article_btn)

    """this used to check the Conduit Title is displayed"""
    def is_conduit_title_displayed(self):
        return self.get_element_text(MainPgWebElements.conduit_title)

    """this used to scroll to the bottom of the page"""
    def scroll_to_end_of_the_page(self):
        self.scroll_to_bottom_of_the_page(MainPgWebElements.main_page)

    """this used to check the next button on the topic list is displayed"""
    def is_next_btn_displayed(self):
        return self.is_element_displayed(MainPgWebElements.list_scroll_next_btn)

    """this used to check the next button on the topic list is enabled"""
    def is_next_btn_selected(self):
        return self.is_element_selected(MainPgWebElements.list_scroll_next_btn)

    """this used to click on next button on the topic list"""
    def click_next_btn_topic_list(self):
        self.do_click(MainPgWebElements.list_scroll_next_btn)

    """this used count web elements (posts) on the list"""
    def count_post_fields(self):
        return self.count_web_elements(MainPgWebElements.post_fields)

    """this used to save the texts of the Article Title web elements to a txt file"""
    def save_article_title_list_into_text_file(self):
        self.save_list_into_text_file(MainPgWebElements.post_fields)

    """this used to compare web elements with text file"""
    def check_saved_article_title_list_from_text_file(self):
        self.check_saved_list_from_text_file(MainPgWebElements.post_fields)
