from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from utils.config import Config

class DriverFactory:
    @staticmethod
    def get_driver():
        service = Service(ChromeDriverManager().install())

        driver = webdriver.Chrome(service=service)

        driver.maximize_window()

        driver.implicitly_wait(Config.IMPLICIT_WAIT)

        driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)

        return driver