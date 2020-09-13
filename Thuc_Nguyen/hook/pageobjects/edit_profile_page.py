from Thuc_Nguyen.hook.pageobjects.constants import EDIT_PROFILE_PAGE
from Thuc_Nguyen.hook.pageobjects.base_page import BasePage


class EditProfilePage(BasePage):

    def get_user_location(self):
        locator = EDIT_PROFILE_PAGE['PROFILE_LOCATION']
        return self.get_element_attribute(locator, 'value')
