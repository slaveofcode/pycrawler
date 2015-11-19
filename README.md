# Pycrawler
A Python crawler tool to grab page(s) information from their html data or web url


# How To Use?

First of all you must installed java runtime machine to get the boilerpipe works, because it's depends on java machine.

    from pycrawl.crawler import Crawler
    
    page = Crawler.grab('http://www.pasarpanda.com')
    
    # Here you can execute or get the information of page object
    
    print(page.title)  # print the title of page
     
    print(page.images())  # get the image urls
    
    print(page.content)  # Print the extracted content
    
    
