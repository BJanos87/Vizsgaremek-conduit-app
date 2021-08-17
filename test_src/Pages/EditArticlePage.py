from test_src.Pages.base_commands import BaseCommands
from test_src.Data.test_data import EditArticlePgWebElements
from test_src.Data.test_data import TestData


class EditArticlePage(BaseCommands):

    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    """Page Actions for Edit Article Page"""

    """this used to check inputs displayed"""
    def is_inputs_displayed(self):
        return self.is_elements_displayed(EditArticlePgWebElements.input_fields)

    """this used to check textarea displayed"""
    def is_textarea_displayed(self):
        return self.is_element_displayed(EditArticlePgWebElements.input_textarea)

    """this used to check inputs attribute"""
    def is_inputs_placeholder(self):
        return self.check_elements_attribute(EditArticlePgWebElements.input_fields, "placeholder", TestData.inputs_placeholder_value_article)

    """this used to check textarea attribute"""
    def is_textarea_placeholder(self):
        return self.check_element_attribute(EditArticlePgWebElements.input_textarea, "placeholder", TestData.inputs_placeholder_value_textarea_article)

    """this used to check the Home button is displayed"""
    def is_home_btn_displayed(self):
        return self.is_element_displayed(EditArticlePgWebElements.home_btn)

    """this used to click on Home button"""
    def click_home_btn(self):
        self.do_click(EditArticlePgWebElements.home_btn )

    """this used to check the Publish Article button is displayed"""
    def is_publish_article_btn_displayed(self):
        return self.is_element_displayed(EditArticlePgWebElements.publish_article_btn)

    """this used to click on Publish Article button"""
    def click_publish_article_btn(self):
        self.do_click(EditArticlePgWebElements.publish_article_btn)

    """this used to fill Article form inputs with test data"""
    def fill_article_form_inputs(self):
        self.do_send_key_elements(EditArticlePgWebElements.input_fields, TestData.inputs_article_form)

    """this used to fill Article form textarea with test data"""
    def fill_article_form_textarea(self):
        self.do_send_key(EditArticlePgWebElements.input_textarea, TestData.input_article_form_textarea)

    """this used to fill Article form inputs with test data from a txt file"""
    def fill_article_form_inputs_from_file(self):
        self.fill_inputs_from_txt(TestData.article_form_inputs_test_file, EditArticlePgWebElements.input_fields)

    """this used to fill Article textarea input with test data from a txt file"""
    def fill_article_form_textarea_from_file(self):
        self.fill_input_from_txt(TestData.article_form_textarea_test_file, EditArticlePgWebElements.input_textarea)

    """this used to clear Article inputs"""
    def clear_article_input_elements(self):
        self.clear_input_elements(EditArticlePgWebElements.input_fields)

    """this used to clear Article textarea input"""
    def clear_article_input_element(self):
        self.clear_input_element(EditArticlePgWebElements.input_textarea)
