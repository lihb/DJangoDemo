from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CookiesAndSessions.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^register$', 'CAndS.views.register'),
	url(r'^login$', 'CAndS.views.login'),
	url(r'^index$', 'CAndS.views.index'),
	url(r'^logout$', 'CAndS.views.logout'),
)
