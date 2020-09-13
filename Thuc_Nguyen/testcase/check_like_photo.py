import unittest
from hamcrest import assert_that, equal_to
from Thuc_Nguyen.hook.api.photo_helper import PhotoHelper
from Thuc_Nguyen.hook.api.user_helper import UserHelper
from Thuc_Nguyen.hook.data_helper import DataHelper
from Thuc_Nguyen.hook.browser_helper import BrowserHelper
from Thuc_Nguyen.hook.pageobjects.login_page import LoginPage
from Thuc_Nguyen.hook.pageobjects.likes_page import LikesPage
from Thuc_Nguyen.hook.pageobjects.photo_page import PhotoPage
from Thuc_Nguyen.hook.pageobjects.constants import URL


class CheckLikePhoto(unittest.TestCase):

    def setUp(self):
        # select and unlike photo by API beforehand to make the test clean
        self.username = UserHelper.get_user_data().json()['username']
        self.photo_id = PhotoHelper.get_random_photo().json()["id"]
        PhotoHelper.unlike_photo(self.photo_id)

        # set up variable to check UI
        email = DataHelper.read_json('../testdata/tc_check_like_photo.json')['email']
        password = DataHelper.read_json('../testdata/tc_check_like_photo.json')['password']
        self.driver = BrowserHelper.launch_chrome_browser()
        self.login_page = LoginPage(self.driver)
        self.photo_page = PhotoPage(self.driver)
        self.likes_page = LikesPage(self.driver)

        # precondition: log in account
        self.login_page.navigate(URL['LOGIN_USER'])
        self.login_page.login(email, password)

    def test_like_a_random_photo_successfully(self):
        # Select 1 random photo
        self.login_page.navigate(URL['PHOTO'].format(photo_id=self.photo_id))
        # Like this photo
        self.photo_page.click_like_button()
        # Check the photo is liked in the likes page
        self.photo_page.navigate(URL['VIEW_LIST_LIKED_PHOTO_OF_USER'].format(username=self.username))
        self.likes_page.click_the_first_photo()
        actual_photo_id = self.photo_page.get_current_url().split('/')[4]
        assert_that(actual_photo_id, equal_to(str(self.photo_id)), 'Verify photo liked')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
