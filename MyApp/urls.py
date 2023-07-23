from django.contrib import admin
from django.urls  import path 
from MyApp import views

# django admin text change manually
admin.site.site_header = "My Coffee Shop Admin"
admin.site.site_title = "My Coffee Shop Admin Portal"
admin.site.index_title = "Welcome to My Coffee Shop Portal"
# URL dispatcher
urlpatterns=[
    path('',views.index, name='home'),
    path('home',views.index, name='home'),
    path('about2', views.about, name='about2'), # we can also write as "about"
    path('menu',views.menu, name='menu'),
    path('contact',views.contact, name='contact')
] 