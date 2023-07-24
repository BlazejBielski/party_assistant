from django.contrib import admin

from . import models


class DishAdminConfig(admin.ModelAdmin):
    model = models.Soup
    list_display = ("id", "name", "price", "slug", "created_at")
    search_fields = ("name",)
    list_filter = ("name", "created_at", "updated_at", "is_vegetarian", "is_keto", "is_gluten_free", "is_low_carb")

    class Meta:
        abstract = True


class SoupAdminConfig(DishAdminConfig):
    pass


class MainDishAdminConfig(DishAdminConfig):
    pass


class AppetizerAdminConfig(DishAdminConfig):
    pass


class SideDishAdminConfig(DishAdminConfig):
    pass


admin.site.register(models.Soup, SoupAdminConfig)
admin.site.register(models.MainDish, MainDishAdminConfig)
admin.site.register(models.Appetizer, AppetizerAdminConfig)
admin.site.register(models.SideDish, SideDishAdminConfig)
