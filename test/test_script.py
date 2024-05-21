from config.web_drivers import WebDriverSetup
from pages.login_pages import LoginPage
from pages.home_pages import HomePage
from pages.product_detail import ProductDetail
from pages.cart_pages import CartPage
from pages.checkout_pages import CheckoutPages
import pytest
import allure

@pytest.fixture(scope="module")
def driver ():
    web_driver_setup = WebDriverSetup()
    driver = web_driver_setup.driver
    yield driver
    
    driver.quit()
    
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
     ("standard_user", "secret_sauce")
   
])

@allure.feature("Login")
@allure.story("User should be able to login with valid credentials")
@allure.severity(allure.severity_level.CRITICAL)

def test_login(driver, username, password):
    print(f"Running test_login with username: {username}")
    
    login_pages = LoginPage(driver)
    
    login_pages.open_login_page("https://www.saucedemo.com")
    
    login_pages.login(username, password)

@allure.feature("Homepage")
@allure.story("User should be able showing of list product")
@allure.severity(allure.severity_level.NORMAL)
def test_homepage(driver) :
    print("Running test_homepage")
    
    homepages = HomePage(driver)
    homepages.home_page()

@allure.feature("Product Detail")
@allure.story("User should be able to see product descrition and price")
@allure.severity(allure.severity_level.NORMAL)

def test_detail_prod(driver) :
    print("Running test_detail_prod")
    
    detailprod = ProductDetail(driver)
    detailprod.product_detail()

@allure.feature("Cart")  
@allure.story("User should be mange product in cart")
@allure.severity(allure.severity_level.NORMAL)
def test_cart (driver):
    
    carts = CartPage(driver)
    carts.cart_pages()
    
@pytest.mark.parametrize("firstname, lastname, zipcode", [
    ("samosa", "reduce", "3324")
   
])

@allure.feature("Checkout")
@allure.story("User should be finish the checkout")
@allure.severity(allure.severity_level.NORMAL)
def test_checkout (driver, firstname, lastname, zipcode) :
    checkout = CheckoutPages(driver)
    checkout.checkout(firstname, lastname, zipcode)