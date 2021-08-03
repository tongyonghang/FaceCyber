from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('register',views.register, name='register'),
    path('login',views.login, name='login'),
    path('main',views.main, name='main'),
    path('profile',views.profile, name='profile'),
    path('friend',views.friend, name='friend'),
    path('self',views.self, name='self'),
    path('logout',views.logout, name='logout'),
    url(r'^get_wiki_summary/$', views.get_wiki_summary, name='get_wiki_summary'),
    url(r'^get_scraper/$', views.get_scraper, name='get_scraper'),
]