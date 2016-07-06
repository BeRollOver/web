from django.conf.urls import patterns, include, url

from django.contrib import admin
import qa.views
import ask.views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', qa.views.index, name='page'),
    url(r'^popular/$', qa.views.popular, name='popular'),
    url(r'^login/', ask.views.test),
    url(r'^signup/', ask.views.test),
    url(r'^question/', include('qa.urls')),
    url(r'^ask/', qa.views.ask, name='ask'),
    url(r'^answer/', qa.views.answer, name='answer'),
    url(r'^new/', ask.views.test),
)
