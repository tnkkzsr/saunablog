from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    
    path('', views.IndexView.as_view(), name="index"),
    path('detail/<pk>/', views.Detail.as_view(), name="detail"),
    path('posts-list/', views.Index.as_view(), name = "posts-list"),
    path('create/', views.Create.as_view(), name="create"),
    path('update/<pk>', views.Update.as_view(), name="update"),
    path('delete/<pk>', views.Delete.as_view(), name="delete"),

]
