from test_src.Tests.test01_registration.conftest import PyFix
from test_src.Pages.HomePage import HomePage
from test_src.Pages.RegPage import RegPage
from test_src.Pages.MainPage import MainPage
from test_src.Data.test_data import TestData
import time


class TestReg01(PyFix):

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
            self.pytest.fail(TestData.assert_error_msg, err)

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
            self.pytest.fail(TestData.assert_error_msg, err)

    def test_fill_signup_form_valid(self):
        try:
            self.RegPage = RegPage(self.driver)
            self.RegPage.fill_reg_valid()
            self.RegPage.click_sign_up_btn()
            time.sleep(2)
        except AssertionError as err:
            self.pytest.fail(TestData.assert_error_msg, err)

    """this used to check the new user sign is successful"""
    def test_sign_in_new_user(self):
        try:
            self.MainPage = MainPage(self.driver)
            assert self.MainPage.is_reg_successful_displayed() is True
            assert self.MainPage.reg_successful_text() == TestData.text_reg_successful
            assert self.MainPage.is_reg_successful_accept_btn_displayed() is True
            self.MainPage.click_reg_successful_accept_btn()
            time.sleep(1)
            assert self.MainPage.is_username_displayed() == TestData.reg_test_valid[0]
            assert self.MainPage.is_log_out_btn_displayed() is True
            self.MainPage.click_log_out_btn()
            time.sleep(1)
        except AssertionError as err:
            self.pytest.fail(TestData.assert_error_msg, err)

    """this used to check log out was successful"""
    def test_logout_successful(self):
        try:
            self.HomePage = HomePage(self.driver)
            assert self.HomePage.get_home_page_url() == TestData.BASE_URL
            assert self.HomePage.get_home_page_title() == TestData.HOME_PAGE_TITLE
            assert self.HomePage.is_sign_in_btn_displayed() is True
        except AssertionError as err:
            self.pytest.fail(TestData.assert_error_msg, err)
