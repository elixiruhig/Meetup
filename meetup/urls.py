"""Meetup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

import meetup
from meetup import views
app_name = "meetup"
urlpatterns = [
    path('', views.homeview, name='homeview'),
    url(r'^group_details/(?P<group_id>[-\w]+)/$', views.group_details, name='group_details'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^user_logout/$', views.user_logout, name='user_logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^create_group/$', views.create_group_view, name='create_group_view'),
    url(r'^(?P<group_id_meetup>[-\w]+)/create_meetup/$', views.create_meetup_view, name='create_meetup_view'),
    url(r'^meetup=(?P<meetup_id>[-\w]+)/$', views.meetup_view, name='meetup_view'),
    url(r'^unsub=(?P<group_id>[-\w]+)/$', views.group_unsub_view, name='group_unsub_view'),
    url(r'^delete=(?P<group_id>[-\w]+)/$', views.group_delete_view, name='group_delete_view'),
    url(r'^profile=(?P<user_id>[-\w]+)/$', views.user_profile_view, name='user_profile_view'),
    url(r'^interest=(?P<interest>[-\w]+)/$', views.interest_view, name='interest_view'),


]
