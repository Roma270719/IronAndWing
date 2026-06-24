from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from custom_order.models import CustomShieldOrder
from .models import SupplyOrder


@login_required(login_url='login')
def profile_view(request):
    shield_orders = CustomShieldOrder.objects.filter(user=request.user)
    supply_orders = SupplyOrder.objects.filter(user=request.user)
    context = {
        'shield_orders': shield_orders,
        'supply_orders': supply_orders,
    }
    return render(request, 'user_profile.html', context=context)