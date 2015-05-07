"""codekeeper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin


from codekeeper.views.home import HomePageView
from codekeeper.views.person import PersonList, PersonDetail
from codekeeper.views.snippet import SnippetList, SnippetDetail
from codekeeper.views.tag import TagList, TagDetail
from codekeeper.views.search import SearchView


urlpatterns = patterns('',


    url("^$", HomePageView.as_view(), name="home"),

    url('^snippets/$', SnippetList.as_view(), name="snippet-list"),
    url('^snippet/(?P<pk>[0-9]+)/$', SnippetDetail.as_view(), name="snippet-detail"),

    url('^people/$', PersonList.as_view(), name="person-list"),
    url('^person/(?P<pk>[0-9]+)/$', PersonDetail.as_view(), name="person-detail"),

    url('^tags/$', TagList.as_view(), name="tag-list"),
    url('^tag/(?P<pk>[0-9]+)/$', TagDetail.as_view(), name="tag-detail"),

    url('^admin/', include(admin.site.urls)),

    url(r'^search/$', SearchView.as_view(), name="search-view"),

    )