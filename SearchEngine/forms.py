from django import forms


class CrawlForm(forms.Form):


    OPTIONS = [ (0, 'Crawl by Categories'),
                (1, 'Crawl by Query'),
                (2, 'Crawl all') ]
    selection = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect())
    CATEGORIES = [(0, 'Football'),
                  (1, 'Sports')
                  ]

    crawlSelection = forms.MultipleChoiceField(CATEGORIES, False, forms.CheckboxSelectMultiple)


class SearchForm(forms.Form):
    searchquery = forms.CharField(label='Search', max_length=100, required=False)

    query = forms.CharField(label='Query keyword', max_length=100, required=False)

    def __init__(self, data=None, *args, **kwargs):
        super(CrawlForm, self).__init__(data, *args, **kwargs)

