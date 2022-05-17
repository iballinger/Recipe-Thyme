from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.




class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    instructions = models.TextField()
    cuisine = models.CharField(max_length=25)
    category = models.CharField(max_length=25)
    prep_time = models.CharField(max_length=25)
    cook_time = models.CharField(max_length=25)
    difficulty = models.IntegerField()

    def __str__(self):
         return self.name

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
