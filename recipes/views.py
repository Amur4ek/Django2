from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Recipe


class RecipeView(View):
    def get(self, request, recipe):
        try:
            recipe_data = Recipe.objects.get(slug=recipe)
        except Recipe.DoesNotExist:
            return HttpResponse("Рецепт не найден")

        servings = request.GET.get('servings', 1)
        if not servings.isdigit() or int(servings) <= 0:
            servings = 1
        else:
            servings = int(servings)

        ingredients = {}
        for key, value in recipe_data.ingredients.items():
            ingredients[key] = value * servings

        return render(request, 'recipes/recipe.html', {'recipe': recipe_data, 'ingredients': ingredients})

