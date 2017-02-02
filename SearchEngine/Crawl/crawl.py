import json
import requests

class Crawl:
    api_key = "44fe4958-51a9-48b2-acdd-7b8277b2ca83"
    def __init__(self):
        print "Crawling initialised."

    def crawl_data(self):
        base_url = "http://content.guardianapis.com/search?"
        api_url = "api-key=" + self.api_key
        search_url = base_url + api_url
        response = requests.get(search_url)
        print response.status_code


def main():
    crawl = Crawl()
    crawl.crawl_data()

if __name__ == '__main__':
    main()
