from bs4 import BeautifulSoup
from boilerpipe.extract import Extractor


class ContentExtractor:

    EXTRACTOR_DEFAULT = 'DefaultExtractor'
    EXTRACTOR_ARTICLE = 'ArticleExtractor'
    EXTRACTOR_ARTICLE_SENTENCES = 'ArticleSentencesExtractor'
    EXTRACTOR_KEEP_EVERTYHING = 'KeepEverythingExtractor'
    EXTRACTOR_KEEP_EVERTYHING_WITH_MIN_KWORDS = 'KeepEverythingWithMinKWordsExtractor'
    EXTRACTOR_LARGEST = 'LargestContentExtractor'
    EXTRACTOR_NUM_WORDS_RULES = 'NumWordsRulesExtractor'
    EXTRACTOR_CANOLA = 'CanolaExtractor'

    @staticmethod
    def extract(html, extractor_type):
        """Extract text content using several method from html

        :param html:
        :param extractor_type:
        :return:
        """
        return Extractor(extractor=extractor_type, html=html)


def extract_favicon(bs4):
    """Extracting favicon url from BeautifulSoup object

    :param bs4: `BeautifulSoup`
    :return: `list` List of favicon urls
    """

    favicon = []

    icon = bs4.select('link[rel="shortcut icon"]')

    if icon:

        if icon.has_attr('href'):

            favicon.append(icon['href'])

    icon = bs4.select('link[rel="icon"]')

    if icon:

        if icon.has_attr('href'):

            favicon.append(icon['href'])

    return favicon


def extract_metas(bs4):
    """Extracting meta tags from BeautifulSoup object

    :param bs4: `BeautifulSoup`
    :return: `list` List of meta tags
    """

    meta_tags = []

    metas = bs4.select('meta')

    for meta in metas:

        meta_content = {}

        if meta.has_attr('name'):
            meta_content.update({'name': meta['name']})

        if meta.has_attr('content'):
            meta_content.update({'content': meta['content']})

        if meta.has_attr('charset'):
            meta_content.update({'charset': meta['charset']})

        if meta.has_attr('http-equiv'):
            meta_content.update({'http-equiv': meta['http-equiv']})

        meta_tags.append(meta_content)

    return meta_tags


def extract_links(bs4):
    """Extracting links from BeautifulSoup object

    :param bs4: `BeautifulSoup`
    :return: `list` List of links
    """

    return [anchor['href'] for anchor in bs4.select('a[href]') if anchor.has_attr('href')]


def extract_original_links(base_url, bs4):
    """Extracting links that contains specific url from BeautifulSoup object

    :param base_url: `str` specific url that matched with the links
    :param bs4: `BeautifulSoup`
    :return: `list` List of links
    """

    return [anchor['href'] for anchor in bs4.select('a[href]')
            if anchor.has_attr('href')
            if anchor['href'].startswith(base_url)]


def extract_resource_links(bs4):
    """Extracting resource links such as .js and .css from BeautifulSoup object

    :param bs4: `BeautifulSoup`
    :return: `list` List of links
    """

    return [anchor['href'] for anchor in bs4.select('a[href]')
            if anchor.has_attr('href')
            if anchor['href'].endswith('.js') or anchor['href'].endswith['.css']]


def extract_css_links(bs4):
    """Extracting css links from BeautifulSoup object

    :param bs4: `BeautifulSoup`
    :return: `list` List of links
    """

    return [anchor['href'] for anchor in bs4.select('a[href]')
            if anchor.has_attr('href')
            if anchor['href'].endswith['.css']]


def extract_js_links(bs4):
    """Extracting js links from BeautifulSoup object

    :param bs4: `BeautifulSoup`
    :return: `list` List of links
    """

    return [anchor['href'] for anchor in bs4.select('a[href]')
            if anchor.has_attr('href')
            if anchor['href'].endswith['.js']]


def extract_images(bs4, lazy_image_attribute=None):
    """If lazy attribute is supplied, find image url on that attribute

    :param bs4:
    :param lazy_image_attribute:
    :return:
    """

    if lazy_image_attribute:
        return [image[lazy_image_attribute] for image in bs4.select('img') if image.has_attr[lazy_image_attribute]]
    else:
        return [image['src'] for image in bs4.select('img') if image.has_attr['src']]


class Page:

    def __init__(self, content, url=None):

        self.__url = url

        self.__original_content = content

        self.__bs4 = BeautifulSoup(content, 'html.parser')

        self._encoding = None

        self._title = None

        self._favicon = None

        self._language = None

        self._metas = None

        self._content = None

        self._links = None

        self._original_links = None

        self._resource_links = None

        self._js_links = None

        self._css_links = None

    @property
    def encoding(self):

        if not self._encoding:

            self._encoding = self.__bs4.original_encoding

        return self._encoding

    @property
    def title(self):

        if not self._title:

            self._title = self.__bs4.select('title')[0].get_text()

        return self._title

    @property
    def favicon(self):

        if not self._favicon:

            self._favicon = extract_favicon(self.__bs4)

        return self._favicon

    @property
    def language(self):

        if not self._language:

            result = self.__bs4.select('html')

            if result:

                if result[0].has_attr('lang'):

                    self._language = result[0]['lang']

        return self._language

    @property
    def metas(self):

        if not self._metas:

            self._metas = extract_metas(self.__bs4)

        return self._metas

    @property
    def content(self):

        if not self._content:

            self._content = ContentExtractor.extract(
                html=str(self.__bs4),
                extractor_type=ContentExtractor.EXTRACTOR_ARTICLE
            ).getText()

        return self._content

    @property
    def links(self):

        if not self._links:

            self._links = extract_links(self.__bs4)

        return self._links

    @property
    def original_links(self):

        if not self._original_links and self.__url:

            self._original_links = extract_original_links(self.__url, self.__bs4)

        return self._original_links

    @property
    def resource_links(self):

        if not self._resource_links:

            self._resource_links = extract_resource_links(self.__bs4)

        return self._resource_links

    @property
    def js_links(self):

        if not self._js_links:

            self._js_links = extract_js_links(self.__bs4)

        return self._js_links

    @property
    def css_links(self):

        if not self._css_links:

            self._css_links = extract_css_links(self.__bs4)

        return self._css_links

    def images(self, lazy_attr=None):
        """Get Images url

        :param lazy_attr: `str` set this if you wanna get custom img url attribute
        :return: `list` list of image urls
        """
        return extract_images(self.__bs4, lazy_image_attribute=lazy_attr)

    def html(self, selector):
        """Return html result that executed by given css selector

        :param selector: `str` css selector
        :return: `list` or `None`
        """

        result = self.__bs4.select(selector)

        return [str(r) for r in result] \
            if result.__len__() > 1 else \
            str(result[0]) if result.__len__() > 0 else None

    def text(self, selector):
        """Return text result that executed by given css selector

        :param selector: `str` css selector
        :return: `list` or `None`
        """

        result = self.__bs4.select(selector)

        return [r.get_text() for r in result] \
            if result.__len__() > 1 else \
            result[0].get_text() if result.__len__() > 0 else None

