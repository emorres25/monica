from django.conf.urls import patterns, include, url
from django.contrib import admin
from main.views import monica
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'monica.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^facebook_auth/?$', monica.as_view()),
)
