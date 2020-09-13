import unittest
from hamcrest import assert_that, equal_to
from Thuc_Nguyen.hook.api.user_helper import UserHelper
from Thuc_Nguyen.hook.data_helper import DataHelper
from Thuc_Nguyen.hook.browser_helper import BrowserHelper
from Thuc_Nguyen.hook.pageobjects.login_page import LoginPage
from Thuc_Nguyen.hook.pageobjects.edit_profile_page import EditProfilePage
from Thuc_Nguyen.hook.pageobjects.view_profile_page import ViewProfilePage
from Thuc_Nguyen.hook.pageobjects.constants import URL


class CheckUserLocation(unittest.TestCase):

    def setUp(self):
        # update user location by API
        self.expected_location = DataHelper.read_json('../testdata/tc_check_user_location.json')["test_location"]
        location_data = {'location': self.expected_location}
        UserHelper.update_user(location_data)

        # set up variable to check UI
        self.username = DataHelper.read_json('../testdata/tc_check_user_location.json')["username"]
        email = DataHelper.read_json('../testdata/tc_check_user_location.json')["email"]
        password = DataHelper.read_json('../testdata/tc_check_user_location.json')["password"]
        self.driver = BrowserHelper.launch_chrome_browser()
        self.login_page = LoginPage(self.driver)
        self.view_profile_page = ViewProfilePage(self.driver)
        self.edit_profile_page = EditProfilePage(self.driver)
        # precondition: log in account
        self.login_page.navigate(URL['LOGIN_USER'])
        self.login_page.login(email, password)

    def test_view_user_location(self):
        # Navigate to User Profile of user
        self.login_page.navigate(URL['VIEW_LIST_COLLECTION_OF_USER'].format(username=self.username))
        # Navigate to Edit Profile Page
        self.view_profile_page.click_edit_profile_button()
        # Verify that user's location is correct
        assert_that(self.edit_profile_page.get_user_location(), equal_to(self.expected_location), 'Verify location')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
