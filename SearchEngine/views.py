from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import CrawlForm, SearchForm
from SearchEngine.Crawl.crawl import Crawl
from SearchEngine.Main.search import smart_search, quick_search


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
    return render(request, 'SearchEngine/crawl.html', {'form': form})


def thanks(request):
    return HttpResponse(content="Thanks for submitting your query. Crawling in progress")


def get_search_keyword(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        # print "form:", form
        print "valid:", form.is_valid()
        if form.is_valid():
            if form.cleaned_data['search_query']:
                form_data = form.cleaned_data
                query_keyword = form_data['search_query']
                print "Keyword: ", query_keyword
                print "Searching by query:", query_keyword
                if 'quickSearch' in request.POST:
                    return send_search(request, query_keyword, 'quick_search')
                elif 'smartSearch' in request.POST:
                    return send_search(request, query_keyword, 'smart_search')
    else:
        form = SearchForm()
    return render(request, 'SearchEngine/home.html', {'form': form})


def send_search(request, query, search_type):
    results = ''
    num_results = 0
    # Setup a Solr instance. The timeout is optional.
    if search_type == 'quick_search':
        (num_results, results) = quick_search(query)
    elif search_type == 'smart_search':
        (num_results, results) = smart_search(query)

    result_list = []
    # Just loop over it to access the results.
    for result in results:
        result_list.append(result)
        print "The result is '{}'.".format(result)
        #print("The address is '{}'.".format(result["address"][0].encode("ascii")))
    return render(request, 'SearchEngine/search.html', {'query': query, 'resultlist': result_list,
                                                        'numResults': num_results})

