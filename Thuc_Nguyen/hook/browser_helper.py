from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Thuc_Nguyen.conf.constants import CHROME_DRIVER_PATH


class BrowserHelper:
    @staticmethod
    def launch_chrome_browser_with_old_file():
        # disable warning "Chrome is being controlled by automated test software"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        # disable save password pop-up
        prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=chrome_options, executable_path=CHROME_DRIVER_PATH)
        driver.maximize_window()
        return driver

    @staticmethod
    def launch_chrome_browser():
        # disable warning "Chrome is being controlled by automated test software"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        # disable save password pop-up
        prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=chrome_options, executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        return driver
