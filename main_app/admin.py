from django.contrib import admin
from .models import Recipe, Photo, Review
# Register your models here.
admin.site.register(Recipe)
admin.site.register(Photo)
admin.site.register(Review)