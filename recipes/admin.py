from django.contrib import admin
from .models import Recipe, Ingredient

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description')
    inlines = [IngredientInline]

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'recipe', 'quantity', 'unit')
    list_filter = ('recipe',)
    search_fields = ('name', 'recipe__title')
