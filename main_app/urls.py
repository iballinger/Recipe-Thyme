from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipes, name='recipes'),
    path('recipes/create/', views.RecipeCreate.as_view(), name='recipes_create'),
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipes_update'),
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipes_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('recipes/<int:pk>/', views.recipe_detail, name='detail'),
    path('recipes/<int:recipe_id>/add_photo/', views.add_photo, name='add_photo'),
    path('recipes/<int:recipe_id>/add_review/', views.add_review, name='add_review'),
    path('recipes/<int:recipe_id>/assoc_ingredient/<int:ingredient_id>/', views.assoc_ingredient, name='assoc_ingredient'),
    path('recipes/<int:recipe_id>/unassoc_ingredient/<int:ingredient_id>/', views.unassoc_ingredient, name='unassoc_ingredient'),
    path('ingredients/', views.IngredientList.as_view(), name='ingredients_index'),
    path('ingredients/<int:pk>/', views.IngredientDetail.as_view(), name='ingredients_detail'),
    path('ingredients/create/', views.IngredientCreate.as_view(), name='ingredients_create'),
    path('ingredients/<int:pk>/update/', views.IngredientUpdate.as_view(), name='ingredients_update'),
    path('ingredients/<int:pk>/delete/', views.IngredientDelete.as_view(), name='ingredients_delete'),
]