from django.shortcuts import render, get_object_or_404
from .models import Item, Category
# Create your views here.


def search(request):
    # adapted from the django tutorials
    items = Item.objects.all()
    categories = None
    if request.GET:
        if request.GET.get('category'):
            categories = request.GET['category'].split(',')
            items = items.filter(category__internal_name__in=categories)
            categories = Category.objects.filter(internal_name__in=categories)

    context = {
        'items': items,
        'category': categories,
    }

    return render(request, 'items/search.html', context)


def item_page(request, item_ID):

    item = get_object_or_404(Item, pk=item_ID)

    context = {
        'item': item,
    }

    return render(request, 'items/item_page.html', context)
