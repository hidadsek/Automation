from Thuc_Nguyen.hook.pageobjects.constants import VIEW_PROFILE_PAGE
from Thuc_Nguyen.hook.pageobjects.base_page import BasePage


class ViewProfilePage(BasePage):

    def get_user_full_name(self):
        locator = VIEW_PROFILE_PAGE['PROFILE_NAME']
        return self.get_element_text(locator)

    def click_edit_profile_button(self):
        locator = VIEW_PROFILE_PAGE['EDIT_PROFILE_BUTTON']
        return self.click_element(locator)
