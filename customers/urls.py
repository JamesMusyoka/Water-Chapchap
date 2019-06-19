from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('^$',views.home,name = 'home'),
    url(r'^signup', views.signup, name = 'signup'),
    url(r'order$', views.Customer_Create.as_view(), name='order_form'),
    url(r'^faqs/', views.faqs, name='faqs'),
] 

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
