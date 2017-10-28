from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import logging
import datetime
import os




def start_search_spider(search_name):
    setting = get_project_settings()
    now = datetime.datetime.now()
    # setting.set('LOG_FILE', os.path.join(os.getcwd(), '../logs/search/') + now.strftime('%Y-%m-%d#%H-%M-%S') + '.log', priority='cmdline')
    process = CrawlerProcess(setting)
    process.crawl('search', name=search_name)
    process.start()


if __name__ == '__main__':
    start_search_spider('大主宰')
