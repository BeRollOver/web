from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', ask.views.test),
    url(r'^singup/', ask.views.test),
    url(r'^question/', include('qa.urls')),
    url(r'^ask/', ask.views.test),
    url(r'^popular/', ask.views.test),
    url(r'^new/', ask.views.test),
)
