from django.contrib import admin
from .models import Activities, Bank, Owner

@admin.register(Activities)
class activitiesAdmin(admin.ModelAdmin):
    list_display = ('created', 'value', 'input', 'description', 'bank', 'owner', 'proof')

@admin.register(Bank)
class bankAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')

@admin.register(Owner)
class ownerAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')