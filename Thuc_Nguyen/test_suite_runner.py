# import your test modules
import unittest
from Thuc_Nguyen.testcase.check_create_and_add_photo_collection import CheckCreateAndAddPhoto
from Thuc_Nguyen.testcase.check_like_photo import CheckLikePhoto
from Thuc_Nguyen.testcase.check_remove_photo_collection import CheckRemovePhoto
from Thuc_Nguyen.testcase.check_photo_information import CheckCameraModelAndFocalLength
from Thuc_Nguyen.testcase.check_user_location import CheckUserLocation
from Thuc_Nguyen.testcase.check_user_full_name import CheckUserFullName


def TestSuite():
    """create test suite"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(CheckCreateAndAddPhoto))
    suite.addTests(loader.loadTestsFromTestCase(CheckRemovePhoto))
    suite.addTests(loader.loadTestsFromTestCase(CheckUserLocation))
    suite.addTests(loader.loadTestsFromTestCase(CheckLikePhoto))
    suite.addTests(loader.loadTestsFromTestCase(CheckCameraModelAndFocalLength))
    suite.addTests(loader.loadTestsFromTestCase(CheckUserFullName))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(TestSuite())
