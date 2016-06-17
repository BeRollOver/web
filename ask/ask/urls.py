from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'qa.views.test'),
    url(r'^login/$', 'qa.views.test'),
    url(r'^singup/$', 'qa.views.test'),
    url(r'^question/(\d+)$', 'qa.views.test'),
    url(r'^ask/.*$', 'qa.views.test'),
    url(r'^popular/$', 'qa.views.test'),
    url(r'^new/$', 'qa.views.tets'),
)
