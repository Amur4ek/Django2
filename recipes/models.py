from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    ingredients = models.JSONField()

    def __str__(self):
        return self.name
