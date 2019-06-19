from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^show/(?P<notification_id>\d+)/$', views.show_notification, name = 'notification'),
	url(r'^delete/(?P<notification_id>\d+)/$', views.delete_notification, name = 'notification'),
]
