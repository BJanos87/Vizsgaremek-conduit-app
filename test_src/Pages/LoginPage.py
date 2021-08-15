from test_src.Pages.base_commands import BaseCommands
from test_src.Data.test_data import LoginPgWebElements
from test_src.Data.test_data import TestData


class LoginPage(BaseCommands):
    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    """Page Actions for Login Page"""

    """this used to check inputs displayed"""
    def is_inputs_displayed(self):
        return self.is_elements_displayed(LoginPgWebElements.input_fields)

    """this used to check inputs attribute"""
    def is_inputs_placeholder(self):
        return self.check_elements_attribute(LoginPgWebElements.input_fields, "placeholder", TestData.inputs_placeholder_value_login)

    """this used to check Password type"""
    def is_password_type(self):
        return self.check_element_attribute(LoginPgWebElements.input_password, "type", TestData.password_type_value)

    """this used to fill Login inputs with existed data"""
    def fill_login_existed_email(self):
        self.do_send_key_elements(LoginPgWebElements.input_fields, TestData.login_test_existed_email)

    """this used to fill Login inputs with not existed data"""
    def fill_login_not_existed_email(self):
        self.do_send_key_elements(LoginPgWebElements.input_fields, TestData.login_test_not_existed_email)

    """this used to check Login Failed msg is displayed"""
    def is_login_failed_msg_displayed(self):
        return self.is_element_displayed(LoginPgWebElements.login_failed_msg)

    """this used to check Login Failed msg text"""
    def login_failed_msg_text(self):
        return self.get_element_text(LoginPgWebElements.login_failed_msg)

    """this used to check Login Failed accept button is displayed"""
    def is_login_failed_accept_btn_displayed(self):
        return self.is_element_displayed(LoginPgWebElements.login_failed_accept_btn)

    """this used to click on Login Failed accept button"""
    def click_login_failed_accept_btn(self):
        self.do_click(LoginPgWebElements.login_failed_accept_btn)

    """this used to check sign in button is displayed"""
    def is_sign_in_btn_displayed(self):
        return self.is_element_displayed(LoginPgWebElements.sign_in_btn)

    """this used to click on the Sign In button"""
    def click_sign_in_btn(self):
        return self.do_click(LoginPgWebElements.sign_in_btn)

    """this used to check Home button is displayed"""
    def is_home_btn_displayed(self):
        return self.is_element_displayed(LoginPgWebElements.home_btn)

    """this used to click on the Home button"""
    def click_home_btn(self):
        return self.do_click(LoginPgWebElements.home_btn)
