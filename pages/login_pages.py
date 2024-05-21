from .base_pages import BasePage  
from locators.elemetn_locator import ElementLocator
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage(BasePage):
    
    def open_login_page(self, url):
        self.driver.get(url)

    def login(self, username, password):
        # Tunggu elemen validator muncul
        validator = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, ElementLocator.VALIDATOR[1]))
        )
        
        assert validator
        
        # Cari input username dan password, kemudian masukkan nilai
        usernames = self.driver.find_element(By.XPATH, ElementLocator.USERNAME_INPUT[1])
        usernames.send_keys(username)
        
        passwords = self.driver.find_element(By.XPATH, ElementLocator.PASSWORD_INPUT[1])
        passwords.send_keys(password)
        
        # Klik tombol login
        login_button = self.driver.find_element(By.XPATH, ElementLocator.LOGIN_BUTTON[1])
        login_button.click()
