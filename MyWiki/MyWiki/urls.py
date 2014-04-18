from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyWiki.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^blog/register$', 'Blog.views.register'),
	url(r'^blog/login$', 'Blog.views.login'),
	url(r'^blog/index$', 'Blog.views.index'),
	url(r'^blog/add$', 'Blog.views.add'),
	url(r'^blog/show$', 'Blog.views.show'),
	url(r'^blog/modify$', 'Blog.views.modify'),
	url(r'^blog/delete$', 'Blog.views.delete'),
)
