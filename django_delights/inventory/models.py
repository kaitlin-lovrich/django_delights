from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=200)
    unit_price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
        
class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
        
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.menu_item + ': ' + self.ingredient
        # try return self.menu_item + ': ' self.quantity + ' ' self.ingredient.unit + ' of ' + self.ingredient after we know the code works to make RecipeRequirement more readable
        
class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=200, blank=True)