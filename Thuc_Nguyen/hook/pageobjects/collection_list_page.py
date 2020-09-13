from Thuc_Nguyen.hook.pageobjects.constants import COLLECTION_LIST_PAGE
from Thuc_Nguyen.hook.pageobjects.base_page import BasePage
from selenium.webdriver.common.by import By


class CollectionListPage(BasePage):

    def click_on_collection(self, collection_pos):
        collection_element = COLLECTION_LIST_PAGE['COLLECTION_IN_LIST'].format(collection_pos=collection_pos)
        locator = {By.XPATH, collection_element}
        return self.click_element(locator)
