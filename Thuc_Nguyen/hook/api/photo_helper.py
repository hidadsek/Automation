from Thuc_Nguyen.hook.api.constants import GET_PHOTO_URL, LIKE_PHOTO_URL, GET_RANDOM_PHOTO_URL, GET_USER_PHOTO_URL
from Thuc_Nguyen.hook.api.request_helper import RequestHelper


class PhotoHelper:

    @staticmethod
    def get_photo_data(photo_id):
        return RequestHelper.send_get_request(GET_PHOTO_URL.format(photo_id=photo_id))

    @staticmethod
    def like_photo(photo_id):
        return RequestHelper.send_post_request(LIKE_PHOTO_URL.format(photo_id=photo_id))

    @staticmethod
    def unlike_photo(photo_id):
        return RequestHelper.send_delete_request(LIKE_PHOTO_URL.format(photo_id=photo_id))

    @staticmethod
    def get_random_photo():
        return RequestHelper.send_get_request(GET_RANDOM_PHOTO_URL)

    @staticmethod
    def update_photo(photo_id, data):
        return RequestHelper.send_put_request(GET_PHOTO_URL.format(photo_id=photo_id), data)

    @staticmethod
    def get_photo_from_user(username):
        return RequestHelper.send_get_request(GET_USER_PHOTO_URL.format(username=username))
