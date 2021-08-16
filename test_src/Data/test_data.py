from selenium.webdriver.common.by import By


class TestData:
    BASE_URL = "http://localhost:1667/#/"
    HOME_PAGE_TITLE = "Conduit"
    MAIN_PAGE_TITLE = "conduit"

    reg_test_valid = ["test_user1", "test_user1@test.com", "Abcd1234"]
    reg_test_invalid_email = ["test_user3", "testuser_3#testcom", "Abcd1234"]
    reg_test_invalid_password = ["test_user3", "test_user3@test.com", "a1"]
    reg_test_invalid_username = ["", "test_user3@test.com", "Abcd1234"]
    login_test_existed_email = ["test_user1@test.com", "Abcd1234"]
    login_test_not_existed_email = ["test_user3@test.com", "Abcd1234"]

    inputs_article_form = ["Teszt Post", "Teszt", "unique"]
    input_article_form_textarea = "Ez egy rövid cikk, az applikáció tesztelése céljából"
    inputs_article_form_changes = ["Teszt Post változtatás", "Teszt változtatva", "uniquechange"]
    input_article_form_textarea_change = "Változtatás az utólagos szerkesztés funkció tesztelésének céljából"

    inputs_placeholder_value_reg = ["Username", "Email", "Password"]
    inputs_placeholder_value_login = ["Email", "Password"]
    inputs_placeholder_value_article = ["Article Title",
                                    "What's this article about?",
                                    "Write your article (in markdown)",
                                    "Enter tags"]
    inputs_placeholder_value_textarea_article = "Write your article (in markdown)"

    password_type_value = "password"

    text_reg_successful = "Your registration was successful!"

    text_reg_failed_msgs = ["Email must be a valid email.",
                            "Password must be 8 characters long and include 1 number, 1 uppercase letter, and 1 lowercase letter.",
                            "Username field required.",
                            "Email already taken."]

    text_login_failed = "Invalid user credentials."

    assert_error_msg = "Az oldal nem az elvárt funkcionalitásnak megfelelően működik, hiba oka:"

class HomePgWebElements:
    sign_up_btn = (By.XPATH, "//*[@id='app']/nav/div/ul/li[3]/a")
    sign_in_btn = (By.XPATH, "//*[@id='app']/nav/div/ul/li[2]/a")
    cookie_accept_btn = (By.XPATH, "//*[@id='cookie-policy-panel']/div/div[2]/button[2]")


class RegPgWebElements:
    input_fields = (By.TAG_NAME, "input")
    input_password = (By.XPATH, "//*[@id='app']/div/div/div/div/form/fieldset[3]/input")
    sign_up_btn = (By.XPATH, "//*[@id='app']/div/div/div/div/form/button")
    reg_failed_accept_btn = (By.XPATH, "/html/body/div[2]/div/div[4]/div/button")
    reg_failed_msg = (By.XPATH, "/html/body/div[2]/div/div[3]")
    home_btn = (By.XPATH, "//*[@id='app']/nav/div/ul/li[1]/a")


class MainPgWebElements:
    username_btn = (By.XPATH, "//*[@id='app']/nav/div/ul/li[4]/a")
    list_scroll_next_btn = (By.XPATH, "//*[@id='app']/div/div[2]/div/div[1]/div[2]/div/div/nav/ul/li[2]/a")
    post_fields = (By.XPATH, "//*[@id='app']/div/div[2]/div/div[1]/div[2]/div/div/div/a/h1")
    reg_successful_msg = (By.XPATH, "/html/body/div[2]/div/div[3]")
    reg_successful_accept_btn = (By.XPATH, "/html/body/div[2]/div/div[4]/div/button")
    log_out_btn = (By.XPATH, "//*[@id='app']/nav/div/ul/li[5]/a")
    new_article_btn = (By.XPATH, "//*[@id='app']/nav/div/ul/li[2]/a")
    conduit_title = (By.XPATH, "//*[@id='app']/div/div[1]/div/h1")
    main_page = (By.TAG_NAME, "body")


class LoginPgWebElements:
    input_fields = (By.TAG_NAME, "input")
    input_password = (By.XPATH, "//*[@id='app']/div/div/div/div/form/fieldset[2]/input")
    sign_in_btn = (By.XPATH, "//*[@id='app']/div/div/div/div/form/button")
    login_failed_msg = (By.XPATH, "/html/body/div[2]/div/div[3]")
    login_failed_accept_btn = (By.XPATH, "/html/body/div[2]/div/div[4]/div/button")
    home_btn = (By.XPATH, "//*[@id='app']/nav/div/ul/li[1]/a")


class EditArticlePgWebElements:
    input_fields = (By.TAG_NAME, "input")
    input_textarea = (By.TAG_NAME, "textarea")
    publish_article_btn = (By.XPATH, "//*[@id='app']/div/div/div/div/form/button")
    home_btn = (By.XPATH, "//*[@id='app']/nav/div/ul/li[1]/a")


class ArticlePgWebElements:
    article_title = (By.XPATH, "//*[@id='app']/div/div[1]/div/h1")
    article_text = (By.XPATH, "//*[@id='app']/div/div[2]/div[1]/div/div[1]/p")
    log_out_btn = (By.XPATH, "//*[@id='app']/nav/div/ul/li[5]/a")
    edit_article_btn = (By.XPATH, "//*[@id='app']/div/div[1]/div/div/span/a")
    delete_article_btn = (By.XPATH, "//*[@id='app']/div/div[1]/div/div/span/button")


class UserPgWebElements:
    article_title = (By.XPATH, "//*[@id='app']/div/div[2]/div/div/div[2]/div/div/div/a/h1")
    article_text = (By.XPATH, "//*[@id='app']/div/div[2]/div[1]/div/div[1]/p")
    home_btn = (By.XPATH, "//*[@id='app']/nav/div/ul/li[1]/a")
