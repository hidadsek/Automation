import unittest
from hamcrest import assert_that, equal_to
from Thuc_Nguyen.hook.api.collection_helper import CollectionHelper
from Thuc_Nguyen.hook.api.photo_helper import PhotoHelper
from Thuc_Nguyen.hook.data_helper import DataHelper
from Thuc_Nguyen.hook.browser_helper import BrowserHelper
from Thuc_Nguyen.hook.pageobjects.login_page import LoginPage
from Thuc_Nguyen.hook.pageobjects.collection_page import CollectionPage
from Thuc_Nguyen.hook.pageobjects.collection_list_page import CollectionListPage
from Thuc_Nguyen.hook.pageobjects.photo_page import PhotoPage
from Thuc_Nguyen.hook.pageobjects.constants import URL


class CheckRemovePhoto(unittest.TestCase):

    def setUp(self):

        # create a collection and add 2 random photos to created collection by API
        self.collection_title = DataHelper.read_json('../testdata/tc_check_create_and_add_photo_collection.json')[
            'test_collection_title']
        collection_data = {'title': self.collection_title}
        self.collection_id = CollectionHelper.create_collection(collection_data).json()['id']
        self.list_photos = []
        for i in range(2):
            photo_id = PhotoHelper.get_random_photo().json()['id']
            self.list_photos.append(photo_id)
            temp_photo_data = {'photo_id': photo_id}
            CollectionHelper.add_photo_to_collection(self.collection_id, temp_photo_data)
        photo_data = {'photo_id': self.list_photos[0]}
        CollectionHelper.remove_photo_from_collection(self.collection_id, photo_data)

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

    def test_remove_photo_from_collection(self):

        # Navigate to Collection Page
        self.login_page.navigate(
            URL['COLLECTION'].format(collection_id=self.collection_id, collection_title=self.collection_title))

        # Verify photo is removed
        list_href_photos = self.collection_page.get_list_href_photo_in_collection()
        has_photo = False
        for href_photo in list_href_photos:
            photo_id = href_photo.split('/')[4]
            if photo_id == self.list_photos[0]:
                has_photo = True
        assert_that(has_photo, equal_to(False), 'Verify photo is not in collection')

    def tearDown(self):
        self.driver.quit()
        # delete the collection
        CollectionHelper.delete_collection(self.collection_id)


if __name__ == "__main__":
    unittest.main()
