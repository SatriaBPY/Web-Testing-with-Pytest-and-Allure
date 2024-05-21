from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

class WebDriverSetup:
    def __init__(self, chrome_option=None):
        if chrome_option is None:
            chrome_option = webdriver.ChromeOptions()
            chrome_option.add_experimental_option("detach", True)
        
        chrome_path = Service (executable_path="driver/chromedriver.exe")
        self.driver = webdriver.Chrome(service=chrome_path, options=chrome_option)
        self.driver.implicitly_wait(10)
