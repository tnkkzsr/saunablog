from django.urls import path
from django.contrib import admin
from blog.views import IndexView, Index,Detail

urlpatterns = [
    
    path('', IndexView.as_view(), name="index"),
    path('detail/<pk>/', Detail.as_view(), name="detail"),
    path('posts-list/', Index.as_view(), name = "posts-list"),

]
