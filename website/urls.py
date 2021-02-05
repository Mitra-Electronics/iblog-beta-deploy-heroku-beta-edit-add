from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload-blog/', views.upload_blog, name='upload_blog'),
    path('video-detail/<slug:slug>/', views.details, name='blog_details'),
    path('edit-video/<slug:slug>/', views.edit_blog, name='edit_blog'),
]