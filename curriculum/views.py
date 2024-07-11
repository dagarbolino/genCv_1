from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import InfoForm
from curriculum.models import Info

@login_required
def add_info(request, info_id):

    info = get_object_or_404(Info, id=info_id, user=request.user)
    formset = InfoForm(instance=info)

    if request.method == 'POST':
        formset = InfoForm(request.POST, instance=info)
        if formset.is_valid():
            formset.save()
            return redirect('some_view_name')

    context = {'formset': formset}
    return render(request, 'add_formation.html', context)

@login_required
def view_info(request, info_id):
    info = get_object_or_404(Info, id=info_id, user=request.user)

    context = {'info': info}
    return render(request, 'view_formation.html', context)



