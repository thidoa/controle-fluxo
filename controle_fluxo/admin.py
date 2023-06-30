from django.contrib import admin
from .models import activities

@admin.register(activities)
class activitiesAdmin(admin.ModelAdmin):
    list_display = ('value', 'input', 'description', 'bank', 'proof')
