import requests
import urllib2
from BeautifulSoup import BeautifulSoup

# TODO ---- Figure out how to crawl for query, and where to start crawling
# TODO ---- Connect to database
# TODO ---- Figure out what data needs to be stored for every crawled item


class Crawl:
    api_key = "44fe4958-51a9-48b2-acdd-7b8277b2ca83"
    api_test = 'test'
    base_url = 'http://content.guardianapis.com/search'
    current_page = 1
    crawled_information = {}
    section = ('football', 'sport')

    def __init__(self):
        print "Crawling initialised."

    def extract_article_paragraphs(self, web_url):
        print "crawl_article()"
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
                        print count, text
            print ""

        except urllib2.URLError:
            print "URLError encountered."

    def crawl_page(self, section, page_id, page_size):
        print "\ncrawl_page()"
        print "Page id: %d, Page size: %d" % (page_id, page_size)
        self.crawled_information.update()
        section_arg = '?section=' + section
        page_arg = '&page=' + str(page_id)
        page_size_arg = '&page-size=' + str(page_size)
        api_arg = "&api-key=" + self.api_test
        page_size_arg = '&page-size=' + str(page_size)
        api_arg = "&api-key=" + self.api_test
        crawl_url = self.base_url + section_arg + page_arg + page_size_arg + api_arg
        response = requests.get(crawl_url)
        dictionary = {}
        dictionary.update(response.json())
        print crawl_url, dictionary
        articles = dictionary['response']['results']
        article_count = 0
        for article in articles:
            article_count += 1
            article_web_url = article['webUrl']
            print article_count, article['apiUrl']
            self.extract_article_paragraphs(article_web_url)

    def crawl_all_pages(self, page_size):
        for section in self.section:
            print "\nSection:", section
            section_arg = '?section=' + section
            page_size_arg = '&page-size=' + str(page_size)
            api_arg = "&api-key=" + self.api_test
            crawl_url = self.base_url + section_arg + page_size_arg + api_arg
            print crawl_url
            response = requests.get(crawl_url)
            dictionary = {}
            dictionary.update(response.json())
            total_articles = int(dictionary['response']['total'])
            number_of_pages = int(dictionary['response']['pages'])
            #print dictionary
            print "Total number of articles:", total_articles
            print "Total number of pages:", number_of_pages
            for page in range(1, 2):
                self.crawl_page(section, page, page_size)


def main():
    crawl = Crawl()
    page_size = 50
    crawl.crawl_all_pages(page_size)

if __name__ == '__main__':
    main()