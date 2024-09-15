# tests/test_sample.py

from utils.base_test import BaseTest
from utils.common_utils import take_screenshot
from pages.home_page import HomePage

class SampleTest(BaseTest):
    
    def test_tap_element(self):
        try:
            home_page = HomePage(self.driver)
            home_page.tap_some_element()
        except Exception as e:
            take_screenshot(self.driver, 'test_tap_element')
            raise e
