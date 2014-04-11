from django.conf.urls import patterns, include, url

from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TestDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   # url(r'^admin/', include(admin.site.urls)),
   url(r'^index/$', 'TestDjango.views.index'),
   url(r'^wikiIndex/$', 'wiki.views.wiki_index'),
   url(r'^manyToOne/$', 'wiki.views.manyToOne'),
)
