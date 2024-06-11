from django.http import HttpResponse
import json

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def ingredients(request, dish):
    servings = int(request.GET.get('servings', 1))
    ingredients = DATA.get(dish, {})

    if servings > 1:
        ingredients = {key: value * servings for key, value in ingredients.items()}

    return HttpResponse(json.dumps(ingredients), content_type='application/json')

###
