from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import ToDo
# Create your views here.

def index(request):
    todos = ToDo.objects.all()
    return render(request, 'index.html', {'todos': todos})

class CreateTodo(CreateView):
    model = ToDo
    fields = '__all__'
    success_url = '/'