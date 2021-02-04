from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


desired_cap = {
    # Set your access credentials
    "browserstack.user": "donaldfotso1",
    "browserstack.key": "r8aTdQab2LMpakRtw3CG",

    # Set URL of the application under test
    "app": "bs://<app-id>",

    # Specify device and os_version for testing
    "device": "Google Pixel 3",
    "os_version": "9.0",

    # Set other BrowserStack capabilities
    "project": "First Python project",
    "build": "Python Android",
    "name": "first_test"
}

# Initialize the remote Webdriver using BrowserStack remote URL
# and desired capabilities defined above
driver = webdriver.Remote(
    command_executor="http://hub-cloud.browserstack.com/wd/hub",
    desired_capabilities=desired_cap
)

# Write your custom code here

# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()
