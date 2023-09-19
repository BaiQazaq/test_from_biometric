from django.contrib import admin

# Register your models here.

from web_app.models import People

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'inn', 'age', 'created_at')
    list_filter = ('id',  'name', 'inn', 'age', 'created_at')
    search_fields = ('name', 'inn', 'age')
    fields = ('name', 'inn', 'age', 'created_at', 'changed_at')
    readonly_fields = ('id', 'created_at', 'changed_at')

admin.site.register(People, PeopleAdmin)