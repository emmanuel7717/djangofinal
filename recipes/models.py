from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)  # NEW
    prep_time = models.IntegerField(blank=True, null=True, help_text="Prep time in minutes")  # NEW
    cook_time = models.IntegerField(blank=True, null=True, help_text="Cook time in minutes")  # NEW
    servings = models.IntegerField(blank=True, null=True, default=4)  # NEW
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    @property
    def total_time(self): 
        if self.prep_time and self.cook_time:
            return self.prep_time + self.cook_time
        return None

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    quantity = models.CharField(max_length=100, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    order = models.IntegerField(default=0) #ordering ingredients

    class Meta:  
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit})"