from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.views import View

from curriculum.forms import InfoForm

from curriculum.models import Info



def home(request):
    return render(request, "pages/home.html")


class HomeView(View):
    def get(self, request):
        form = InfoForm()
        return render(
            request,
            "pages/home.html",
            context={"form": form},
        )

    def post(self, request):
        form = InfoForm(request.POST)
        if form.is_valid():
            ...  # traiter
            return redirect("pages:home")
        return render(
            request,
            "pages/home.html",
            context={"form": form},
        )
        
        
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

    def post(self, request, pk):
        info = Info.objects.get(pk=pk)
        form = InfoForm(request.POST, instance=info)
        if form.is_valid():
            ...  # traiter
            return redirect("pages:home")
        return render(
            request,
            "pages/update_cv.html",
            context={"form": form},
        )
        
class InfoDeleteView(DeleteView):
    model = Info
    template_name = "pages/delete_cv.html"
    success_url = reverse_lazy("pages:home")
    
    def get(self, request, pk):
        info = Info.objects.get(pk=pk)
        return render(
            request,
            "pages/delete_cv.html",
            context={"info": info},
        )

    def post(self, request, pk):
        info = Info.objects.get(pk=pk)
        info.delete()
        return redirect("pages:home")
    
    