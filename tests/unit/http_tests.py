import unittest, os, sys

current_dir = os.path.dirname(__file__)
base_dir = os.path.join(current_dir, os.pardir, os.pardir)
sys.path.append(base_dir)

from requests.exceptions import ConnectionError
from pycrawler.http import HttpRequest


class HttpRequestTests(unittest.TestCase):

    def test_response_not_empty(self):
        url = 'http://www.pasarpanda.com'
        http = HttpRequest.get(url)
        self.assertIsNotNone(http)

    def test_raise_error(self):
        url = 'http://www.fake-url-that-not-exist-on-the-internet.com'
        with self.assertRaises(ConnectionError):
            HttpRequest.get(url)
