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

class TestVrifiezlaconfirmationdelacommandeaprslepaiement():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_vrifiezlaconfirmationdelacommandeaprslepaiement(self):
    self.driver.get("https://www.demoblaze.com/")
    self.driver.set_window_size(1051, 797)
    self.driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()
    self.driver.find_element(By.LINK_TEXT, "Add to cart").click()
    assert self.driver.switch_to.alert.text == "Product added"
    self.driver.find_element(By.ID, "cartur").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("Leslie Holden")
    self.driver.find_element(By.ID, "country").send_keys("Commodi esse quidem")
    self.driver.find_element(By.ID, "city").send_keys("Voluptatem qui offic")
    self.driver.find_element(By.ID, "card").send_keys("Perferendis reprehen")
    self.driver.find_element(By.ID, "month").send_keys("8")
    self.driver.find_element(By.ID, "year").send_keys("2004")
    self.driver.find_element(By.CSS_SELECTOR, "#orderModal .btn-primary").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(6)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#orderModal .btn-primary").click()
    self.driver.find_element(By.CSS_SELECTOR, "h2:nth-child(6)").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "h2:nth-child(6)").text == "Thank you for your purchase!"
  
