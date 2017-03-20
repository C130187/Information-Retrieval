from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CrawlForm

def index(request):
    return render(request, 'SearchEngine/home.html')


def search(request):
    return render(request, 'SearchEngine/search.html')


# TODO -- This view must process the form and send data to crawl function,
# TODO -- get crawled information and return a template to display the crawled info
def get_crawl_keyword(request):
    if request.method == 'POST':
        form = CrawlForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['query']
            print "Keyword: ", form.cleaned_data
            return HttpResponseRedirect('/thanks')
    else:
        form = CrawlForm()
    return render(request, 'SearchEngine/crawl.html', {'form':form})


def thanks(request):
    return HttpResponse(content="Thanks for submitting your query. Crawling in progress")