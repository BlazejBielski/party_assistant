from django.contrib import admin

from dishes.models import Soup


class SoupAdminConfig(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'slug', 'created_at')
    search_fields = ('name',)
    list_filter = ('name', 'created_at', 'updated_at', 'is_vegetarian', 'is_keto', 'is_gluten_free', 'is_low_carb')


admin.site.register(Soup, SoupAdminConfig)
