from django.urls import path
from .views import InfoListView, InfoCreateView, home, InfoUpdateView, InfoDeleteView

app_name = "pages"

urlpatterns = [
    path('', home, name='home'),
    path('liste_cv/', InfoListView.as_view(), name='liste_cv'),
    path('create_cv/', InfoCreateView.as_view(), name='create_cv'),
    path('delete_cv/<int:pk>/', InfoDeleteView.as_view(), name='delete_cv'),  # Nom modifié ici
    path('update_cv/<int:pk>/', InfoUpdateView.as_view(), name='update_cv'),
]