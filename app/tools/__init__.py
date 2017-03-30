from crawler import Crawler

cww_crawler = Crawler()

def carSeriseWithBrandID(brandid='0'):
    return cww_crawler.cheWaWaCarSeriseList(brandid=brandid)