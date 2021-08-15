from test_src.Pages.base_commands import BaseCommands
from test_src.Data.test_data import RegPgWebElements
from test_src.Data.test_data import TestData


class RegPage(BaseCommands):

    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    """Page Actions for Registration Page"""

    """this used to check inputs displayed"""
    def is_inputs_displayed(self):
        return self.is_elements_displayed(RegPgWebElements.input_fields)

    """this used to check inputs attribute"""
    def is_inputs_placeholder(self):
        return self.check_elements_attribute(RegPgWebElements.input_fields, "placeholder", TestData.inputs_placeholder_value_reg)

    """this used to check Password type"""
    def is_password_type(self):
        return self.check_element_attribute(RegPgWebElements.input_password, "type", TestData.password_type_value)

    """this used to check Sign Up button is displayed"""
    def is_sign_up_btn_displayed(self):
        return self.is_element_displayed(RegPgWebElements.sign_up_btn)

    """this used to click on Sign Up button"""
    def click_sign_up_btn(self):
        self.do_click(RegPgWebElements.sign_up_btn)

    """this used to check Registration Failed msg is displayed"""
    def is_reg_failed_msg_displayed(self):
        return self.is_element_displayed(RegPgWebElements.reg_failed_msg)

    """this used to check Registration Failed msg text"""
    def reg_failed_msg_text(self):
        return self.get_element_text(RegPgWebElements.reg_failed_msg)

    """this used to check Registration Failed accept button is displayed"""
    def is_reg_failed_accept_btn_displayed(self):
        return self.is_element_displayed(RegPgWebElements.reg_failed_accept_btn)

    """this used to click on Registration Failed accept button"""
    def click_reg_failed_accept_btn(self):
        self.do_click(RegPgWebElements.reg_failed_accept_btn)

    """this used to check home button is displayed"""
    def is_home_btn_displayed(self):
        return self.is_element_displayed(RegPgWebElements.home_btn)

    """this used to click on the home button"""
    def click_home_btn(self):
        self.do_click(RegPgWebElements.home_btn)

    """this used to fill Reg page with valid data"""
    def fill_reg_valid(self):
        self.do_send_key_elements(RegPgWebElements.input_fields, TestData.reg_test_valid)

    """this used to fill Reg page with invalid email"""
    def fill_reg_invalid_email(self):
        self.do_send_key_elements(RegPgWebElements.input_fields, TestData.reg_test_invalid_email)

    """this used to fill Reg page with invalid password"""
    def fill_reg_invalid_password(self):
        self.do_send_key_elements(RegPgWebElements.input_fields, TestData.reg_test_invalid_password)

    """this used to fill Reg page with invalid username"""
    def fill_reg_invalid_username(self):
        self.do_send_key_elements(RegPgWebElements.input_fields, TestData.reg_test_invalid_username)
