from test_src.Tests.test02_login.conftest import PyFix
from test_src.Pages.HomePage import HomePage
from test_src.Pages.LoginPage import LoginPage
from test_src.Data.test_data import TestData
import time


class TestLogin02(PyFix):

    """this used check the title of the loaded url, and check the Sign In button"""
    def test_homepage(self):
        try:
            self.HomePage = HomePage(self.driver)
            assert self.HomePage.get_home_page_url() == TestData.BASE_URL
            assert self.HomePage.get_home_page_title() == TestData.HOME_PAGE_TITLE
            assert self.HomePage.is_sign_in_btn_displayed() is True
            self.HomePage.click_sign_in_btn()
            time.sleep(1)
        except AssertionError as err:
            self.pytest.fail(print(TestData.assert_error_msg, err))

    """this used to check the elements of the Login Page"""
    def test_check_login_form(self):
        try:
            self.LoginPage = LoginPage(self.driver)
            assert self.LoginPage.is_inputs_displayed() is True
            assert self.LoginPage.is_inputs_placeholder() is True
            assert self.LoginPage.is_password_type() is True
        except AssertionError as err:
            self.pytest.fail(print(TestData.assert_error_msg, err))

    """this used to fill Login Page and sign in to app with not existed user"""
    def test_login_not_exist_user(self):
        try:
            self.LoginPage = LoginPage(self.driver)
            self.LoginPage.fill_login_not_existed_email()
            assert self.LoginPage.is_sign_in_btn_displayed() is True
            self.LoginPage.click_sign_in_btn()
            time.sleep(1)
            assert self.LoginPage.is_login_failed_msg_displayed() is True
            assert self.LoginPage.login_failed_msg_text() == TestData.text_login_failed
            assert self.LoginPage.is_login_failed_accept_btn_displayed() is True
            self.LoginPage.click_login_failed_accept_btn()
            assert self.LoginPage.is_home_btn_displayed() is True
            self.LoginPage.click_home_btn()
        except AssertionError as err:
            self.pytest.fail(print(TestData.assert_error_msg, err))

    """this used to check successful navigate to home page"""
    def test_homepage_is_displayed(self):
        try:
            self.HomePage = HomePage(self.driver)
            assert self.HomePage.get_home_page_url() == TestData.BASE_URL
            assert self.HomePage.get_home_page_title() == TestData.HOME_PAGE_TITLE
            assert self.HomePage.is_sign_in_btn_displayed() is True
        except AssertionError as err:
            self.pytest.fail(print(TestData.assert_error_msg, err))
