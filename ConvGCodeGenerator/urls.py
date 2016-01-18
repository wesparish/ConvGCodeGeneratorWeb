
from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^contact/$', views.contact_us, name='contact_us'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/cg2'}, name='auth_logout'),
    url(r'^logout/(?P<next_page>.*)/$', 'django.contrib.auth.views.logout', name='auth_logout_next'),
    url('^', include('django.contrib.auth.urls')),  
    url(r'^$', views.index, name='index'),
]
