import pysolr
import json
import os

# Setup a Solr instance. The timeout is optional.
solr = pysolr.Solr('http://localhost:8983/solr/newtest/', timeout=10)


def get_file_to_index(file_name):
    with open(file_name) as data_file:
        data = json.load(data_file)
       # print data
       # print data['response']['results']
        results = data['response']['results']

    keys_to_remove = ['apiUrl', 'isHosted', 'sectionId', 'sectionName']
    for result in results:
        for key, value in result.items():
            if key in keys_to_remove:
                del result[key]
    print results
    solr.add(results)

    # results = solr.search('Arsenal')

    # print "Saw {0} result(s).".format(len(results))

    # Just loop over it to access the results.
    # for result in results:
    #    print "The result is '{}'.".format(result)
    #    print "The address is '{}'.".format(result["address"][0].encode("ascii"))