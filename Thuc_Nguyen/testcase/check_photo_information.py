import unittest
from hamcrest import assert_that, equal_to
from Thuc_Nguyen.hook.api.photo_helper import PhotoHelper
from Thuc_Nguyen.hook.api.user_helper import UserHelper
from Thuc_Nguyen.hook.data_helper import DataHelper
from Thuc_Nguyen.hook.browser_helper import BrowserHelper
from Thuc_Nguyen.hook.pageobjects.login_page import LoginPage
from Thuc_Nguyen.hook.pageobjects.edit_profile_page import EditProfilePage
from Thuc_Nguyen.hook.pageobjects.photo_list_page import PhotoListPage
from Thuc_Nguyen.hook.pageobjects.photo_page import PhotoPage
from Thuc_Nguyen.hook.pageobjects.view_profile_page import ViewProfilePage
from Thuc_Nguyen.hook.pageobjects.constants import URL


class CheckCameraModelAndFocalLength(unittest.TestCase):

    def setUp(self):
        # update info camera model and focal length of all photos by API
        self.camera_model = DataHelper.read_json('../testdata/tc_check_photo_information.json')['camera_model']
        self.focal_length = DataHelper.read_json('../testdata/tc_check_photo_information.json')['focal_length']
        self.username = UserHelper.get_user_data().json()['username']
        list_photos_of_user = UserHelper.get_list_photos_of_user(self.username).json()
        for photo in list_photos_of_user:
            list_photo_update_data = {'exif[model]': self.camera_model,
                                      'exif[focal_length]': self.focal_length}
            PhotoHelper.update_photo(photo_id=photo['id'], data=list_photo_update_data)

        # set up variable to check UI
        email = DataHelper.read_json('../testdata/tc_check_photo_information.json')["email"]
        password = DataHelper.read_json('../testdata/tc_check_photo_information.json')["password"]
        self.driver = BrowserHelper.launch_chrome_browser()
        self.login_page = LoginPage(self.driver)
        self.view_profile_page = ViewProfilePage(self.driver)
        self.edit_profile_page = EditProfilePage(self.driver)
        self.photo_page = PhotoPage(self.driver)
        self.photo_list_page = PhotoListPage(self.driver)

        # precondition: log in account
        self.login_page.navigate(URL['LOGIN_USER'])
        self.login_page.login(email, password)

    def test_view_camera_model_and_focal_length_of_photo(self):
        # Navigate to User Profile (Photos of User)
        self.login_page.navigate(URL['VIEW_LIST_PHOTO_OF_USER'].format(username=self.username))

        # Select 1 photo
        self.photo_list_page.click_the_first_photo_in_list()

        # Open photo info popup
        self.photo_page.click_info_button()

        # Verify photo's camera model and focal length
        assert_that(self.photo_page.get_camera_model(), equal_to(self.camera_model), 'Verify camera model')
        assert_that(self.photo_page.get_focal_length(), equal_to(self.focal_length), 'Verify focal length')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
