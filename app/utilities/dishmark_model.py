from django.db import models


class DishMarkModel(models.Model):
    is_vegetarian = models.BooleanField(default=False, blank=True, null=True)
    is_gluten_free = models.BooleanField(default=False, blank=True, null=True)
    is_low_carb = models.BooleanField(default=False, blank=True, null=True)
    is_keto = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        abstract = True
