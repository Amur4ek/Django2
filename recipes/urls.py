from django.urls import path
from .views import RecipeView

urlpatterns = [
    path('<slug:recipe>/', RecipeView.as_view(), name='recipe'),
]
