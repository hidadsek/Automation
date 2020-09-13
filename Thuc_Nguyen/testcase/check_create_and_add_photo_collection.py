import unittest
from hamcrest import assert_that, equal_to
from Thuc_Nguyen.hook.api.collection_helper import CollectionHelper
from Thuc_Nguyen.hook.api.user_helper import UserHelper
from Thuc_Nguyen.hook.data_helper import DataHelper
from Thuc_Nguyen.hook.browser_helper import BrowserHelper
from Thuc_Nguyen.hook.pageobjects.login_page import LoginPage
from Thuc_Nguyen.hook.pageobjects.collection_page import CollectionPage
from Thuc_Nguyen.hook.pageobjects.collection_list_page import CollectionListPage
from Thuc_Nguyen.hook.pageobjects.photo_page import PhotoPage
from Thuc_Nguyen.hook.pageobjects.constants import URL


class CheckCreateAndAddPhoto(unittest.TestCase):

    def setUp(self):

        # create a collection and add a photo to created collection by API
        collection_title = \
            DataHelper.read_json('../testdata/tc_check_create_and_add_photo_collection.json')['test_collection_title']
        collection_data = {'title': collection_title}
        self.collection_id = CollectionHelper.create_collection(collection_data).json()['id']
        self.username = UserHelper.get_user_data().json()['username']
        self.photo_id = UserHelper.get_list_photos_of_user(self.username).json()[0]['id']
        self.photo_data = {'photo_id': self.photo_id}
        CollectionHelper.add_photo_to_collection(collection_id=self.collection_id, data=self.photo_data)

        # set up variable to check UI
        email = DataHelper.read_json('../testdata/tc_check_create_and_add_photo_collection.json')['email']
        password = DataHelper.read_json('../testdata/tc_check_create_and_add_photo_collection.json')['password']
        self.driver = BrowserHelper.launch_chrome_browser()
        self.login_page = LoginPage(self.driver)
        self.collection_page = CollectionPage(self.driver)
        self.collections_list_page = CollectionListPage(self.driver)
        self.photo_page = PhotoPage(self.driver)

        # precondition: log in account
        self.login_page.navigate(URL['LOGIN_USER'])
        self.login_page.login(email, password)

    def test_add_random_photo_to_collection(self):
        # Navigate to Collection Page
        self.login_page.navigate(URL['VIEW_LIST_COLLECTION_OF_USER'].format(username=self.username))

        # Select a collection
        self.collections_list_page.click_on_collection(1)
        actual_collection_id = self.collection_page.get_current_url().split('/')[4]

        # Select a photo
        self.collection_page.click_photo_in_collection(1, 1)
        actual_photo_id = self.photo_page.get_current_url().split('/')[4]

        # Verify collection_id and photo_id
        assert_that(actual_collection_id, equal_to(str(self.collection_id)), 'Verify collection id')
        assert_that(actual_photo_id, equal_to(str(self.photo_id)), 'Verify photo id')

    def tearDown(self):
        self.driver.quit()
        # delete the collection
        CollectionHelper.delete_collection(self.collection_id)


if __name__ == "__main__":
    unittest.main()
