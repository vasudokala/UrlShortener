from django.conf.urls import patterns, include, url
 
urlpatterns = patterns('shortener.views',
    url(r'^$', 'index', name='home'),
    # for our home/index page
 
    url(r'^redirect/$', 'redirect_original', name='redirectoriginal'),
    # when short URL is requested it redirects to original URL
 
    url(r'^makeshort/$', 'shorten_url', name='shortenurl'),
    # this will create a URL's short id and return the short URL
    )