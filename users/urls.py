from django.urls import path, include

from . import views

app_name = "users"

urlpatterns = [
    path('logout/', views.custom_logout_view, name='logout'),
    path("signup/", views.signup, name="signup"),
    path('', include('django.contrib.auth.urls')),
]