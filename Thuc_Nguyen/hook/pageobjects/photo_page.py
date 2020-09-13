from Thuc_Nguyen.hook.pageobjects.constants import PHOTO_PAGE
from Thuc_Nguyen.hook.pageobjects.base_page import BasePage


class PhotoPage(BasePage):

    def click_like_button(self):
        locator = PHOTO_PAGE['LIKE_BUTTON']
        return self.click_element(locator)

    def click_info_button(self):
        locator = PHOTO_PAGE['INFO_BUTTON']
        return self.click_element(locator)

    def get_camera_model(self):
        locator = PHOTO_PAGE['CAMERA_MODEL_VALUE']
        return self.get_element_text(locator)

    def get_focal_length(self):
        locator = PHOTO_PAGE['FOCAL_LENGTH_VALUE']
        return self.get_element_text(locator)
