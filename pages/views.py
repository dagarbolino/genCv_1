from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, render, redirect

from curriculum.forms import InfoForm, HobbyForm

from curriculum.models import Info, Hobby



def home(request):
    return render(request, "pages/home.html")


class InfoListView(ListView):
    model = Info
    template_name = "pages/list.html"
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
    success_url = reverse_lazy('pages:home')
    
class HobbyUpdateView(UpdateView):
    model = Hobby
    template_name = "pages/hobbie_update.html"
    form_class = HobbyForm

    def get_success_url(self):
        return reverse_lazy("pages:home")   
    
    def get(self, request, pk):
        hobby = Hobby.objects.get(pk=pk)
        form = HobbyForm(instance=hobby)
        return render(
            request,
            "pages/hobbie_update.html",
            context={"form": form},
        )    