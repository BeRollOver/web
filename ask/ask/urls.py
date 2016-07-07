from django.conf.urls import patterns, include, url

from django.contrib import admin
from qa import views as qa_views
from ask import views as ask_views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', qa_views.index, name='page'),
    url(r'^popular/$', qa_views.popular, name='popular'),
    url(r'^login/', qa_views.login, name='login'),
    url(r'^signup/', qa_views.signup, name='signup'),
    url(r'^question/', include('qa.urls')),
    url(r'^ask/', qa_views.ask, name='ask'),
    url(r'^answer/', qa_views.answer, name='answer'),
    url(r'^new/', ask_views.test),
)
