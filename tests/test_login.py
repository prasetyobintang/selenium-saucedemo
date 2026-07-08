from pages.login_page import LoginPage
from utils.driver_factory import DriverFactory
from utils.config import Config

def test_login_success():
    
    driver = DriverFactory.get_driver()
    
    driver.get(Config.BASE_URL)

    login_page = LoginPage(driver)
    
    login_page.login(
        "standard_user",
        "secret_sauce"
    )
    
    assert "inventory" in driver.current_url

    driver.quit()