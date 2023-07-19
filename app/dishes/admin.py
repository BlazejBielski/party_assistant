from django.contrib import admin

from dishes.models import Soup


class SoupAdminConfig(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'slug')
    search_fields = ('name',)
    list_filter = ('name', 'created_at', 'updated_at')


admin.site.register(Soup)
