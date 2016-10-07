"""project_movieratings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from movieratings.views import top_20_view, index_view, all_movies_view, all_raters_view, movie_info_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^top20/$', top_20_view, name='top_20_view'),
    url(r'^$', index_view),
    url(r'^allmovies/$', all_movies_view),
    url(r'^allraters/$', all_raters_view),
    url(r'^movie/(?P<movie_id>\d+)/$', movie_info_view),

]
