from django.shortcuts import render, redirect
from catalog.models import GuildProduct, Category
from .models import Feedback
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

    feed_back = Feedback.objects.first()
    special_products = GuildProduct.objects.filter(is_special=True).order_by('-id')[:4]
    categories = Category.objects.all()
    context = {
        'special_products': special_products,
        'categories': categories,
        'form': form,
        'feed_back': feed_back,
    }
    return render(request, 'home.html', context=context)