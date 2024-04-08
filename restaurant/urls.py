"""
URL configuration for restaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    path('menu/', views.menu, name='menu'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('login/', views.login, name='login'),
    path('handle_login/', views.handle_login, name='handle_login'),
    path('signup/', views.signup, name='signup'),
    path('handle_signup/', views.handle_signup, name='handle_signup'),
    path('logout/', views.logout, name='logout'),
    path('handle_booking/', views.handle_booking, name='handle_booking'),
    path('my_booking/', views.my_booking, name='my_booking'),
    path('edit_booking/', views.edit_booking, name='edit_booking'),
    path('handle_edit_booking/', views.handle_edit_booking, name='handle_edit_booking'),
    path('delete_booking/', views.delete_booking, name='delete_booking'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)