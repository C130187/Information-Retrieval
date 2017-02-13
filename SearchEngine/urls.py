from django.conf.urls import url
from . import views # period means importing from current package
app_name = 'SearchEngine'
urlpatterns = [
url(r'^$', views.index, name='index'),

]