from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from .models import Recipe, Ingredient

# ==================== RECIPE VIEWS ====================

def recipe_list(request):
    """Display all recipes with search"""
    recipes = Recipe.objects.all().order_by('-created_at')
    
    # Add search functionality
    search_query = request.GET.get('q', '')
    if search_query:
        recipes = recipes.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(ingredients__name__icontains=search_query)
        ).distinct()
    
    return render(request, 'recipes/recipe_list.html', {
        'recipes': recipes,
        'search_query': search_query
    })

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
        instructions = request.POST.get('instructions', '')
        prep_time = request.POST.get('prep_time') or None
        cook_time = request.POST.get('cook_time') or None
        servings = request.POST.get('servings') or 4
        
        if title:
            recipe = Recipe.objects.create(
                title=title,
                description=description,
                instructions=instructions,
                prep_time=prep_time,
                cook_time=cook_time,
                servings=servings
            )
            return redirect('recipe_detail', pk=recipe.pk)
    
    return render(request, 'recipes/recipe_form.html')

def recipe_update(request, pk):
    """Update an existing recipe"""
    recipe = get_object_or_404(Recipe, pk=pk)
    
    if request.method == 'POST':
        recipe.title = request.POST.get('title', recipe.title)
        recipe.description = request.POST.get('description', recipe.description)
        recipe.instructions = request.POST.get('instructions', recipe.instructions)
        recipe.prep_time = request.POST.get('prep_time') or None
        recipe.cook_time = request.POST.get('cook_time') or None
        recipe.servings = request.POST.get('servings') or recipe.servings
        recipe.save()
        return redirect('recipe_detail', pk=recipe.pk)
    
    return render(request, 'recipes/recipe_form.html', {'recipe': recipe})

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
            # Get the highest order number and add 1
            max_order = recipe.ingredients.count()
            Ingredient.objects.create(
                name=name,
                quantity=quantity,
                unit=unit,
                recipe=recipe,
                order=max_order
            )
            return redirect('recipe_detail', pk=recipe.pk)
    
    return render(request, 'recipes/ingredient_form.html', {'recipe': recipe})

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
        'ingredient': ingredient
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