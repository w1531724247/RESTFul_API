from crawler import Crawler
from HTTPRequest import HTTPRequest

httpRequest = HTTPRequest()
cww_crawler = Crawler()

def carSeriseWithBrandID(brandid='0'):
    return cww_crawler.cheWaWaCarSeriseList(brandid=brandid)