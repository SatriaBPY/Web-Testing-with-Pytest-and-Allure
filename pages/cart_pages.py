from .base_pages import BasePage
from locators.elemetn_locator import ElementLocator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CartPage (BasePage) :
    
    def cart_pages (self) :
        addproduct = self.driver.find_element(By.XPATH, ElementLocator.ADD_PRODUCT1[1])
        addproduct.click()
        
        carticon = self.driver.find_element(By.XPATH, ElementLocator.CART_ICON[1])
        carticon.click()
        
        time.sleep(2)
        validator = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ElementLocator.VALIDATOR_QTT[1]))
        )
        
        assert validator.text == '1'
        
        