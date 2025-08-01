from django.contrib import admin
from django.urls import path
from .views import about_page, blog_detail_page, home_page, blogs_page

urlpatterns = [
    path('', home_page, name="home_page" ),
    path('about/', about_page, name="about_page"),
    path('blogs/', blogs_page, name="blogs_page"),
    # path('blogs/<int:pk>', blog_detail_page, name="blogs_detail_page")
]
