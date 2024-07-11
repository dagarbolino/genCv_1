from django.urls import path, include

from . import views


app_name = "users"

urlpatterns = [
    path('logout/', views.custom_logout_view, name='logout'),
    path("signup/", views.signup, name="signup"),
    path('login/', views.login_view, name='login'),
    path('user-info/', views.user_info_view, name='user_info'),
]