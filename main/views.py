from django.shortcuts import render, redirect
from catalog.models import GuildProduct, Category
from .models import AboutInfo
from .forms import FeedbackForm


# Create your views here.
def main_index(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_index')
    else:
        form = FeedbackForm()

    special_products = GuildProduct.objects.filter(is_special=True).order_by('-id')[:4]
    categories = Category.objects.all()
    about_info = AboutInfo.objects.first()
    context = {
        'special_products': special_products,
        'categories': categories,
        'about_info': about_info,
        'form': form,
    }
    return render(request, 'home.html', context=context)