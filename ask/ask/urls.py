from django.conf.urls import patterns, include, url

from django.contrib import admin
import qa
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'qa.views.test'),
    url(r'^\?page=[0-9]+$', qa.views.index, name='page'),
    url(r'^popular/\?page=[0-9]+$', qa.views.popular, name='popular'),
    url(r'^login/', 'qa.views.test'),
    url(r'^signup/', 'qa.views.test'),
    url(r'^question/', include('qa.urls')),
    url(r'^ask/', 'qa.views.test'),
    url(r'^popular/', 'qa.views.test'),
    url(r'^new/', 'qa.views.test'),
)
