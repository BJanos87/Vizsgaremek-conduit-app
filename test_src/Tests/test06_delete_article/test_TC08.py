from test_src.Tests.test06_delete_article.conftest import PyFix
from test_src.Pages.HomePage import HomePage
from test_src.Pages.LoginPage import LoginPage
from test_src.Pages.MainPage import MainPage
from test_src.Pages.UserPage import UserPage
from test_src.Pages.ArticlePage import ArticlePage
from test_src.Data.test_data import TestData
import time


class TestDeleteArticle(PyFix):

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
    """Login an existing user"""
    def test_check_login_form(self):
        try:
            self.LoginPage = LoginPage(self.driver)
            assert self.LoginPage.is_inputs_displayed() is True
            assert self.LoginPage.is_inputs_placeholder() is True
            assert self.LoginPage.is_password_type() is True
        except AssertionError as err:
            self.pytest.fail(print(TestData.assert_error_msg, err))

    """this used to fill Login Page and sign in to app"""
    def test_login_exist_user(self):
        try:
            self.LoginPage = LoginPage(self.driver)
            self.LoginPage.fill_login_existed_email()
            assert self.LoginPage.is_sign_in_btn_displayed() is True
            self.LoginPage.click_sign_in_btn()
            time.sleep(3)
        except AssertionError as err:
            self.pytest.fail(print(TestData.assert_error_msg, err))

    """this used to navigate to User page and count posts on the next page of the list"""
    """before delete an article"""
    def test_count_posts_before_delete_post(self):
        try:
            self.MainPage = MainPage(self.driver)
            self.UserPage = UserPage(self.driver)
            assert self.MainPage.is_username_displayed() == TestData.reg_test_valid[0]
            self.MainPage.scroll_to_bottom_of_the_main_page()
            assert self.MainPage.is_next_btn_displayed() is True
            assert self.MainPage.is_next_btn_selected() is False
            self.MainPage.click_next_btn_topic_list()
            time.sleep(3)
            # assert self.MainPage.is_next_btn_selected() is True
            assert self.MainPage.count_post_fields() == 2
            self.MainPage.click_user_btn()
            time.sleep(3)
            assert self.UserPage.is_home_btn_displayed() is True
            self.UserPage.click_home_btn()
            time.sleep(3)
            self.MainPage.click_user_btn()
            time.sleep(3)
        except AssertionError as err:
            self.pytest.fail(print(TestData.assert_error_msg, err))

    """this used to open an existing article to delete"""
    def test_delete_an_existing_article(self):
        try:
            self.UserPage = UserPage(self.driver)
            self.ArticlePage = ArticlePage(self.driver)
            # assert self.UserPage.is_article_title_displayed() == TestData.inputs_article_form_changes[0]
            # assert self.UserPage.is_article_text_displayed() == TestData.input_article_form_textarea_change
            self.UserPage.click_article_title()
            time.sleep(1)
            assert self.ArticlePage.is_delete_article_btn_displayed() is True
            self.ArticlePage.click_delete_article_btn()
            time.sleep(3)
        except AssertionError as err:
            self.pytest.fail(print(TestData.assert_error_msg, err))

    """this used to navigate to User page and count posts on the next page of the list"""
    """after delete an article"""
    def test_count_posts_after_delete_post(self):
        try:
            self.MainPage = MainPage(self.driver)
            assert self.MainPage.is_username_displayed() == TestData.reg_test_valid[0]
            self.MainPage.scroll_to_bottom_of_the_main_page()
            assert self.MainPage.is_next_btn_displayed() is True
            assert self.MainPage.is_next_btn_selected() is False
            self.MainPage.click_next_btn_topic_list()
            time.sleep(3)
            # assert self.MainPage.is_next_btn_selected() is True
            assert self.MainPage.count_post_fields() == 1
            assert self.MainPage.is_log_out_btn_displayed() is True
            self.MainPage.click_log_out_btn()
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
