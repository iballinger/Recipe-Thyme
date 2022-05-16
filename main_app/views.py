from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe


@login_required
def recipes(request):
  recipes = Recipe.objects.all()
  return render(request, 'recipes/index.html', {'recipes': recipes})

class RecipeCreate(CreateView):
  model = Recipe
  fields = ['title', 'instructions', 'cuisine', 'category', 'prep_time', 'cook_time', 'difficulty']

  def form_valid(self, form): 
    form.instance.user = self.request.user
    return super().form_valid(form)

# Create your views here.
def home(request):
  return render(request, 'home.html')


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # Save the user to the db
      user = form.save()
      # Programmatically login
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


def recipe_detail(request, pk):
  recipe = Recipe.objects.get(id=pk)
  return render(request, 'recipes/detail.html', {'recipe': recipe}) 


def recipe_index(request):
  recipes = Recipe.objects.filter(user=request.user)
  return render(request, 'recipes/index.html', {'recipes': recipes})