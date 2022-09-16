from django.contrib import admin

from .models import Todo  # add this

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):  # add this
    list_display = ['title', 'description', 'completed'] # add this
