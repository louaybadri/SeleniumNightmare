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

class Test8Explorezlespagessupplmentairestellesquelapagedaccueillapageproposetc():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_8Explorezlespagessupplmentairestellesquelapagedaccueillapageproposetc(self):
    self.driver.get("https://www.demoblaze.com/")
    self.driver.set_window_size(1552, 832)
    self.driver.find_element(By.CSS_SELECTOR, ".active > .nav-link").click()
    assert self.driver.find_element(By.ID, "cat").text == "CATEGORIES"
    self.driver.find_element(By.LINK_TEXT, "Contact").click()
    self.driver.find_element(By.CSS_SELECTOR, "#exampleModal .modal-header").click()
    assert self.driver.find_element(By.ID, "exampleModalLabel").text == "New message"
    self.driver.find_element(By.CSS_SELECTOR, "#exampleModal span").click()
    self.driver.find_element(By.LINK_TEXT, "About us").click()
    assert self.driver.find_element(By.ID, "videoModalLabel").text == "About us"
    self.driver.find_element(By.CSS_SELECTOR, "#videoModal .modal-header span").click()
    self.driver.find_element(By.ID, "cartur").click()
    self.driver.find_element(By.ID, "login2").click()
    self.driver.find_element(By.CSS_SELECTOR, "#logInModal span").click()
    assert self.driver.find_element(By.ID, "logInModalLabel").text == "Log in"
    self.driver.find_element(By.ID, "signin2").click()
    self.driver.find_element(By.CSS_SELECTOR, "#signInModal span").click()
    assert self.driver.find_element(By.ID, "signInModalLabel").text == "Sign up"
    self.driver.find_element(By.CSS_SELECTOR, ".active > .nav-link").click()
    assert self.driver.find_element(By.ID, "cat").text == "CATEGORIES"
  
