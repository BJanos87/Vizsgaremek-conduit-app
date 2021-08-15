from test_src.Tests.test04_new_article.conftest import PyFix
from test_src.Pages.HomePage import HomePage
from test_src.Pages.LoginPage import LoginPage
from test_src.Pages.MainPage import MainPage
from test_src.Data.test_data import TestData
import time


class TestSaveData(PyFix):

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
            self.pytest.fail(TestData.assert_error_msg, err)

    """this used to check the elements of the Login Page"""
    """Login an existing user"""
    def test_check_login_form(self):
        try:
            self.LoginPage = LoginPage(self.driver)
            assert self.LoginPage.is_inputs_displayed() is True
            assert self.LoginPage.is_inputs_placeholder() is True
            assert self.LoginPage.is_password_type() is True
        except AssertionError as err:
            self.pytest.fail(TestData.assert_error_msg, err)

    """this used to fill Login Page and sign in to app"""
    def test_login_exist_user(self):
        try:
            self.LoginPage = LoginPage(self.driver)
            self.LoginPage.fill_login_existed_email()
            assert self.LoginPage.is_sign_in_btn_displayed() is True
            self.LoginPage.click_sign_in_btn()
            time.sleep(3)
        except AssertionError as err:
            self.pytest.fail(TestData.assert_error_msg, err)

    """this used to compare web elements with text file"""
    def test_check_write_list_into_text_file(self):
        try:
            self.MainPage = MainPage(self.driver)
            assert self.MainPage.is_username_displayed() == TestData.reg_test_valid[0]
            self.MainPage.save_article_title_list_into_text_file()
            self.MainPage.check_saved_article_title_list_from_text_file()
            assert self.MainPage.is_log_out_btn_displayed() is True
            self.MainPage.click_log_out_btn()
            time.sleep(1)
        except AssertionError as err:
            self.pytest.fail(TestData.assert_error_msg, err)

    """this used to check successful navigate to home page"""
    def test_homepage_is_displayed(self):
        try:
            self.HomePage = HomePage(self.driver)
            assert self.HomePage.get_home_page_url() == TestData.BASE_URL
            assert self.HomePage.get_home_page_title() == TestData.HOME_PAGE_TITLE
            assert self.HomePage.is_sign_in_btn_displayed() is True
        except AssertionError as err:
            self.pytest.fail(TestData.assert_error_msg, err)
