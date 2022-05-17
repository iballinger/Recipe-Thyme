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
]