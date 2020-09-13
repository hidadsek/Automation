from Thuc_Nguyen.hook.pageobjects.constants import COLLECTION_PAGE
from Thuc_Nguyen.hook.pageobjects.base_page import BasePage
from selenium.webdriver.common.by import By


class CollectionPage(BasePage):

    def click_photo_in_collection(self, column_pos, row_pos):
        photo_element = COLLECTION_PAGE['PHOTO_IN_COLLECTION'].format(column_pos=column_pos, row_pos=row_pos)
        locator = {By.XPATH, photo_element}
        return self.click_element(locator)

    def get_list_href_photo_in_collection(self):
        locator = COLLECTION_PAGE['LIST_PHOTO_IN_COLLECTION']
        return self.get_elements_attribute(locator, 'href')
