from django import forms
from django.shortcuts import redirect, render, get_object_or_404
from curriculum.models import Info, Hobby

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