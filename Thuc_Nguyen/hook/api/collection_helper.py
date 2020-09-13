from Thuc_Nguyen.hook.api.constants import ADD_PHOTO_TO_COLLECTION_URL, REMOVE_PHOTO_TO_COLLECTION_URL, \
    CREATE_COLLECTION_URL, REMOVE_COLLECTION_URL
from Thuc_Nguyen.hook.api.request_helper import RequestHelper


class CollectionHelper:
    @staticmethod
    def add_photo_to_collection(collection_id, data):
        return RequestHelper.send_post_request(ADD_PHOTO_TO_COLLECTION_URL.format(collection_id=collection_id), data)

    @staticmethod
    def remove_photo_from_collection(collection_id, data):
        return RequestHelper.send_delete_request(REMOVE_PHOTO_TO_COLLECTION_URL.format(collection_id=collection_id),
                                                 data)

    @staticmethod
    def create_collection(data):
        return RequestHelper.send_post_request(CREATE_COLLECTION_URL, data)

    @staticmethod
    def delete_collection(collection_id):
        return RequestHelper.send_delete_request(REMOVE_COLLECTION_URL.format(collection_id=collection_id))
