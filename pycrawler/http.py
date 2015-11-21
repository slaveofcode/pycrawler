import requests
from http.client import OK


class HttpRequest:

    @classmethod
    def get(cls, url):

        try:
            response = requests.get(url)
        except ConnectionError:
            return ''

        return response.text if response.status_code == OK else ''
