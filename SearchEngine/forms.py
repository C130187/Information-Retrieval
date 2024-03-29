from django import forms


class CrawlForm(forms.Form):
    query = forms.CharField(label='Query keyword', max_length=100, required=False)
    '''
    OPTIONS = [ (0, 'Crawl by Categories'),
                (1, 'Crawl by Query'),
                (2, 'Crawl all') ]
    selection = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect())
    CATEGORIES = [(0, 'Football'),
                  (1, 'Sports')
                  ]
    crawlSelection = forms.MultipleChoiceField(CATEGORIES, False, forms.CheckboxSelectMultiple)
    '''


class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search', max_length=100, required=False)