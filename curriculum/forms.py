from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render

from curriculum.models import Info


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
    


    
   