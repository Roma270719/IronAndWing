from django.contrib import admin
from .models import AboutInfo, Feedback, Navbar


@admin.register(Navbar)
class NavbarAdmin(admin.ModelAdmin):
    list_display = ('name', 'main', 'catalog', 'info', 'custom')

@admin.register(AboutInfo)
class AboutInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'headline', 'text_preview', 'footer_one', 'phone', 'email', 'footer_text', 'footer_three', 'footer_work', 'footer_time')

    def text_preview(self, obj):
        return obj.text[:50] + "..." if len(obj.text) > 50 else obj.text
    text_preview.short_description = "Text Preview"

    def has_add_permission(self, request):
        if AboutInfo.objects.exists():
            return False
        return True


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'headline', 'name', 'email', 'is_processed', 'created_at', 'updated_at')
    list_filter = ('is_processed', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_editable = ('headline', 'is_processed',)
    readonly_fields = ('created_at', 'updated_at')