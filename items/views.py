from django.shortcuts import render
from .models import Item, Category
# Create your views here.


def search(request):

    items = Item.objects.all()
    categories = None
    if request.GET:
        if request.GET.get('category'):
            categories = request.GET['category']
            print(items)
            items = items.filter(category__internal_name__in=categories)  # this is filtering out correct items, why?
            print(items)
            categories = Category.objects.filter(internal_name__in=categories)
            print(categories)

    context = {
        'items': items,
        'category': categories,
    }

    return render(request, 'items/search.html', context)


def item_page(request):
    return render(request, 'items/item_page.html')
