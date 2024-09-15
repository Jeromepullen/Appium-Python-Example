# tests/test_login.py

from utils.base_test import BaseTest
from pages.login_page import LoginPage

class LoginTest(BaseTest):
    
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username('test_user')
        login_page.enter_password('test_password')
        login_page.tap_login_button()
        
        # Add assertions to validate login success
        success_element = self.driver.find_element_by_accessibility_id('success_message')
        self.assertTrue(success_element.is_displayed(), "Login failed")
