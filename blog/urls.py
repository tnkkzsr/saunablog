from django.urls import path
from django.contrib import admin
from blog.views import IndexView,PostingView,PostslistView

urlpatterns = [
    
    path('', IndexView.as_view(), name="index"),
    path('post/', PostingView.as_view(), name = "post"),
    path('posts-list/', PostslistView.as_view(), name = "posts-list"),

]
