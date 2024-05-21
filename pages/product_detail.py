from .base_pages import BasePage
from locators.elemetn_locator import ElementLocator
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class ProductDetail (BasePage):
    def product_detail (self):
        openprod = self.driver.find_element(By.XPATH, ElementLocator.VALIDATOR_HOMEPAGE[1])
        openprod.click()
        
        validator2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ElementLocator.VALIDATOR_PROD[1]))
        )
        
        assert validator2.text == "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."
        
        addproduct = self.driver.find_element(By.XPATH, ElementLocator.ADD_PRODUCT[1])
        addproduct.click()
        
        time.sleep(2)
        removeprod = self.driver.find_element(By.XPATH, ElementLocator.REMOVE_PROD[1])
        removeprod.click()
        
        backtohome = self.driver.find_element(By.XPATH, ElementLocator.BACKTO_HOME[1])
        backtohome.click()