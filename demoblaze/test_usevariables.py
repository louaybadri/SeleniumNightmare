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

class TestUsevariables():
  def setup_method(self, method):
    print("Setting up the test")
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    print("Tearing down the test")
    self.driver.quit()
  
  def test_usevariables(self):
    self.setup_method(None)
    print("Setting up variables")
    self.vars["FakeName"] = "this is a name"
    self.vars["FakeAdd"] = "this is an address"
    self.vars["FakeCity"] = "this is a city"
    
    print("Navigating to the test page")
    self.driver.get("https://www.demoblaze.com/")
    self.driver.set_window_size(1051, 797)
    
    print("Adding 'Samsung galaxy s6' to the cart")
    self.driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()
    self.driver.find_element(By.LINK_TEXT, "Add to cart").click()
    assert self.driver.switch_to.alert.text == "Product added"
    
    print("Navigating to the cart and proceeding to checkout")
    self.driver.find_element(By.ID, "cartur").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    
    print("Filling out the checkout form")
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys(self.vars["FakeName"])
    self.driver.find_element(By.ID, "country").send_keys(self.vars["FakeAdd"])
    self.driver.find_element(By.ID, "city").send_keys(self.vars["FakeCity"])
    self.driver.find_element(By.ID, "card").send_keys(self.vars["FakeName"])
    self.driver.find_element(By.ID, "month").send_keys("8")
    self.driver.find_element(By.ID, "year").send_keys("2004")
    
    print("Submitting the form")
    self.driver.find_element(By.CSS_SELECTOR, "#orderModal .btn-primary").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(6)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#orderModal .btn-primary").click()
    
    print("Checking the result")
    assert self.driver.find_element(By.CSS_SELECTOR, "h2:nth-child(6)").text == "Thank you for your purchase!"
    print("Test completed successfully")

# Running the test
print("Starting the test")
TestUsevariables().test_usevariables()
print("Test execution finished")