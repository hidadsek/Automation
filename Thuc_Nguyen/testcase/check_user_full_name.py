import unittest
from hamcrest import assert_that, equal_to
from Thuc_Nguyen.hook.browser_helper import BrowserHelper
from Thuc_Nguyen.hook.data_helper import DataHelper
from Thuc_Nguyen.hook.pageobjects.home_page import HomePage
from Thuc_Nguyen.hook.pageobjects.login_page import LoginPage
from Thuc_Nguyen.hook.pageobjects.view_profile_page import ViewProfilePage
from Thuc_Nguyen.hook.pageobjects.constants import URL


class CheckUserFullName(unittest.TestCase):

    def setUp(self) -> None:
        # set up variable
        self.fullname = DataHelper.read_json('../testdata/tc_check_user_full_name.json')["fullname"]
        email = DataHelper.read_json('../testdata/tc_check_user_full_name.json')["email"]
        password = DataHelper.read_json('../testdata/tc_check_user_full_name.json')["password"]
        self.driver = BrowserHelper.launch_chrome_browser()
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.view_profile_page = ViewProfilePage(self.driver)
        # precondition: log in account
        self.login_page.navigate(URL['LOGIN_USER'])
        self.login_page.login(email, password)

    def test_view_user_full_name(self):
        # Navigate to User Profile of user
        self.home_page.click_personal_menu()
        self.home_page.select_menu_item('View profile')
        # Verify that user's full name is correct
        assert_that(self.view_profile_page.get_user_full_name(), equal_to(self.fullname), 'Verify user full name')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
