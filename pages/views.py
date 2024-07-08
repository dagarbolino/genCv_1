from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import get_object_or_404, render, redirect

from curriculum.forms import InfoForm, HobbyForm, SkillForm, LanguageForm, FormationForm, ExperienceForm

from curriculum.models import Info, Hobby, Skill, Language, Formation, Experience



def home(request):
    return render(request, "pages/home.html")


class InfoListView(ListView):
    model = Info
    template_name = "pages/list.html"
    #template_name = "pages/detail_cv.html"
    
    context_object_name = "infos"
    
    def get_queryset(self):
        return Info.objects.all()

    def infoView(request):
        if request.method == "POST":
            form = InfoForm(request.POST)
            if form.is_valid():
                ...  # traiter
                return redirect("pages:home")
        else:
            form = InfoForm()
        return render(
            request,
            "pages/home.html",
            context={"form": form},
        )
    
class InfoCreateView(CreateView):
    model = Info
    form_class = InfoForm
    template_name = 'pages/create_cv.html'
    success_url = reverse_lazy('pages:home')
    
class InfoDetailView(DetailView):
    model = Info
    template_name = "pages/detail_cv.html"
    
    
    def get(self, request, pk):
        info = get_object_or_404(Info, pk=pk)
        return render(request, "pages/detail_cv.html", context={"info": info})
    
    

    
    

    
    
class InfoDeleteView(DeleteView):
    model = Info
    template_name = "pages/delete_cv.html"
    success_url = reverse_lazy("pages:home")
    
    def get(self, request, pk):
        info = get_object_or_404(Info, pk=pk)
        return render(request, "pages/delete_cv.html", context={"info": info})
    

class InfoUpdateView(UpdateView):
    model = Info
    template_name = "update_cv.html"
    form_class = InfoForm

    def get_success_url(self):
        return reverse_lazy("pages:home")   
    
    def get(self, request, pk):
        info = Info.objects.get(pk=pk)
        form = InfoForm(instance=info)
        return render(
            request,
            "pages/update_cv.html",
            context={"form": form},
        )

class HobbiCreateView(CreateView):
    model = Hobby
    form_class = HobbyForm
    template_name = 'pages/hobbie_create.html'
    success_url = reverse_lazy('pages:create_cv')
    
class HobbiListView(ListView):
    model = Hobby
    template_name = "pages/hobbie_list.html"
    context_object_name = "hobbies"
    
    def get_queryset(self):
        return Hobby.objects.all()
    
    def hobbieView(request):
        if request.method == "POST":
            form = HobbyForm(request.POST)
            if form.is_valid():
                ...  # traiter
                return redirect("pages:home")
        else:
            form = HobbyForm()
        return render(
            request,
            "pages/home.html",
            context={"form": form},
        )
        
class HobbyDeleteView(DeleteView):
    model = Hobby
    template_name = "pages/hobbie_delete.html"
    success_url = reverse_lazy("pages:home")
    
    def get(self, request, pk):
        hobby = get_object_or_404(Hobby, pk=pk)
        return render(request, "pages/hobbie_delete.html", context={"hobby": hobby})            
    


        
class SkillCreateView(CreateView):
    model = Skill
    form_class = SkillForm
    template_name = 'pages/skill_create.html'
    success_url = reverse_lazy('pages:home')
    
class SkillListView(ListView):
    model = Skill
    template_name = "pages/skill_list.html"
    context_object_name = "skills"
    
    def get_queryset(self):
        return Skill.objects.all()
    
    def skillView(request):
        if request.method == "POST":
            form = SkillForm(request.POST)
            if form.is_valid():
                ...  # traiter
                return redirect("pages:home")
        else:
            form = SkillForm()
        return render(
            request,
            "pages/home.html",
            context={"form": form},
        )    
    
class SkillDeleteView(DeleteView):
    model = Skill
    template_name = "pages/skill_delete.html"
    success_url = reverse_lazy("pages:home")
    
    def get(self, request, pk):
        skill = get_object_or_404(Skill, pk=pk)
        return render(request, "pages/skill_delete.html", context={"skill": skill})

        
class LanguageCreateView(CreateView):
    model = Language
    form_class = LanguageForm
    template_name = 'pages/language_create.html'
    success_url = reverse_lazy('pages:home')
    
class LanguageListView(ListView):
    model = Language
    template_name = "pages/language_list.html"
    context_object_name = "languages"
    
    def get_queryset(self):
        return Language.objects.all()
    
    def languageView(request):
        if request.method == "POST":
            form = LanguageForm(request.POST)
            if form.is_valid():
                ...  # traiter
                return redirect("pages:home")
        else:
            form = LanguageForm()
        return render(
            request,
            "pages/home.html",
            context={"form": form},
        )
        
class LanguageDeleteView(DeleteView):
    model = Language
    template_name = "pages/language_delete.html"
    success_url = reverse_lazy("pages:home")
    
    def get(self, request, pk):
        language = get_object_or_404(Language, pk=pk)
        return render(request, "pages/language_delete.html", context={"language": language})            
    
            
        
        
class FormationCreateView(CreateView):
    model = Formation
    form_class = FormationForm
    template_name = 'pages/formation_create.html'
    success_url = reverse_lazy('pages:home')
    
class FormationListView(ListView):
    model = Formation
    template_name = "pages/formation_list.html"
    context_object_name = "formations"
    
    def get_queryset(self):
        return Formation.objects.all()
    
    def formationView(request):
        if request.method == "POST":
            form = FormationForm(request.POST)
            if form.is_valid():
                ...  # traiter
                return redirect("pages:home")
        else:
            form = FormationForm()
        return render(
            request,
            "pages/home.html",
            context={"form": form},
        )   
        
        
class FormationDeleteView(DeleteView):
    model = Formation
    template_name = "pages/formation_delete.html"
    success_url = reverse_lazy("pages:home")
    
    def get(self, request, pk):
        formation = get_object_or_404(Formation, pk=pk)
        return render(request, "pages/formation_delete.html", context={"formation": formation})         
    

class ExperienceCreateView(CreateView):
    model = Experience
    form_class = ExperienceForm
    template_name = 'pages/experience_create.html'
    success_url = reverse_lazy('pages:home')
    
class ExperienceListView(ListView):
    model = Experience
    template_name = "pages/experience_list.html"
    context_object_name = "experiences"
    
    def get_queryset(self):
        return Experience.objects.all()
    
    def experienceView(request):
        if request.method == "POST":
            form = ExperienceForm(request.POST)
            if form.is_valid():
                ...  # traiter
                return redirect("pages:home")
        else:
            form = ExperienceForm()
        return render(
            request,
            "pages/home.html",
            context={"form": form},
        )
        
class ExperienceDeleteView(DeleteView):
    model = Experience
    template_name = "pages/experience_delete.html"
    success_url = reverse_lazy("pages:home")
    
    def get(self, request, pk):
        experience = get_object_or_404(Experience, pk=pk)
        return render(request, "pages/experience_delete.html", context={"experience": experience})            