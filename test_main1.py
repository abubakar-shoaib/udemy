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

class TestMain1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_main1(self):
    self.driver.get("https://www.udemy.com/")
    self.driver.set_window_size(1440, 801)
    self.driver.find_element(By.CSS_SELECTOR, ".desktop-header-module--gap-auth-button--f25sS > .ud-btn-primary > span").click()
    self.driver.find_element(By.ID, "form-group--1").click()
    self.driver.find_element(By.ID, "form-group--1").send_keys("Abubakar Shoaib")
    self.driver.find_element(By.ID, "form-group--3").send_keys("abubakarphp@gmail.com")
    self.driver.find_element(By.ID, "form-group--5").click()
    self.driver.find_element(By.ID, "form-group--5").send_keys("Shhamim03@")
    self.driver.find_element(By.CSS_SELECTOR, ".auth-layout--auth-grid-layout--E7OfM").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ud-btn-brand > span").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".ud-btn-brand")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
  
