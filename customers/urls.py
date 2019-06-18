from django.conf.urls import url
from . import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'order$', views.Customer_Create.as_view(), name='order_form'),
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 