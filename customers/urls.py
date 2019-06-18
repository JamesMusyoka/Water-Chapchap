from django.conf.urls import url
from . import views
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^signup', views.signup, name = 'signup'),
    url('^$',views.home,name = 'home'),
] 
=======
>>>>>>> origin/feature/homepage
