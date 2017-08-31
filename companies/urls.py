from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from companies import views
from django.contrib import admin


urlpatterns = [
	url(r'^info/$', views.farmerinfo_list),
    url(r'^info/(?P<pk>[0-9]+)/$', views.farmerinfo_detail),
]