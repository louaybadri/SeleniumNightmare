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


class TestTest1():

    def setup_method(self, method):
        print("Setting up the test")
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        print("Tearing down the test")
        self.driver.quit()

    def test_test1(self):
        self.setup_method(None)  # Ensure setup is called
        print("Navigating to the test page")
        self.driver.get("https://safatelli.github.io/tp-test-logiciel/assets/hello.html")
        
        print("Entering 'Louay' into the username field and submitting")
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").send_keys("Louay \n")
        self.driver.find_element(By.CSS_SELECTOR, "button").click()
        assert self.driver.find_element(By.ID, "message").text == "Bonjour, Louay !"
        
        print("Entering 'Badri' into the username field and submitting")
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").send_keys("Badri")
        self.driver.find_element(By.CSS_SELECTOR, "button").click()
        assert self.driver.find_element(By.ID, "message").text == "Bonjour, Badri !"
        # assert self.driver.find_element(By.ID, "message").text == "Bonjour, Louay Badri !"

        print("Test completed successfully")


# Running the test
print("Starting the test")
TestTest1().test_test1()
print("Test execution finished")