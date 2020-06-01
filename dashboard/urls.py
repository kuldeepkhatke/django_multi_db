from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^accounts/profile/$', views.dashboard, name="dashboard"),
    url(r'^delete/user/(?P<pk>\d+)/$', views.delete_user, name="dashboard"),
]
