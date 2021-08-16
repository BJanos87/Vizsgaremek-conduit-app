from test_src.Tests.test01_registration.conftest import PyFix
from test_src.Pages.HomePage import HomePage
from test_src.Pages.RegPage import RegPage
from test_src.Data.test_data import TestData
import time


class TestReg02(PyFix):

    """this used to check the title of the loaded url, and check the Sign Up button"""
    def test_homepage(self):
        try:
            self.HomePage = HomePage(self.driver)
            assert self.HomePage.get_home_page_url() == TestData.BASE_URL
            assert self.HomePage.get_home_page_title() == TestData.HOME_PAGE_TITLE
            assert self.HomePage.is_sign_up_btn_displayed() is True
            self.HomePage.click_sign_up_btn()
            time.sleep(1)
        except AssertionError as err:
            self.pytest.fail(print(TestData.assert_error_msg, err))

    """this used to check the elements of the Registration Page"""
    """register a new user"""
    def test_check_signup_form(self):
        try:
            self.RegPage = RegPage(self.driver)
            assert self.RegPage.is_inputs_displayed() is True
            assert self.RegPage.is_inputs_placeholder() is True
            assert self.RegPage.is_password_type() is True
            assert self.RegPage.is_sign_up_btn_displayed() is True
        except AssertionError as err:
            self.pytest.fail(print(TestData.assert_error_msg, err))

    """this used to check to fill registration form with invalid email"""
    def test_fill_signup_form_invalid_email(self):
        try:
            self.RegPage = RegPage(self.driver)
            self.RegPage.fill_reg_invalid_email()
            self.RegPage.click_sign_up_btn()
            time.sleep(1)
            assert self.RegPage.is_reg_failed_msg_displayed() is True
            assert self.RegPage.reg_failed_msg_text() == TestData.text_reg_failed_msgs[0]
            assert self.RegPage.is_reg_failed_accept_btn_displayed() is True
            self.RegPage.click_reg_failed_accept_btn()
        except AssertionError as err:
            self.pytest.fail(print(TestData.assert_error_msg, err))

    """this used to check to fill registration form with invalid password"""
    def test_fill_signup_form_invalid_password(self):
        try:
            self.RegPage = RegPage(self.driver)
            self.RegPage.fill_reg_invalid_password()
            self.RegPage.click_sign_up_btn()
            time.sleep(1)
            assert self.RegPage.is_reg_failed_msg_displayed() is True
            assert self.RegPage.reg_failed_msg_text() == TestData.text_reg_failed_msgs[1]
            assert self.RegPage.is_reg_failed_accept_btn_displayed() is True
            self.RegPage.click_reg_failed_accept_btn()
        except AssertionError as err:
            self.pytest.fail(print(TestData.assert_error_msg, err))

    """this used to check to fill registration form with invalid username"""
    def test_fill_signup_form_invalid_username(self):
        try:
            self.RegPage = RegPage(self.driver)
            self.RegPage.fill_reg_invalid_username()
            self.RegPage.click_sign_up_btn()
            time.sleep(1)
            assert self.RegPage.is_reg_failed_msg_displayed() is True
            assert self.RegPage.reg_failed_msg_text() == TestData.text_reg_failed_msgs[2]
            assert self.RegPage.is_reg_failed_accept_btn_displayed() is True
            self.RegPage.click_reg_failed_accept_btn()
        except AssertionError as err:
            self.pytest.fail(print(TestData.assert_error_msg, err))

    """this used to check to fill registration form with an existing email"""
    def test_fill_signup_form_existing_email(self):
        try:
            self.RegPage = RegPage(self.driver)
            self.RegPage.fill_reg_valid()
            self.RegPage.click_sign_up_btn()
            time.sleep(1)
            assert self.RegPage.is_reg_failed_msg_displayed() is True
            assert self.RegPage.reg_failed_msg_text() == TestData.text_reg_failed_msgs[3]
            assert self.RegPage.is_reg_failed_accept_btn_displayed() is True
            self.RegPage.click_reg_failed_accept_btn()
        except AssertionError as err:
            self.pytest.fail(print(TestData.assert_error_msg, err))

    """this used to check user is logged out"""
    def test_navigate_home(self):
        try:
            self.RegPage = RegPage(self.driver)
            assert self.RegPage.is_home_btn_displayed() is True
            self.RegPage.click_home_btn()
        except AssertionError as err:
            self.pytest.fail(print(TestData.assert_error_msg, err))

    def test_homepage_is_displayed(self):
        try:
            self.HomePage = HomePage(self.driver)
            assert self.HomePage.get_home_page_url() == TestData.BASE_URL
            assert self.HomePage.get_home_page_title() == TestData.HOME_PAGE_TITLE
            assert self.HomePage.is_sign_in_btn_displayed() is True
        except AssertionError as err:
            self.pytest.fail(print(TestData.assert_error_msg, err))
