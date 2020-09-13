from Thuc_Nguyen.hook.api.constants import GET_USER_PROFILE_URL,GET_LIST_PHOTOS_OF_USER_URL
from Thuc_Nguyen.hook.api.request_helper import RequestHelper


class UserHelper:
    @staticmethod
    def get_user_data():
        return RequestHelper.send_get_request(GET_USER_PROFILE_URL)

    @staticmethod
    def update_user(data):
        return RequestHelper.send_put_request(GET_USER_PROFILE_URL, data)

    @staticmethod
    def get_list_photos_of_user(username):
        return RequestHelper.send_get_request(GET_LIST_PHOTOS_OF_USER_URL.format(username=username))

