from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=300, null=False)
    prep_time = models.IntegerField(null=False)
    cook_time = models.IntegerField(null=False)
    total_time = models.IntegerField(null=False)
    image = models.CharField(max_length=300, null=True)
    yields = models.CharField(max_length=100, null=False)
    cuisine = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=100, null=False)

class RecipeIngredient(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=200, null=False)

class RecipeInstruction(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    step_no = models.IntegerField(null=False)
    instruction = models.CharField(max_length=10000, null=False)

class RecipeNutrition(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    nutrient = models.CharField(max_length=100, null=False)
    quantity = models.CharField(max_length=100)
