import datetime
import json
import os
import requests
import time
import urllib2
from BeautifulSoup import BeautifulSoup

# TODO ---- Dump crawled data into json files per crawled page


class Crawl:
    api_key = "44fe4958-51a9-48b2-acdd-7b8277b2ca83"
    api_test = 'test'
    base_url = 'http://content.guardianapis.com/search'
    page_size = 10
    crawled_information = {}
    sections = ('sport', 'football')

    def __init__(self):
        print "Crawling initialised."

    def get_section_arg(self, section):
        if section in self.sections:
            return '?section=' + section
        else:
            return '?section=' + 'sport'

    def get_page_id_arg(self, page_id):
        return '&page=' + str(page_id)

    def get_api_key_arg(self):
        return "&api-key=" + self.api_test

    def get_query_arg(self, query):
        return "&q=" + query

    def extract_article_paragraphs(self, web_url):
        print "\nextract_article_paragraphs()"
        print "url:", web_url
        try:
            urlf = urllib2.urlopen(web_url)
            article_html = urlf.read()
            paragraph_start = int(article_html.find('<p>'))
            paragraph_end = int(article_html.rfind('</p>'))
            soup = BeautifulSoup(article_html[paragraph_start:paragraph_end + 4])
            invalid_tags = ['a', 'span', 'em', 'strong', 'strike']
            ignore_tags = ['br', 'time']
            # Replace tags with the text within them
            for tag in invalid_tags:
                for match in soup.findAll(tag):
                    match.replaceWithChildren()

            # Replace tags with ""
            for tag in ignore_tags:
                for match in soup.findAll(tag):
                    match.replaceWith("")

            soup = soup.findAll('p')
            count = 0
            paragraph_list = []
            for paragraph in soup:
                paragraph = str(paragraph)
                if '<p>' in paragraph:
                    text = paragraph.strip('<p>').strip('</p>')
                    # Do not add again if it already exists
                    if text not in paragraph_list:
                        count += 1
                        paragraph_list.append(text)
                        #print count, text
            #print " "
            return (paragraph_list)
        except urllib2.URLError:
            print "URLError encountered."

    def crawl_page(self, crawl_url, page_id):
        print "\ncrawl_page()"
        print "Page id:", page_id
        self.crawled_information.update()
        crawl_url += self.get_page_id_arg(page_id)
        print "Url: ", crawl_url
        response = requests.get(crawl_url)
        dictionary = {}
        dictionary.update(response.json())
        print crawl_url, dictionary
        articles = dictionary['response']['results']
        article_count = 0
        # TODO ---- This part needs to be modified to dump data for every crawled page
        file_path = os.getcwd() + "/JSON_files/crawled_sport" + str(1) + ".json"
        with open(file_path, 'w') as json_file:
            for article in articles:
                article_count += 1
                article_id = article['id']
                article_web_url = article['webUrl']
                print article_count, article['apiUrl'], article_id
                paragraphs = self.extract_article_paragraphs(article_web_url)
                print "Paragraphs for article:", len(paragraphs), ":", paragraphs
                json.dump(paragraphs, json_file)

    def crawl_by_section(self, section, page_id, query=None):
        print "crawl_by_section(), Query:", query
        print "Crawling section:", section
        crawl_url = self.base_url + self.get_section_arg(section) + self.get_api_key_arg()
        if query is not None:
            crawl_url += self.get_query_arg(query)
        print crawl_url
        response = requests.get(crawl_url)
        dictionary = {}
        dictionary.update(response.json())
        file = os.getcwd() + "/JSON_files/crawl_info.json"
        with open(file, 'w') as json_file:
            json.dump(response.json(), json_file)
        total_articles = int(dictionary['response']['total'])
        number_of_pages = int(dictionary['response']['pages'])
        # print dictionary
        print "Total number of articles:", total_articles
        print "Total number of pages:", number_of_pages
        for page in range(page_id, page_id+1):
            self.crawl_page(crawl_url, page)

    def crawl_all_sections(self, page_id, query=None):
        '''
        Case for the selection of crawling all sections or crawling by query
        :param query:
        :return: None
        '''

        # Crawls both 'Football' and 'Sport' sections
        if query is not None:
            for section in self.sections:
                self.crawl_by_section(section, page_id, query)
        # Crawls query in both 'Football' and 'Sport' sections
        else:
            for section in self.sections:
                self.crawl_by_section(section, page_id)

    def crawl_dynamic(self, section_list, query=None, page_id=1):
        print "crawl_dynamic()"
        if query is not None:
            self.crawl_all_sections(page_id, query=query)
        elif len(section_list) == 1:
            self.crawl_by_section(section_list[0], page_id)
        else:
            self.crawl_all_sections(page_id)

def main():
    crawl = Crawl()
    crawl.crawl_by_section(section='sport', page_id=1, query='federer')
    #crawl.crawl_query('Nadal')
    #query = 'Rafael'
    #print query
    #query=query.replace(" ", "%20")
    #print query

if __name__ == '__main__':
    main()
