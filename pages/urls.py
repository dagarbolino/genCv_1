from django.urls import path


from .views import dashboard, InfoListView, InfoCreateView, home, generate_pdf, InfoUpdateView, InfoDetailView, InfoDeleteView, HobbiCreateView, SkillCreateView, SkillListView, LanguageCreateView, FormationCreateView, ExperienceCreateView, ExperienceListView, ExperienceDeleteView, SkillDeleteView, FormationListView, FormationDeleteView, LanguageListView, LanguageDeleteView, HobbiListView, HobbyDeleteView
app_name = "pages"

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('home/', home, name='home'),
    path('liste_cv/', InfoListView.as_view(), name='liste_cv'),
    path('create_cv/', InfoCreateView.as_view(), name='create_cv'),
    path('delete_cv/<int:pk>/', InfoDeleteView.as_view(), name='delete_cv'),  
    path('update_cv/<int:pk>/', InfoUpdateView.as_view(), name='update_cv'),
    path('detail_cv/<int:pk>/', InfoDetailView.as_view(), name='detail_cv'),
    
    path('hobbie_create/', HobbiCreateView.as_view(), name='hobbie_create'),
    path('hobbie_list/', HobbiListView.as_view(), name='hobbie_list'),
    path('hobbie_delete/<int:pk>/', HobbyDeleteView.as_view(), name='hobbie_delete'),
    #path('hobbie_update/<int:pk>/', HobbyUpdateView.as_view(), name='hobbie_update'),
    
    path('skill_create/', SkillCreateView.as_view(), name='skill_create'),
    path('skill_list/', SkillListView.as_view(), name='skill_list'),
    path('skill_delete/<int:pk>/', SkillDeleteView.as_view(), name='skill_delete'),
    #path('skill_update/<int:pk>/', SkillUpdateView.as_view(), name='skill_update'),
    
    path('language_create/', LanguageCreateView.as_view(), name='language_create'),
    path('language_list/', LanguageListView.as_view(), name='language_list'),
    path('language_delete/<int:pk>/', LanguageDeleteView.as_view(), name='language_delete'),
    #path('language_update/<int:pk>/', LanguageUpdateView.as_view(), name='language_update'),
    
    path('formation_create/', FormationCreateView.as_view(), name='formation_create'),
    path('formation_list/', FormationListView.as_view(), name='formation_list'),
    path('formation_delete/<int:pk>/', FormationDeleteView.as_view(), name='formation_delete'),
    #path('formation_update/<int:pk>/', FormationUpdateView.as_view(), name='formation_update'),
    
    path('experience_create/', ExperienceCreateView.as_view(), name='experience_create'),
    path('experience_list/', ExperienceListView.as_view(), name='experience_list'),
    path('experience_delete/<int:pk>/', ExperienceDeleteView.as_view(), name='experience_delete'),
    
    
    path('curriculum-pdf/<int:pk>/', generate_pdf, name='curriculum_pdf'),


]