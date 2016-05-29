"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from book import views


urlpatterns = patterns('mysite.views',
                       # url(r'^$', my_homepage_view),
                       url(r'^hello/$', 'hello'),
                       url(r'^time/$', 'current_datetime'),
                       url(r'^another-time-page/$', 'current_datetime'),
                       url(r'^time/plus/(\d{1,2})/$', 'hours_ahead'),

)

urlpatterns += patterns('',
                        (r'^admin/', include(admin.site.urls)),
                        )

urlpatterns += patterns('article.views',
                  url(r'^article', 'get_article'),
)

urlpatterns += ('',
    # ...
    (r'^search/$', views.search),
    # ...
)

