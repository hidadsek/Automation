import requests
from Thuc_Nguyen.hook.api.constants import HEADER


class RequestHelper:

    @staticmethod
    def send_post_request(url, data=None):
        if data is None:
            data = {}
        return requests.post(url, headers=HEADER, data=data, verify=False)

    @staticmethod
    def send_put_request(url, data):
        return requests.put(url, headers=HEADER, data=data, verify=False)

    @staticmethod
    def send_delete_request(url, data=None):
        if data is None:
            data = {}
        return requests.delete(url, headers=HEADER, data=data, verify=False)

    @staticmethod
    def send_get_request(url):
        return requests.get(url, headers=HEADER, verify=False)
