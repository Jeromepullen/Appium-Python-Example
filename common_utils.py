# utils/common_utils.py

import os
from datetime import datetime

def take_screenshot(driver, test_name):
    screenshot_dir = 'screenshots'
    os.makedirs(screenshot_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")
    driver.save_screenshot(screenshot_path)
