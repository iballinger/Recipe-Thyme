from django.forms import ModelForm
from .models import Review, Ingredient

class ReviewForm(ModelForm):
  class Meta:
    model = Review
    fields = ['score', 'content']

class IngredientForm(ModelForm):
  class Meta:
    model = Ingredient
    fields = ['portion', 'ingredient']