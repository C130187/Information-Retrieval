from django.conf.urls import url
from . import views # period means importing from current package
app_name = 'SearchEngine'
urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^home/', views.get_search_keyword, name='home'),
url(r'^search/', views.send_search, name='search'),
url(r'^crawl/', views.get_crawl_keyword, name='crawl'),
url(r'^thanks/', views.thanks, name='thanks')
]