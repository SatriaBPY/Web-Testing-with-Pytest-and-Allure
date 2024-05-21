from selenium.webdriver.common.by import By

class ElementLocator :
    #Login
    USERNAME_INPUT = (By.XPATH, "//input[@id='user-name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")
    VALIDATOR = (By.XPATH, "//div[@id='login_credentials']")
    
    #Homepage
    VALIDATOR_HOMEPAGE = (By.XPATH, "//img[@alt='Sauce Labs Backpack']")
    ADD_PRODUCT1 = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    ADD_PRODUCT2 = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
    REMOVE_PROD1 = (By.XPATH, "//button[@id='remove-sauce-labs-backpack']")
    REMOVE_PROD2 = (By.XPATH, "//button[@id='remove-sauce-labs-bike-light']")
    
    #Product Detail
    VALIDATOR_PROD = (By.CSS_SELECTOR, ".inventory_details_desc")
    ADD_PRODUCT = (By.XPATH, "//button[@id='add-to-cart']")
    REMOVE_PROD = (By.XPATH, "//button[@id='remove']")
    BACKTO_HOME = (By.XPATH, "//button[@id='back-to-products']")
    
    #Cart
    VALIDATOR_QTT = (By.XPATH, "//div[@class='cart_quantity']")
    
    #Checkout
    VALIDATOR_CHECK = (By.XPATH, "//div[@class='checkout_info']")
    CHECKOUT = (By.XPATH, "//button[@id='checkout']")
    FIRST_NAME = (By.XPATH, "//input[@id='first-name']")
    LAST_NAME = (By.XPATH, "//input[@id='last-name']")
    ZIP_CODE = (By.XPATH, "//input[@id='postal-code']")
    CART_ICON = (By.XPATH, "//a[.='1']")
    CONTINUE = (By.XPATH, "//input[@id='continue']")
    
    #checkout2
    VALIDATOR_CHECK2 = (By.XPATH, "//div[@class='summary_total_label']")
    VALIDATOR_CHECK3 = (By.XPATH, "//h2[@class='complete-header']")
    FINISH_BUTTON = (By.XPATH, "//button[@id='finish']")