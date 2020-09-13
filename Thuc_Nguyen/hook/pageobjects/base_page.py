from Thuc_Nguyen.conf.constants import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def refresh(self):
        self.driver.refresh()

    def get_current_url(self):
        return self.driver.current_url

    def wait_element_to_be_clickable(self, locator, timeout=TIME_OUT):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(ec.element_to_be_clickable(locator))

    def wait_element_to_be_visible(self, locator, timeout=TIME_OUT):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(ec.visibility_of_element_located(locator))

    def wait_all_elements_to_be_present(self, locator, timeout=TIME_OUT):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(ec.presence_of_all_elements_located(locator))

    def click_element(self, locator):
        self.wait_element_to_be_clickable(locator).click()

    def input_text(self, locator, value):
        self.wait_element_to_be_clickable(locator).send_keys(value)

    def get_element_attribute(self, locator, attribute):
        return self.wait_element_to_be_visible(locator).get_attribute(attribute)

    def get_element_text(self, locator):
        return self.wait_element_to_be_visible(locator).text

    def get_elements_attribute(self, locator, attribute):
        elements = self.wait_all_elements_to_be_present(locator)
        data_list = []
        for element in elements:
            data_list.append(element.get_attribute(attribute))
        return data_list




