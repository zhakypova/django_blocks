from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views import generic

from .models import Block, Apartment
from .forms import BlockForm, ApartmentForm


def block_list(request):
    blocks = Block.objects.all()
    context = {
        'blocks':blocks
    }
    return render(request, 'block_list.html', context)

def block_create(request):
    form = BlockForm()
    if request.method == 'POST':
        form = BlockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('block_list'))
    context = {
        'form':form
    }
    return render(request, 'block_form.html', context)

def block_detail(request,id):
    bloc = Block.objects.get(id=id)
    context = {
        'bloc':bloc
    }
    return render(request, 'block_detail.html', context)

def block_update(request, id):
    bloc = Block.objects.get(id=id)
    form = BlockForm(instance=bloc)
    if request.method == 'POST':
        form = BlockForm(request.POST, instance=bloc)
        if form.is_valid():
            form.save()
            return redirect(bloc.get_absolut_url())
    context = {
        'form':form
    }
    return render(request, 'block_form.html', context)

def block_delete(request, id):
    bloc = Block.objects.get(id=id)
    if request.method == 'POST':
        bloc.delete()
        return redirect(reverse_lazy('block_list'))
    context = {
        'bloc':bloc
    }
    return render(request, 'block_delete.html', context)


class ApartmentDetailView(generic.DetailView):
    model = Apartment
    template_name = 'apartment_detail.html'


class ApartmentListView(generic.ListView):
    model = Apartment
    template_name = 'apartment_list.html'
    context_object_name = 'apartments'

class ApartmentCreateView(generic.CreateView):
    model = Apartment
    form_class = ApartmentForm
    template_name = 'apartment_form.html'
    success_url = reverse_lazy('apartment_list')

class ApartmentUpdateView(generic.UpdateView):
    model = Apartment
    form_class = ApartmentForm
    template_name = 'apartment_form.html'

class ApartmentDeleteView(generic.DeleteView):
    model = Apartment
    template_name = 'apartment_delete.html'
    context_object_name = 'apartment'
    success_url = reverse_lazy('apartment_list')













