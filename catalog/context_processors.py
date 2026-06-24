from .models import GuildProduct

def cart_context(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0
    total_count = 0

    for product_id, quantity in cart.items():
        try:
            if not str(product_id).isdigit():
                continue

            product = GuildProduct.objects.get(id=int(product_id))
            item_total = product.price * quantity
            total_price += item_total
            total_count += quantity
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'item_total': item_total,
            })
        except (GuildProduct.DoesNotExist, Exception) as e:
            continue

    return {
        'cart_items': cart_items,
        'cart_total_price': total_price,
        'cart_total_count': total_count,
    }