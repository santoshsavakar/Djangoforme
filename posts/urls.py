from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_create,
	post_detail,
	post_list,
	post_update,
	post_delete,
	)

urlpatterns = [
    url(r'^$', post_list),
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/$', post_detail),    
    url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),
    url(r'^delete/$', post_delete),


]
