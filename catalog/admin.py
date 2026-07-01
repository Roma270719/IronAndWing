from django.contrib import admin, messages
from .models import Category, GuildProduct, BattleReview
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('name',)


@admin.register(GuildProduct)
class GuildProductAdmin(admin.ModelAdmin):
    list_display = ('photo_tag','category', 'name', 'price', 'stock', 'stock_change', 'material_or_element', 'is_special', 'discount_price')
    list_filter = ('category', 'is_special', 'material_or_element')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('stock', )
    fields = ('name', 'slug', 'category', 'price', 'description', 'image', 'material_or_element', 'stock', 'stock_change', 'is_special', 'discount_price')
    list_editable = ('category', 'name', 'price', 'stock_change', 'is_special', 'discount_price')

    def changelist_view(self, request, extra_context=None):
        if request.method == 'POST' and '_save' in request.POST:
            for key, value in request.POST.items():
                if '-stock_change' in key and value:
                    try:
                        parts = key.split('-')
                        parts[-1] = 'id'
                        id_key = '-'.join(parts)
                        product_id = request.POST.get(id_key)
                        if product_id:
                            product = GuildProduct.objects.get(pk=product_id)
                            change_val = int(value)
                            if change_val < 0 and (product.stock + change_val) < 0:
                                self.message_user(
                                    request,
                                    f"Not enough stock for '{product.name}'! Remaining: {product.stock}.",
                                    level=messages.ERROR
                                )
                                return HttpResponseRedirect(request.get_full_path())
                    except (ValueError, GuildProduct.DoesNotExist):
                        pass
        return super().changelist_view(request, extra_context)

    def photo_tag(self, obj):
        if obj.image:
            try:
                return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />')
            except ValueError:
                return "-"
        return "-"
    photo_tag.short_description = "Photo"


@admin.register(BattleReview)
class BattleReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('user__username', 'product__name', 'review')
    readonly_fields = ('created_at',)