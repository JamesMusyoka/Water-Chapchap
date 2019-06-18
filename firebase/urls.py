from django.contrib import admin
from django.conf.urls import url 
from . import views
urlpatterns = [
url(r'^signin/$',views.singIn),
url(r'^postsign/$',views.postsign),
]