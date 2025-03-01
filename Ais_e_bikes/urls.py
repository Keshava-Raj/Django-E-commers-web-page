"""
URL configuration for Ais_e_bikes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Ais_e_bike_app import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact',views.contact1,name='contact'),
    path('',views.home ,name='home'),
    path('about Us',views.Aboutus ,name='about'),
    path('Signup',views.users_register ,name='register'),
    path('login',views.user_login ,name='userlogin'),
    path('Ride',views.dashboard ,name='dashboard'),
    path('user register',views.provider_register ,name='provider'),
    #path('provider signup',views.User_Register ,name='provider'),
    path('user sucssessfull login',views.provider_dashboard ,name='sucssessfulllogin'),
    path('user logout',views.logout_view ,name='logout'),
    path('providersignin', views.provider_Login , name = "ProviderLogin" ),
    path('textfile', views.providtexter_Login , name = "textfile" ),
    path('addvaickal', views.providtexter_addvaickal , name = "addvaickal" ),
    path('orderBoking', views.bookvaickel , name = "Bikebooking" ),
    path('order placed', views.ridersuccess , name = "orderbooked" ),
    
]

 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

