from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysqlTest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^display/$', 'sqlTest.views.display_request'),
    url(r'^search_form/$', 'sqlTest.views.search_form'),
    url(r'^search/$', 'sqlTest.views.search'),
    url(r'^search_result/$', 'sqlTest.views.search'),
    url(r'^contact_form/$', 'ContactUS.views.contact'),
    url(r'^contact/thanks/$', 'ContactUS.views.thanks'),
)
