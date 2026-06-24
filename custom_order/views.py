from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomShieldOrderForm

@login_required(login_url='/accounts/login/')
def custom_order_index(request):
    if request.method == 'POST':
        form = CustomShieldOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('profile')
    else:
        form = CustomShieldOrderForm()

    context = {
        'form': form
    }
    return render(request, 'custom_order.html', context=context)