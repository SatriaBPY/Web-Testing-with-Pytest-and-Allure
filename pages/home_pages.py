from .base_pages import BasePage
from locators.elemetn_locator import ElementLocator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class HomePage (BasePage) :
    def home_page (self) :
        validator = WebDriverWait(self.driver, 10). until(
            EC.presence_of_element_located((By.XPATH, ElementLocator.VALIDATOR_HOMEPAGE[1]))
        )
        
        assert validator
        
        addproduct1 = self.driver.find_element(By.XPATH, ElementLocator.ADD_PRODUCT1[1])
        addproduct1.click()
        
        addproduct2= self.driver.find_element(By.XPATH, ElementLocator.ADD_PRODUCT2[1])
        addproduct2.click()
        
        time.sleep(2)
        removeprod1 = self.driver.find_element(By.XPATH, ElementLocator.REMOVE_PROD1[1])
        removeprod1.click()
        
        time.sleep(2)
        removeprod2 = self.driver.find_element(By.XPATH, ElementLocator.REMOVE_PROD2[1])
        removeprod2.click()