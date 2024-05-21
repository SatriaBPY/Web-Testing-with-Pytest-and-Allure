from .base_pages import BasePage
from locators.elemetn_locator import ElementLocator
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class CheckoutPages (BasePage):
    def checkout (self, firstname, lastname, zipcode):
        validotor = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ElementLocator.VALIDATOR_QTT[1]))
        )
        
        assert validotor.text == '1'
        
        checkbutton = self.driver.find_element(By.XPATH, ElementLocator.CHECKOUT[1])
        checkbutton.click()
        
        time.sleep(2)
        validator2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ElementLocator.VALIDATOR_CHECK[1]))
        )
        
        assert validator2
        
        firstname_field = self.driver.find_element(By.XPATH, ElementLocator.FIRST_NAME[1])
        firstname_field.send_keys(firstname)
        
        lastname_field = self.driver.find_element(By.XPATH, ElementLocator.LAST_NAME[1])
        lastname_field.send_keys(lastname)
        
        zipcode_field = self.driver.find_element(By.XPATH, ElementLocator.ZIP_CODE[1])
        zipcode_field.send_keys(zipcode)
        
        continuecheck = self.driver.find_element(By.XPATH, ElementLocator.CONTINUE[1])
        continuecheck.click()
        
        time.sleep(2)
        validator3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ElementLocator.VALIDATOR_CHECK2[1]))
        )
        
        validator3.text != "0"
        
        finish = self.driver.find_element(By.XPATH, ElementLocator.FINISH_BUTTON[1])
        finish.click()
        
        time.sleep(2)
        validator4 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ElementLocator.VALIDATOR_CHECK3[1]))
        )
        
        assert validator4.text == "Thank you for your order!"