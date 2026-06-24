from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, GuildProduct, BattleReview
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from user_profile.models import SupplyOrder
from .forms import CaravanOrderForm, BattleReviewForm

# Create your views here.
def catalog_index(request):
    categories = Category.objects.all()
    products = GuildProduct.objects.all()

    category_slug = request.GET.get('cat')
    if category_slug:
        products = products.filter(category__slug=category_slug)

    query = request.GET.get('search')
    if query:
        query = query.strip()
        words = query.split()

        for word in words:
            products = products.filter(
                Q(name__icontains=word) |
                Q(description__icontains=word) |
                Q(material_or_element__icontains=word)
            )

    context = {'categories': categories,
               'products': products,
               'search_query': query
               }
    return render(request, 'catalog.html', context=context)


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect(request.META.get('HTTP_REFERER', 'catalog_index'))


def product_detail(request, slug):
    product = get_object_or_404(GuildProduct, slug=slug)
    reviews = BattleReview.objects.filter(product=product)
    form = BattleReviewForm()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')

        form = BattleReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', slug=slug)
    context = {
        'product': product,
        'reviews': reviews,
        'form': form
    }
    return render(request, 'detail.html', context=context)

@login_required(login_url='/accounts/login/')
def checkout_view(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('catalog_index')

    if request.method == 'POST':
        form = CaravanOrderForm(request.POST)
        if form.is_valid():
            castle_address = form.cleaned_data['castle_address']
            for product_id, quantity in cart.items():
                try:
                    product = GuildProduct.objects.get(id=int(product_id))

                    SupplyOrder.objects.create(
                        user=request.user,
                        product=product,
                        quantity=quantity,
                        castle_address=castle_address,
                        status='PREPARING',
                    )

                    if product.stock >= quantity:
                        product.stock -= quantity
                        product.save()

                except GuildProduct.DoesNotExist:
                    continue

            request.session['cart'] = {}
            request.session.modified = True

            return redirect('profile')
    else:
        form = CaravanOrderForm()

    return render(request, 'checkout.html', {'form': form})