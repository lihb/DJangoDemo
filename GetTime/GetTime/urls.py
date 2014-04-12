from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GetTime.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^currentDate/$', 'Time.views.currentDate'),
	url(r'^Date/plus/(\d){1,2}$', 'Time.views.futureDate'),
)
