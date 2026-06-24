from django.contrib import admin
from .models import SupplyOrder


@admin.register(SupplyOrder)
class SupplyOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    list_editable = ('status', )
    readonly_fields = ('created_at', 'updated_at')