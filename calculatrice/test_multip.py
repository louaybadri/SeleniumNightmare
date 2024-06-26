# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestMultip():
  def setup_method(self, method):
    print("Setting up the test")
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    print("Tearing down the test")
    self.driver.quit()
  
  def test_multip(self):
    self.setup_method(None)
    print("Navigating to the test page")
    self.driver.get("https://safatelli.github.io/tp-test-logiciel/assets/calc.html")
    self.driver.set_window_size(1534, 605)
    
    print("Entering '12' into the num1 field")
    self.driver.find_element(By.ID, "num1").click()
    self.driver.find_element(By.ID, "num1").send_keys("12")
    
    print("Selecting '*' operator")
    self.driver.find_element(By.ID, "operator").click()
    dropdown = self.driver.find_element(By.ID, "operator")
    dropdown.find_element(By.XPATH, "//option[. = '*']").click()
    
    print("Entering '-2' into the num2 field and submitting")
    self.driver.find_element(By.ID, "num2").click()
    self.driver.find_element(By.ID, "num2").send_keys("-2")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    
    print("Checking the result")
    assert self.driver.find_element(By.ID, "result").text == "Résultat : -24"
    print("Test completed successfully")

# Running the test
print("Starting the test")
TestMultip().test_multip()
print("Test execution finished")