from __future__ import print_function
from solrq import Q
import pysolr, json, urllib, urllib2
import os

# Setup a Solr instance. The timeout is optional.

solr = pysolr.Solr('http://localhost:8983/solr/newtest/', timeout=10)

def index():
    with open('../SearchEngine/Crawl/json_files/crawl_info_sport_1.json') as data_file:
        data = json.load(data_file)
        # print(data)
        # print(data['response']['results'])
        results = data['response']['results']

    keys_to_remove = ['apiUrl', 'isHosted', 'sectionId', 'sectionName']
    for result in results:
        for key, value in result.items():
            if key in keys_to_remove:
                del result[key]
    print(results)
    solr.add(results)
    #smart_search('weaks')




def smart_search(query):
    query_params = {'q': '"'+query+'"', 'wt':'json'}
    url = 'http://localhost:8983/solr/newtest/select?'
    url = url + urllib.urlencode(query_params)
    print(url)
    results = json.loads(urllib2.urlopen(url).read())
    #results = solr.search("'"+query+"'")
    print(results['response']['docs'])
    number = results['response']['numFound']
    # if (number == 0): #do spellcheck
    #     collations = results['spellcheck']['collations']
    #     collationqueries = []
    #     for c in collations:
    #         if(c!='collation'):
    #             print (c['collationQuery'])
    #             collationqueries.append(c['collationQuery'])
    #     print (collationqueries)
    #     if(len(collationqueries)==0):
    #         print("entered ~1")
    #         query_params = {'q': query+'~1', 'wt': 'json'}
    #         url = 'http://localhost:8983/solr/newtest/select?'
    #         url = url + urllib.urlencode(query_params)
    #         results = json.loads(urllib2.urlopen(url).read())
    #         number = results['response']['numFound']
    # print(results)
   # print(number)
   #  for doc in results['response']['docs']:
   #      print (doc['webTitle'])
   #      doc['webTitle'][0] = doc['webTitle'][0].encode("utf-8")
   #      print(type(doc['webTitle'][0]))
   #      print(type(doc['webTitle'][0]))
    #encoded_str = results.encode("utf8")
    return (number, results['response']['docs'])






def quick_search(query):
    query_params = {'q': query, 'wt': 'json'}
    url = 'http://localhost:8983/solr/newtest/select?'
    url = url + urllib.urlencode(query_params)
    results = json.loads(urllib2.urlopen(url).read())
    print(results)
    number = results['response']['numFound']
    print(number)
    return results

#quick_search('with weeks')
smart_search('with eight')

