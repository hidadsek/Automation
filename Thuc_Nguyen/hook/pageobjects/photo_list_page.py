from Thuc_Nguyen.hook.pageobjects.constants import PHOTO_LIST_PAGE
from Thuc_Nguyen.hook.pageobjects.base_page import BasePage
from selenium.webdriver.common.by import By


class PhotoListPage(BasePage):

    def click_the_first_photo_in_list(self):
        locator = PHOTO_LIST_PAGE['PHOTO_IN_LIST']
        return self.click_element(locator)
