from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.all_recipes, name='all_recipes'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]