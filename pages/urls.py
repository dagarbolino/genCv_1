from django.urls import path

from .views import InfoListView, InfoCreateView, home

app_name = "pages"

urlpatterns = [
    path('', home, name='home'),
    path('liste_cv/', InfoListView.as_view(), name='liste_cv'),
    path('create_cv/', InfoCreateView.as_view(), name='create_cv'),
    
]

