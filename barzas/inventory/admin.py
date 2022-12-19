from django.contrib import admin

from .models import Location, Material


#
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('place',)
    list_display_links = ('place',)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('inv_number', 'name', 'count')
    list_editable = ('name', 'count')
    list_filter = ('name',)
    ordering = ('name',)
