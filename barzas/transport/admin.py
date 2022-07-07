from django.contrib import admin

from .models import Point, Distance


# пункты загрузки-выгрузки
@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ('name',)


# дистанция между пунктами загрузки-выгрузки
@admin.register(Distance)
class DistanceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'point_start', 'point_final', 'distance')
    list_editable = ('point_start', 'point_final', 'distance',)
    list_filter = ('point_start', 'point_final',)
    ordering = ('point_start', 'point_final',)
    search_fields = ('point_start__name', 'point_final__name',)
    search_help_text = "Поиск по пунктам погрузки/разгрузки"
