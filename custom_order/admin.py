from django.contrib import admin
from .models import CustomShieldOrder


@admin.register(CustomShieldOrder)
class CustomShieldOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'lord_name', 'shield_type', 'status', 'created_at', 'updated_at')
    search_fields = ('user__username', 'lord_name')
    list_filter = ('status', 'shield_type', 'user')
    list_editable = ('status',)