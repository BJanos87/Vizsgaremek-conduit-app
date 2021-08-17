from test_src.Tests.test09_cookie_check.conftest import PyFix
from test_src.Pages.HomePage import HomePage
from test_src.Data.test_data import TestData
import time


class TestCookie(PyFix):

    """this used to check the title of the loaded url, and check the Sign In button"""
    """this used to check cookie status, after accept that"""
    def test_homepage_cookie(self):
        try:
            self.HomePage = HomePage(self.driver)
            assert self.HomePage.get_home_page_url() == TestData.BASE_URL
            assert self.HomePage.get_home_page_title() == TestData.HOME_PAGE_TITLE
            assert self.HomePage.is_sign_in_btn_displayed() is True
            assert self.HomePage.get_cookie_status_from_homepage() == 1
            self.HomePage.click_cookie_accept_btn()
            self.HomePage.reload_home_page()
            time.sleep(3)
            assert self.HomePage.get_cookie_status_from_homepage() == 2
            assert self.HomePage.check_value_cookie_from_homepage() == "accept"
            time.sleep(1)
        except AssertionError as err:
            self.pytest.fail(print(TestData.assert_error_msg, err))

    """this used to check that the user not logged in"""
    def test_homepage_is_displayed(self):
        try:
            self.HomePage = HomePage(self.driver)
            assert self.HomePage.get_home_page_url() == TestData.BASE_URL
            assert self.HomePage.get_home_page_title() == TestData.HOME_PAGE_TITLE
            assert self.HomePage.is_sign_in_btn_displayed() is True
        except AssertionError as err:
            self.pytest.fail(print(TestData.assert_error_msg, err))
