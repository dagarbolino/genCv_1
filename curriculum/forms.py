from django import forms
from django.shortcuts import redirect, render, get_object_or_404
from curriculum.models import Info, Hobby, Skill, Language, Formation, Experience

from django.views.decorators.http import require_POST



class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ("title", "lastname", "firstname", "email", "phone", "address", "city", "zip_code", "state", "motivation", "photo", 
                "hobbies", "formations", "experiences", "skills", "languages", "is_active")

    def create_cv_view(request):
        if request.method == 'POST':
            form = InfoForm(request.POST, request.FILES)
            if form.is_valid():
                
                form.save()
                return redirect('pages:home')
        else:
            form = InfoForm()
        return render(request, 'create_cv.html', {'cv_form': form})
    

    def update_cv_view(request, pk):
        cv = Info.objects.get(pk=pk)
        form = InfoForm(request.POST or None, instance=cv)
        if form.is_valid():
            form.save()
            return redirect('pages:home')
        return render(request, 'update_cv.html', {'cv_form': form})
    
    
    def detail_cv_view(request, pk):
        cv = Info.objects.get(pk=pk)
        form = InfoForm(request.POST or None, instance=cv)
        if form.is_valid():
            form.save()
            return redirect('pages:home')
        return render(request, 'detail_cv.html', {'cv_form': form})
    

    
    
class HobbyForm(forms.ModelForm):
    class Meta: 
        model = Hobby
        fields = ("title_hobby",)
    
    def create_hobby_view(request):
        if request.method == 'POST':
            form = HobbyForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('pages:home')
        else:
            form = HobbyForm()
        return render(request, 'hobbie_create.html', {'hobby_form': form})
    
    def update_hobby_view(request, pk):
        hobby = Hobby.objects.get(pk=pk)
        form = HobbyForm(request.POST or None, instance=hobby)
        if form.is_valid():
            form.save()
            return redirect('pages:home')
        return render(request, 'hobbie_update.html', {'hobby_form': form})
    
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ("title_Skill",)
    
    def create_skill_view(request):
        if request.method == 'POST':
            form = SkillForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('pages:home')
        else:
            form = SkillForm()
        return render(request, 'skill_create.html', {'skill_form': form})
    
    def update_skill_view(request, pk):
        skill = Skill.objects.get(pk=pk)
        form = SkillForm(request.POST or None, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('pages:home')
        return render(request, 'skill_update.html', {'skill_form': form})
    
    
class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ("title_language", "niveau_language")
    
    def create_language_view(request):
        if request.method == 'POST':
            form = LanguageForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('pages:home')
        else:
            form = LanguageForm()
        return render(request, 'language_create.html', {'language_form': form})
    
    def update_language_view(request, pk):
        language = Language.objects.get(pk=pk)
        form = LanguageForm(request.POST or None, instance=language)
        if form.is_valid():
            form.save()
            return redirect('pages:home')
        return render(request, 'language_update.html', {'language_form': form})
    
    
class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ("title_formation", "date_formation", "location_formation", "description_formation")
    
    def create_formation_view(request):
        if request.method == 'POST':
            form = FormationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('pages:home')
        else:
            form = FormationForm()
        return render(request, 'formation_create.html', {'formation_form': form})
    
    def update_formation_view(request, pk):
        formation = Formation.objects.get(pk=pk)
        form = FormationForm(request.POST or None, instance=formation)
        if form.is_valid():
            form.save()
            return redirect('pages:home')
        return render(request, 'formation_update.html', {'formation_form': form})    
    
    
class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ("title_experience", "date_experience", "location_experience", "description_experience")
    
    def create_experience_view(request):
        if request.method == 'POST':
            form = ExperienceForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('pages:home')
        else:
            form = ExperienceForm()
        return render(request, 'experience_create.html', {'experience_form': form})
    
    def update_experience_view(request, pk):
        experience = Experience.objects.get(pk=pk)
        form = ExperienceForm(request.POST or None, instance=experience)
        if form.is_valid():
            form.save()
            return redirect('pages:home')
        return render(request, 'experience_update.html', {'experience_form': form})    