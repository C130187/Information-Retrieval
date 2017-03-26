from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from SearchEngine.Crawl.crawl import Crawl
from .forms import CrawlForm


def index(request):
    return render(request, 'SearchEngine/home.html')


def search(request):
    return render(request, 'SearchEngine/search.html')


# TODO -- This view must process the form and send data to crawl function,
# TODO -- get crawled information and return a template to display the crawled info
def get_crawl_keyword(request):
    if request.method == 'POST':
        crawl = Crawl()
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