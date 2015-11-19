import requests
from http.client import OK


class HttpRequest:

    @classmethod
    def get(cls, url):

        response = requests.get(url)

        return response.text if response.status_code == OK else ''
