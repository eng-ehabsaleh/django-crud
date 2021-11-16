from django.shortcuts import render
from .models import Snack
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView )
# Create your views here.

class SnackListView(ListView):
    template_name='snack_list.html'
    model=Snack
    context_object_name='snack_list_object'
    
class SnackDetailView(DetailView):
    template_name='snack_detail.html'
    model=Snack
    context_object_name='snack-detail'
    
class SnackCreateView(CreateView):
    template_name='snack_create.html'
    model=Snack
    fields=['title','purchaser','description']        
    
class SnackUpdateView(UpdateView):
    template_name='snack_update.html'
    model=Snack
    fields=['title','description']    
    
class SnackDeleteView(DeleteView):
    template_name='snack_delete.html'
    model=Snack    