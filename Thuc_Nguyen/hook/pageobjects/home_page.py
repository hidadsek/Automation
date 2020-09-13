from Thuc_Nguyen.hook.pageobjects.constants import HOME_PAGE
from Thuc_Nguyen.hook.pageobjects.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    def navigate_to_login_page(self):
        locator = HOME_PAGE['LOGIN_BUTTON']
        self.click_element(locator)

    def click_personal_menu(self):
        locator = HOME_PAGE['MENU_BUTTON']
        self.click_element(locator)

    def select_menu_item(self, item):
        item_link = HOME_PAGE['MENU_ITEM'].format(item=item)
        locator = (By.XPATH, item_link)
        self.click_element(locator)



