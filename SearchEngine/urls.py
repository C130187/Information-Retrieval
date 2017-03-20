from django.conf.urls import url
from . import views # period means importing from current package
app_name = 'SearchEngine'
urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^search/', views.search, name='search'),
url(r'^crawl/', views.get_crawl_keyword, name='crawl'),
url(r'^thanks/', views.thanks, name='thanks')
]