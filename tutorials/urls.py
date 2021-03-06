"""tutorials URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from companies import views
#from tutorials.views import hello,print_date,hours_ahead

urlpatterns = [
#	url(r'^admin/', admin.site.urls),
#	url(r'^info/', views.farmerinfo_list.as_view()),
#   url(r'^hello/$',hello),
#   url(r'^printdate/$',print_date),
#   url(r'^printdate/plus/(\d{1,2})/$',hours_ahead),
#   url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^', include('companies.urls')),
]

#urlpatterns = format_suffix_patterns(urlpatterns)