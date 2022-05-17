from nturl2path import url2pathname
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, Photo, Ingredient
import os
import uuid
import boto3
from .forms import ReviewForm, IngredientForm




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

class RecipeUpdate(LoginRequiredMixin, UpdateView):
  model = Recipe
  fields = ['title', 'instructions', 'cuisine', 'category', 'prep_time', 'cook_time', 'difficulty']

class RecipeDelete(LoginRequiredMixin, DeleteView):
  model = Recipe
  success_url = '/recipes/'

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

@login_required
def recipe_detail(request, pk):  
  recipe = Recipe.objects.get(id=pk)
  review_form = ReviewForm()
  ingredient_form = IngredientForm()
  return render(request, 'recipes/detail.html', {
    'recipe': recipe,
    'review_form': review_form,
    'ingredient_form': ingredient_form
  }) 


def recipe_index(request):
  recipes = Recipe.objects.filter(user=request.user)
  return render(request, 'recipes/index.html', {'recipes': recipes})

@login_required
def add_photo(request, recipe_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      Photo.objects.create(url=url, recipe_id=recipe_id)
    except Exception as e:
      print('An error occurred uploading file to S3')
      print(e)
  return redirect('detail', pk=recipe_id)

def add_review(request, recipe_id):
 
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.recipe_id = recipe_id
    new_review.save()
  return redirect('detail', pk=recipe_id)

def add_ingredient(request, recipe_id):
  form = IngredientForm(request.POST)
  if form.is_valid():
    new_ingredient = form.save(commit=False)
    new_ingredient.recipe_id = recipe_id
    new_ingredient.save()
  return redirect('detail', pk=recipe_id)

# def delete_ingredient(request, recipe_id, ingredient_id):
#   Ingredient.objects.filter(ingredient_id=ingredient_id).delete()
#   return redirect('detail', pk=recipe_id)
class IngredientDelete(LoginRequiredMixin, DeleteView):
  model = Ingredient
  success_url = '/recipes/'