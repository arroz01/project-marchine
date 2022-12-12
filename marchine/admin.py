from django.contrib import admin

from .models import Marchine


# Register your models here.
class MarchineAdmin(admin.ModelAdmin):
    list_display = ('valor', 'acao', 'data_criacao')
    list_filter = ('acao', 'data_criacao')
    search_fields = ('acao', 'data_criacao')
    ordering = ('-data_criacao',)


admin.site.register(Marchine, MarchineAdmin)
