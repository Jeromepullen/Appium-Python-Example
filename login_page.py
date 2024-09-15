# pages/login_page.py

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_field_id = 'username_field'
        self.password_field_id = 'password_field'
        self.login_button_id = 'login_button'

    def enter_username(self, username):
        self.driver.find_element_by_accessibility_id(self.username_field_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_accessibility_id(self.password_field_id).send_keys(password)

    def tap_login_button(self):
        self.driver.find_element_by_accessibility_id(self.login_button_id).click()
