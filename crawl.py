from decouple import config
from pymongo import MongoClient
from spider.spider import FacebookSpider

def start_crawl():
	conn = MongoClient('localhost', 27017)

	db = conn['facebook_reactions_database']

	timeline = db['timeline']

	facebook_email = config('FACEBOOK_EMAIL', default=False) 
	facebook_password = config('FACEBOOK_PASSWORD', default=False)

	spider = FacebookSpider(timeline)
	spider.login(facebook_email, facebook_password)
	spider.crawl()


if __name__ == '__main__':
	start_crawl()