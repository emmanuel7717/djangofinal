from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Recipe, Ingredient

# ==================== RECIPE VIEWS ====================

def recipe_list(request):
    """Display all recipes"""
    recipes = Recipe.objects.all().order_by('-created_at')
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, pk):
    """Display a single recipe with its ingredients"""
    recipe = get_object_or_404(Recipe, pk=pk)
    ingredients = recipe.ingredients.all()
    return render(request, 'recipes/recipe_detail.html', {
        'recipe': recipe,
        'ingredients': ingredients
    })

def recipe_create(request):
    """Create a new recipe"""
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        
        if title:
            recipe = Recipe.objects.create(
                title=title,
                description=description
            )
            return redirect('recipe_detail', pk=recipe.pk)
    
    return render(request, 'recipes/recipe_form.html', {'action': 'Create'})

def recipe_update(request, pk):
    """Update an existing recipe"""
    recipe = get_object_or_404(Recipe, pk=pk)
    
    if request.method == 'POST':
        recipe.title = request.POST.get('title', recipe.title)
        recipe.description = request.POST.get('description', recipe.description)
        recipe.save()
        return redirect('recipe_detail', pk=recipe.pk)
    
    return render(request, 'recipes/recipe_form.html', {
        'recipe': recipe,
        'action': 'Update'
    })

def recipe_delete(request, pk):
    """Delete a recipe"""
    recipe = get_object_or_404(Recipe, pk=pk)
    
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    
    return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': recipe})

# ==================== INGREDIENT VIEWS ====================

def ingredient_add(request, recipe_pk):
    """Add a new ingredient to a recipe"""
    recipe = get_object_or_404(Recipe, pk=recipe_pk)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        quantity = request.POST.get('quantity', '')
        unit = request.POST.get('unit', '')
        
        if name:
            Ingredient.objects.create(
                name=name,
                quantity=quantity,
                unit=unit,
                recipe=recipe
            )
            return redirect('recipe_detail', pk=recipe.pk)
    
    return render(request, 'recipes/ingredient_form.html', {
        'recipe': recipe,
        'action': 'Add'
    })

def ingredient_edit(request, recipe_pk, ingredient_pk):
    """Edit an existing ingredient"""
    recipe = get_object_or_404(Recipe, pk=recipe_pk)
    ingredient = get_object_or_404(Ingredient, pk=ingredient_pk, recipe=recipe)
    
    if request.method == 'POST':
        ingredient.name = request.POST.get('name', ingredient.name)
        ingredient.quantity = request.POST.get('quantity', ingredient.quantity)
        ingredient.unit = request.POST.get('unit', ingredient.unit)
        ingredient.save()
        return redirect('recipe_detail', pk=recipe.pk)
    
    return render(request, 'recipes/ingredient_form.html', {
        'recipe': recipe,
        'ingredient': ingredient,
        'action': 'Edit'
    })

def ingredient_delete(request, recipe_pk, ingredient_pk):
    """Delete an ingredient from a recipe"""
    recipe = get_object_or_404(Recipe, pk=recipe_pk)
    ingredient = get_object_or_404(Ingredient, pk=ingredient_pk, recipe=recipe)
    
    if request.method == 'POST':
        ingredient.delete()
        return redirect('recipe_detail', pk=recipe.pk)
    
    return render(request, 'recipes/ingredient_confirm_delete.html', {
        'recipe': recipe,
        'ingredient': ingredient
    })
