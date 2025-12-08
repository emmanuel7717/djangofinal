from django.core.management.base import BaseCommand
from recipes.models import Recipe, Ingredient

class Command(BaseCommand):
    help = 'Populate the database with sample recipe data'

    def handle(self, *args, **options):
        # Clear existing data
        Recipe.objects.all().delete()
        
        # Sample recipes data
        recipes_data = [
            {
                'title': 'Classic Chocolate Chip Cookies',
                'description': 'Soft and chewy chocolate chip cookies perfect for any occasion. These cookies are made with butter, brown sugar, and plenty of chocolate chips.',
                'ingredients': [
                    {'name': 'All-purpose flour', 'quantity': '2.25', 'unit': 'cups'},
                    {'name': 'Baking soda', 'quantity': '1', 'unit': 'tsp'},
                    {'name': 'Sea salt', 'quantity': '1', 'unit': 'tsp'},
                    {'name': 'Butter', 'quantity': '1', 'unit': 'cup'},
                    {'name': 'Brown sugar', 'quantity': '0.75', 'unit': 'cups'},
                    {'name': 'Granulated sugar', 'quantity': '0.75', 'unit': 'cups'},
                    {'name': 'Vanilla extract', 'quantity': '1', 'unit': 'tsp'},
                    {'name': 'Eggs', 'quantity': '2', 'unit': ''},
                    {'name': 'Chocolate chips', 'quantity': '2', 'unit': 'cups'},
                ]
            },
            {
                'title': 'Spaghetti Carbonara',
                'description': 'An authentic Italian pasta dish made with eggs, guanciale (or pancetta), and pecorino cheese. Creamy, rich, and absolutely delicious.',
                'ingredients': [
                    {'name': 'Spaghetti', 'quantity': '1', 'unit': 'lb'},
                    {'name': 'Guanciale', 'quantity': '200', 'unit': 'g'},
                    {'name': 'Eggs', 'quantity': '4', 'unit': ''},
                    {'name': 'Pecorino Romano cheese', 'quantity': '1', 'unit': 'cup'},
                    {'name': 'Black pepper', 'quantity': '', 'unit': 'to taste'},
                    {'name': 'Salt', 'quantity': '', 'unit': 'to taste'},
                ]
            },
            {
                'title': 'Thai Green Curry',
                'description': 'A vibrant and aromatic Thai curry made with coconut milk, green chilies, and fresh basil. Perfect served with jasmine rice.',
                'ingredients': [
                    {'name': 'Coconut milk', 'quantity': '2', 'unit': 'cans'},
                    {'name': 'Green curry paste', 'quantity': '3', 'unit': 'tbsp'},
                    {'name': 'Chicken breast', 'quantity': '1.5', 'unit': 'lbs'},
                    {'name': 'Bell peppers', 'quantity': '2', 'unit': ''},
                    {'name': 'Thai basil', 'quantity': '1', 'unit': 'cup'},
                    {'name': 'Lime juice', 'quantity': '2', 'unit': 'tbsp'},
                    {'name': 'Fish sauce', 'quantity': '1', 'unit': 'tbsp'},
                    {'name': 'Garlic', 'quantity': '4', 'unit': 'cloves'},
                ]
            },
            {
                'title': 'Avocado Toast',
                'description': 'A simple yet satisfying breakfast or brunch dish. Creamy avocado spread on toasted bread with a squeeze of lemon.',
                'ingredients': [
                    {'name': 'Bread', 'quantity': '2', 'unit': 'slices'},
                    {'name': 'Avocado', 'quantity': '1', 'unit': ''},
                    {'name': 'Lemon', 'quantity': '0.5', 'unit': ''},
                    {'name': 'Sea salt', 'quantity': '', 'unit': 'to taste'},
                    {'name': 'Red pepper flakes', 'quantity': '', 'unit': 'to taste'},
                    {'name': 'Butter', 'quantity': '1', 'unit': 'tbsp'},
                ]
            },
            {
                'title': 'Homemade Pizza',
                'description': 'Make your own pizza with a perfectly crispy crust and your favorite toppings. Great for parties or family dinner.',
                'ingredients': [
                    {'name': 'Pizza dough', 'quantity': '1', 'unit': 'batch'},
                    {'name': 'Tomato sauce', 'quantity': '1', 'unit': 'cup'},
                    {'name': 'Mozzarella cheese', 'quantity': '2', 'unit': 'cups'},
                    {'name': 'Pepperoni', 'quantity': '1', 'unit': 'cup'},
                    {'name': 'Mushrooms', 'quantity': '1', 'unit': 'cup'},
                    {'name': 'Bell peppers', 'quantity': '1', 'unit': ''},
                    {'name': 'Olive oil', 'quantity': '2', 'unit': 'tbsp'},
                    {'name': 'Oregano', 'quantity': '1', 'unit': 'tsp'},
                ]
            },
        ]
        
        # Create recipes and ingredients
        created_count = 0
        for recipe_data in recipes_data:
            recipe = Recipe.objects.create(
                title=recipe_data['title'],
                description=recipe_data['description']
            )
            
            # Add ingredients to the recipe
            for ingredient_data in recipe_data['ingredients']:
                Ingredient.objects.create(
                    recipe=recipe,
                    name=ingredient_data['name'],
                    quantity=ingredient_data['quantity'],
                    unit=ingredient_data['unit']
                )
            
            created_count += 1
            self.stdout.write(self.style.SUCCESS(f'✓ Created recipe: {recipe.title}'))
        
        self.stdout.write(self.style.SUCCESS(f'\n✅ Successfully added {created_count} sample recipes!'))
