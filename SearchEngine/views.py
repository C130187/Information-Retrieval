from django.core.urlresolvers import reverse
from solrq import Q
import pysolr, json
from django.shortcuts import redirect,render
from django.http import HttpResponse, HttpResponseRedirect
from SearchEngine.Crawl.crawl import Crawl
from .forms import CrawlForm, SearchForm


def index(request):
    return render(request, 'SearchEngine/home.html')


def search(request):
    return render(request, 'SearchEngine/search.html')


# TODO -- This view must process the form and send data to crawl function,
# TODO -- get crawled information and return a template to display the crawled info
def get_crawl_keyword(request):
    if request.method == 'POST':
        form = CrawlForm(request.POST)
        print "form:", form
        print "valid:", form.is_valid()
        if form.is_valid():
            if form.cleaned_data['query']:
                form_data = form.cleaned_data
                query_keyword = form_data['query']
                print "Keyword: ", query_keyword
                query_keyword = query_keyword.replace(" ", "%20")
                query_keyword = query_keyword.replace("&", "%26")
                query_keyword = query_keyword.replace("|", "%7C")
                crawl = Crawl()
                print "Crawling by query:", query_keyword
                crawl.crawl_dynamic([], query_keyword)
                return HttpResponseRedirect('/thanks')
    else:
        form = CrawlForm()
    return render(request, 'SearchEngine/crawl.html', {'form':form})


def thanks(request):
    return HttpResponse(content="Thanks for submitting your query. Crawling in progress")

def get_search_keyword(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        print "form:", form
        print "valid:", form.is_valid()
        if form.is_valid():
            if form.cleaned_data['searchquery']:
                form_data = form.cleaned_data
                query_keyword = form_data['searchquery']
                print "Keyword: ", query_keyword
                print "Searching by query:", query_keyword
                return send_search(request,query_keyword)
    else:
        form = SearchForm()
    return render(request, 'SearchEngine/home.html', {'form':form})

def send_search(request, query_keyword):
    # Setup a Solr instance. The timeout is optional.
    solr = pysolr.Solr('http://localhost:8983/solr/newtest/', timeout=10)

    results = solr.search(Q(name=query_keyword))

    resultlist = []

    print("Saw {0} result(s).".format(len(results)))

    # Just loop over it to access the results.
    for result in results:
        resultlist.append(result)
        print("The result is '{}'.".format(result))
        print("The address is '{}'.".format(result["address"][0].encode("ascii")))
    return render(request, 'SearchEngine/search.html',{'query_keyword':query_keyword,'resultlist':resultlist})