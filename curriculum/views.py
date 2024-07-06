from django.shortcuts import render, redirect
from .forms import InfoForm

from curriculum.models import Info

def add_info(request, info_id):
    info = Info.objects.get(id=info_id)
    formset = InfoForm(instance=info)

    if request.method == 'POST':
        formset = InfoForm(request.POST, instance=info)
        if formset.is_valid():
            formset.save()
            return redirect('some_view_name')

    context = {'formset': formset}
    return render(request, 'add_formation.html', context)



def list_info(request):
    infos = Info.objects.all()
    context = {'infos': infos}
    return render(request, 'list_formation.html', context)