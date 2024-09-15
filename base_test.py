# utils/base_test.py

import unittest
from utils.appium_setup import get_driver

class BaseTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = get_driver()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        if self.driver:
            self.driver.quit()
