from django.urls import path,include
from django.contrib import admin
from . import views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


index_view = TemplateView.as_view(template_name="blog/login_index.html")


urlpatterns = [
    

    path('', views.IndexView.as_view(), name="index"),
    path('detail/<pk>/', views.Detail.as_view(), name="detail"),
    path('posts-list/', views.Index.as_view(), name = "posts-list"),
    path('create/', views.Create.as_view(), name="create"),
    path('update/<pk>', views.Update.as_view(), name="update"),
    path('delete/<pk>', views.Delete.as_view(), name="delete"), 
    path("login_index/", login_required(index_view), name="login_index"),#ログイン必須のページに飛ぶ
    path('', include("django.contrib.auth.urls")),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    

]
