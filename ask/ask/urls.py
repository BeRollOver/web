from django.conf.urls import patterns, include, url

from django.contrib import admin
import qa.views
import ask.views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', ask.views.test),
    url(r'^\?page=[0-9]+$', qa.views.index, name='page'),
    url(r'^popular/\?page=[0-9]+$', qa.views.popular, name='popular'),
    url(r'^login/', ask.views.test),
    url(r'^signup/', ask.views.test),
    url(r'^question/', include('qa.urls')),
    url(r'^ask/', ask.views.test),
    url(r'^popular/', ask.views.test),
    url(r'^new/', ask.views.test),
)
