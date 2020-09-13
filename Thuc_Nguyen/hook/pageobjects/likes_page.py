from Thuc_Nguyen.hook.pageobjects.constants import LIKES_PAGE
from Thuc_Nguyen.hook.pageobjects.base_page import BasePage
from selenium.webdriver.common.by import By


class LikesPage(BasePage):

    def click_the_first_photo(self):
        locator = LIKES_PAGE['PHOTO_IN_LIKES']
        return self.click_element(locator)
