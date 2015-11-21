# Pycrawler
A Python crawler tool to grab page(s) information from their html data or web url. 
This library using python 3 and some dependencies with java runtime.  

# Installation

You can install this lib directly from github repository by execute 

    # Install from last stable release
    
    pip install git+ssh://git@github.com/slaveofcode/pycrawler@master
    
    # install by pip
    
    pip install pycrawler3

# How To Use?

First of all you must installed java runtime machine to get the boilerpipe works, because it's depends on java machine.

    from pycrawler.crawler import Crawler
    
    # returns page object
    
    page = Crawler.grab('http://www.pasarpanda.com')
    
    # Here you can execute or get the information of page object
    
    print(page.title)  # print the title of page
     
    print(page.images())  # get the image urls
    
    print(page.content)  # Print the extracted content
    
# Available Methods and Attributes

    # Grab from URL
    page = Crawler.grab('http://www.getscoop.com/berita/scoop-meluncurkan-fitur-baru-parental-control/')
    
    # Grab from file
    page = Crawler.from_file('/home/aditya/mydir/myhtml.html')
    
    # Grab from string
    page = Crawler.from_text('<html><head><title>My title yo</title></head><body>The content of my html</body></html>')
    
    # Page Object Methods and Properties
    
    page.title  # get the title of the page object
    >>> 'SCOOP Meluncurkan Fitur Baru Parental Control Untuk Mendukung Konten Edukasi dan Anak | SCOOP Berita'
    
    page.encoding  # get encoding of page
    >>> 'UTF-8'
    
    page.canonical_url  # get the canonical url
    >>> 'http://www.getscoop.com/berita/scoop-meluncurkan-fitur-baru-parental-control/'

    page.favicon  # get favicon icon as list
    >>> ['http://www.getscoop.com/berita/wp-content/themes/metro-pro/images/favicon.ico']
    
    page.language  # get language
    >>> 'en-US'
    
    page.metas  # get meta tags as list dictionary
    >>> [{'charset': 'UTF-8'}, {'name': 'description', 'content': 'SCOOP ingin meningkatkan aktivitas edukatif dan pengaruh positif bagi anak di dunia digital. Baca selengkapnya SCOOP Meluncurkan Fitur Baru Parental Control Untuk Mendukung Konten Edukasi dan Anak.'}, {'name': 'robots', 'content': 'noodp,noydir'}, ...]
    
    page.content  # get extracted content
    >>> 'SCOOP Meluncurkan Fitur Baru Parental Control Untuk Mendukung Konten Edukasi dan Anak\nNovember 18, 2015\nby Ita Istiqomah Leave a Comment\nSetelah sukses dengan fitur SCOOP Premium, kami kembali melakukan terobosan dan inovasi, salah satunya dengan merilis layanan terbaru "Parental Control” pada bulan November ini....'
    
    page.links  # get links
    >>> ['http://www.getscoop.com/berita/scoop-meluncurkan-fitur-baru-parental-control/#respond', 'http://www.getscoop.com/berita/category/entrepreneurship/', 'http://www.getscoop.com/berita/category/technology/', ...]
    
    page.original_links  # get original links that same as page url
    >>> ['http://www.getscoop.com/berita/2015/10/', 'http://www.getscoop.com/berita/tag/scoop/', 'http://www.getscoop.com/berita/barbie-girl-happy-sumpah-pemuda/#comment-101088', 'http://www.getscoop.com/berita/category/feature/', 'http://www.getscoop.com/berita/scoop-webstore/', ...]

    page.js_links  # get javascript links
    >>> ['http://www.getscoop.com/berita/af-custom/js/jquery-1.7.2.min.js', 'http://www.getscoop.com/berita/wp-includes/js/jquery/jquery.js?ver=1.11.3', 'http://www.getscoop.com/berita/wp-includes/js/jquery/jquery.color.min.js?ver=2.1.1', 'http://www.getscoop.com/berita/wp-content/themes/metro-pro/js/backstretch-set.js?ver=1.0.0', ...]

    page.css_links  # get css links
    >>> ['http://www.getscoop.com/berita/wp-content/plugins/wpfront-scroll-top/css/wpfront-scroll-top.css?ver=1.4.2', 'http://www.getscoop.com/berita/wp-content/plugins/ultimate-social-deux/public/assets/css/style.css?ver=3.1.6', '//fonts.googleapis.com/css?family=Oswald%3A400&ver=2.0.0', ...]
    
    page.resource_links  # get combined js & css links
    >>> ['http://www.getscoop.com/berita/af-custom/js/jquery-1.7.2.min.js', 'http://www.getscoop.com/berita/wp-includes/js/jquery/jquery.js?ver=1.11.3', 'http://www.getscoop.com/berita/wp-includes/js/jquery/jquery.color.min.js?ver=2.1.1', ...]
    
    page.images()  # get images
    >>> ['http://www.getscoop.com/berita/wp-content/uploads/2015/11/parental-control-scoop.jpg', 'http://kacang.apps-foundry.com/www/delivery/avw.php?zoneid=38&cb=INSERT_RANDOM_NUMBER_HERE&n=afd1f9fe', 'http://www.getscoop.com/berita/wp-content/plugins/wpfront-scroll-top/images/icons/1.png']
    
    page.html('article .entry-content')  # get html by css selector
    >>>  '<div class="entry-content" itemprop="text"><div class="us_posts_top" style="margin-top:0px;margin-bottom:0px;"><div class="us_wrapper tal"><div class="us_button us_share_text" data-text="Share this:"><span class="us_share_text_span"></span></div><div class="us_facebook us_button" data-text="SCOOP Meluncurkan Fitur Baru Parental Control ...'
    
    page.text('article .entry-content')  # get text by css selector
    >>> '  \nSetelah sukses dengan fitur SCOOP Premium, kami kembali melakukan terobosan dan inovasi, salah satunya dengan merilis layanan terbaru "Parental Control” pada bulan November ini.\nParental Control didukung dengan berbagai konten anak dan edukasi, dengan harapan SCOOP dapat meningkatkan aktivitas edukatif dan memberikan pengaruh positif bagi anak di dunia digital...'
    

## Run The Test

Run the test by using nosetests, make sure nosetest already installed, 
or you can run command `pip install nose` to install them

    >> nosetests
    
    >> ----------------------------------------------------------------------
    
    >> Ran 5 tests in 4.726s
    
    >> OK

    
    
