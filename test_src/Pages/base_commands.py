from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class BaseCommands:

    """This class is the parent of all pages"""
    """It contains all the generic methods and utilities for all the pages"""

    def __init__(self, driver):
        self.driver = driver

    """this used to open webpage"""
    def get_url(self, url):
        self.driver.get(url)

    """this used get current title"""
    def get_current_title(self):
        return self.driver.title

    """this used to get current url"""
    def get_current_url(self):
        return self.driver.current_url

    """this used to get cookie status"""
    def get_cookies_list(self):
        cookies = self.driver.get_cookies()
        return cookies

    """this used to check value of the cookie"""
    def check_value_cookie(self):
        cookies = self.driver.get_cookies()
        return cookies[0]

    """this used to check, that a web element is displayed"""
    def is_element_displayed(self, by_locator):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator))
        return element.is_displayed()

    """this used to check, that web elements is displayed"""
    def is_elements_displayed(self, by_locator):
        elements = WebDriverWait(self.driver, 5).until(EC.visibility_of_any_elements_located(by_locator))
        for element in elements:
            return element.is_displayed()

    """this used to check, that a web element is selected"""
    def is_element_selected(self, by_locator):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator))
        return element.is_selected()

    """this used to fill an input field"""
    def do_send_key(self, by_locator, text):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator))
        element.send_keys(text)

    """this used to fill some input fields"""
    def do_send_key_elements(self, by_locator, text):
        elements = WebDriverWait(self.driver, 5).until(EC.visibility_of_any_elements_located(by_locator))
        for i in range(len(elements)):
            elements[i].send_keys(text[i])

    """this used to clear an input field"""
    def clear_input_element(self, by_locator):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator))
        element.clear()

    """this used to clear some input fields"""
    def clear_input_elements(self, by_locator):
        elements = WebDriverWait(self.driver, 5).until(EC.visibility_of_any_elements_located(by_locator))
        for i in range(len(elements)):
            elements[i].clear()

    """this used to click on a web element"""
    def do_click(self, by_locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(by_locator)).click()

    """this used to get text from a web element(innerHTML)"""
    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator))
        return element.text

    """this used to get text from some web elements(innerHTML)"""
    def get_elements_text(self, by_locator):
        elements = WebDriverWait(self.driver, 5).until(EC.visibility_of_any_elements_located(by_locator))
        for i in range(len(elements)):
            return elements[i].text

    """this used to get an attribute value from a web element"""
    def check_element_attribute(self, by_locator, attribute, test_data):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute(attribute) == test_data

    """this used to get an attribute value from some web elements"""
    def check_elements_attribute(self, by_locator, attribute, test_datas):
        elements = WebDriverWait(self.driver, 5).until(EC.visibility_of_any_elements_located(by_locator))
        for i in range(len(elements)):
            return elements[i].get_attribute(attribute) == test_datas[i]

    """this used to scroll to the bottom of the page"""
    def scroll_to_bottom_of_the_page(self, by_locator):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator))
        element.send_keys(Keys.END)

    """this used to count web elements on the page"""
    def count_web_elements(self, by_locator):
        elements = WebDriverWait(self.driver, 5).until(EC.visibility_of_any_elements_located(by_locator))
        return (len(elements))

    """this used to save a list into a text file"""
    def save_list_into_txt_file(self, file, by_locator):
        elements = WebDriverWait(self.driver, 5).until(EC.visibility_of_any_elements_located(by_locator))
        with open(file, "w", encoding='utf-8') as f:
            f.write('')
        for i in range(len(elements)):
            with open(file, 'a', encoding='utf-8') as f:
                f.write(elements[i].text)
                f.write('\n')

    """this used to compare web elements with saved txt file"""
    def check_saved_list_from_txt_file(self, file, by_locator):
        elements = WebDriverWait(self.driver, 5).until(EC.visibility_of_any_elements_located(by_locator))
        formatted_text_file = []
        with open(file, 'r', encoding='utf-8') as f:
            result = f.readlines()
            for row in result:
                row = row.replace("\n", '')
                formatted_text_file.append(row)
        for i, element in enumerate(elements):
            assert element.text == formatted_text_file[i]

    """this used to fill an input with test data from a txt file"""
    def fill_input_from_txt(self, file, by_locator):
        with open(file, 'r', encoding='utf-8') as f:
            result = f.readline()
        self.do_send_key(by_locator, result)

    """this used to fill inputs with test data from a txt file"""
    def fill_inputs_from_txt(self, file, by_locator):
        formatted_inputs = []
        with open(file, 'r', encoding='utf-8') as f:
            result = f.readlines()
            for row in result:
                row = row.replace("\n", '')
                formatted_inputs.append(row)
        self.do_send_key_elements(by_locator, formatted_inputs)
