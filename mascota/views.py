from django.db.models.query import QuerySet
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Mascota
from .forms import MascotaForm

def home(request):
    return render(request, 'mascota/mascota_list.html')

@login_required
def mascota_create(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('mascota:lista_mascotas'))
    else:
        form = MascotaForm()
    return render(request, 'mascota/mascota_form.html', {'form': form})

@login_required
def mascota_list(request):
    nombre = request.GET.get('consulta', None)
    queryset = Mascota.objects.all()
    if nombre:
        queryset = queryset.filter(nombre__icontains=nombre)
    return render(request, 'mascota/mascota_list.html', {'mascotas': queryset})

@login_required
def mascota_detail(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    return render(request, 'mascota/detalle_mascota.html', {'mascota': mascota})

@login_required
def mascota_update(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES, instance=mascota)  
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('mascota:detalle_mascota', kwargs={'pk': mascota.pk}))
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'mascota/actualizar_mascota.html', {'form': form})
    
@login_required
def mascota_delete(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        mascota.delete()
        return redirect(reverse_lazy('mascota:lista_mascotas'))
    return render(request, 'mascota/mascota_confirm_delete.html', {'mascota': mascota})