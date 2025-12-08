from django.urls import path
from . import views

urlpatterns = [
    # Recipe URLs
    path('', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/new/', views.recipe_create, name='recipe_create'),
    path('recipe/<int:pk>/edit/', views.recipe_update, name='recipe_update'),
    path('recipe/<int:pk>/delete/', views.recipe_delete, name='recipe_delete'),
    
    # Ingredient URLs
    path('recipe/<int:recipe_pk>/ingredient/new/', views.ingredient_add, name='ingredient_add'),
    path('recipe/<int:recipe_pk>/ingredient/<int:ingredient_pk>/edit/', views.ingredient_edit, name='ingredient_edit'),
    path('recipe/<int:recipe_pk>/ingredient/<int:ingredient_pk>/delete/', views.ingredient_delete, name='ingredient_delete'),
]
