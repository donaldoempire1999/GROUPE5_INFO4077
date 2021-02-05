import unittest
from appium import webdriver

# Android environment
import unittest
from appium import webdriver

desired_cap = {
  "deviceName": "HTC Desire 530",
  "udid": "HT69W0003763",
  "platFormName": "Android",
  "platformVersion": "730",
  "appPackage": "com.example.covid_app",
  "appActivity": "com.example.covid_app.MainActivity"
}

driver = webdriver.Remote("http://localhost:4723", desired_cap)
driver.implicitly_wait(30)

driver.find_element_by_id("com.example.covid_app:id/preventionRecyclerView").click()