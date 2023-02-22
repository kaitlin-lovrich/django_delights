from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=200)
    unit_price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name