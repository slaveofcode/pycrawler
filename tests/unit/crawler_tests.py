import unittest, os, sys

current_dir = os.path.dirname(__file__)
base_dir = os.path.join(current_dir, os.pardir, os.pardir)
sys.path.append(base_dir)

from pycrawler.crawler import Crawler
from pycrawler.page import Page


class CrawlerTests(unittest.TestCase):

    def test_return_page_object_from_url(self):

        url = 'http://www.pasarpanda.com'

        c = Crawler.grab(url)

        self.assertIsInstance(c, Page)

    def test_return_page_object_from_file(self):

        c = Crawler.from_file('{base_dir}/tests/files/sample1.html'.format(base_dir=base_dir))

        self.assertIsInstance(c, Page)

    def test_return_page_object_from_string(self):

        f = open('{base_dir}/tests/files/sample1.html'.format(base_dir=base_dir), 'r')

        c = Crawler.from_text(f.read())

        f.close()

        self.assertIsInstance(c, Page)