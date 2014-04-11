from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ManytoMany.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^Many/show_author$', 'Many.views.show_author'),
    url(r'^Many/show_book$', 'Many.views.show_book'),
    url(r'^Many/register$', 'Many.views.register'),
    url(r'^Many/regist$', 'Many.views.regist'),
)
