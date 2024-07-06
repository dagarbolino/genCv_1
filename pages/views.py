from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
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