# pages/home_page.py

class HomePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.some_element_id = 'some_element_id'

    def tap_some_element(self):
        self.driver.find_element_by_accessibility_id(self.some_element_id).click()
