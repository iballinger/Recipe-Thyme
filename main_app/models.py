from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.



class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=25)
    category = models.CharField(max_length=25)
    allergens = models.CharField(max_length=25)
    servings = models.IntegerField()
    prep_time = models.CharField(max_length=25)
    cook_time = models.CharField(max_length=25)
    difficulty = models.IntegerField()
    instructions = models.TextField()

    def __str__(self):
         return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_color = models.CharField(max_length=50)

class Photo(models.Model):
    url = models.CharField(max_length=200)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for recipe_id: {self.recipe_id} @{self.url}"

class Ingredient(models.Model):
    portion = models.CharField(max_length=25)
    ingredient = models.CharField(max_length=50)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient

    def get_absolute_url(self):
        return reverse('ingredients_detail', kwargs={'pk': self.id})

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    content = models.CharField(max_length=500)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.recipe.id})
    

    def __str__(self):
        return f"{self.score}: {self.content}" 
    class Meta: 
        ordering = ['-score']

        
    