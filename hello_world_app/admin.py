from django.contrib import admin
from hello_world_app.models import Name


class NameAdmin(admin.ModelAdmin):
    list_display = ('value', 'created_at', )
    search_fields = ('value',)

admin.site.register(Name, NameAdmin)
