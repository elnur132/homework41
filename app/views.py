from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import PeopleForm
from .models import People
from django.views.generic import ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class ListPeople(ListView):
    model = People
    template_name = 'people.html'
    context_object_name = 'people'
    
class CreatePerson(SuccessMessageMixin, CreateView):
    model = People
    form_class = PeopleForm
    template_name = 'create_person.html'
    success_url = reverse_lazy('people')
    success_message = 'Данные добавлены успешно'