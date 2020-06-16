from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    # EMAIL_ADDRESS_LOGIN_TEXTFIELD = (By.CSS_SELECTOR, "id_login-username")
    # PASSWORD_LOGIN_TEXTFIELD = (By.CSS_SELECTOR, "#id_login-password")
    # LOGIN_BUTTON = (By.CSS_SELECTOR, "#login_form .btn-lg")
    # EMAIL_ADDRESS_REGISTER_TEXTFIELD = (By.CSS_SELECTOR, "#id_registration-email")
    # PASSWORD_REGISTER_TEXTFIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    # CONFIRM_PASSWORD_REGISTER_TEXTFIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    # REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form .btn-lg")
