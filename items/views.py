from django.shortcuts import render
from .models import Item, Category
# Create your views here.


def search(request):

    items = Item.objects.all()
    categories = None
    if request.GET:
        if request.GET.get('category'):
            categories = request.GET['category']
            items = items.filter(category__internal_name__in=categories)  # this is filtering out correct items as is the categories one.
            categories = Category.objects.filter(internal_name__in=categories)  # possible/probably misuse of objects.filter

    context = {
        'items': items,
        'category': categories,
    }

    return render(request, 'items/search.html', context)


def item_page(request):
    return render(request, 'items/item_page.html')
