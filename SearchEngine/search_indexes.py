from __future__ import print_function
from solrq import Q
import pysolr, json

# Setup a Solr instance. The timeout is optional.
solr = pysolr.Solr('http://localhost:8983/solr/newtest/', timeout=10)

with open('dummy.json') as data_file:
    data = json.load(data_file)
    print(data)

solr.add(data)

results = solr.search(Q(name="Solr"))

print("Saw {0} result(s).".format(len(results)))

# Just loop over it to access the results.
for result in results:
    print("The result is '{}'.".format(result))
    print("The address is '{}'.".format(result["address"][0].encode("ascii")))

