from django.contrib import admin
from django.urls import path
from myapp.views import *
# register_page, login_page, home_page, see_more, logout_user, contact_page, about_page, admin_page, restaran

urlpatterns = [
    path('register/', register_page, name = 'register'),
    path('login/', login_page, name='login'),
    path('', home_page, name='home'),
    path('logout/', logout_user, name='logout'),
    path('contact/', contact_page, name='contact'),
    path('about/', about_page, name='about'),
    path('adminUser/', admin_page, name='admin'),
    path('restaran/<int:pk_test>/', restaran, name='restaran'),
    path('see-more/', see_more, name='see-more'),
    path('category/<str:cat_id>', category, name='category')

]