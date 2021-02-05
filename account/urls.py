from django.urls import path
from . import views


urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login_page, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_user, name='logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]