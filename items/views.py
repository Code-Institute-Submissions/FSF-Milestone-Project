from django.shortcuts import render, get_object_or_404
from .models import Item, Category
from userprofiles.models import Review
# Create your views here.


def search(request):
    # adapted from the django tutorials
    items = Item.objects.all()
    categories = None
    search = None
    if request.GET:
        if request.GET.get('category'):
            categories = request.GET['category'].split(',')
            items = items.filter(category__internal_name__in=categories)
            categories = Category.objects.filter(internal_name__in=categories)
        if request.GET.get('search'):
            search = request.GET['search']
            items = items.filter(name__icontains=search)
        if request.GET.get('sort'):
            items = items.order_by(request.GET['sort'])
    context = {
        'items': items,
        'search': search,
        'category': categories,
    }

    return render(request, 'items/search.html', context)


def item_page(request, item_ID):

    item = get_object_or_404(Item, pk=item_ID)
    reviews = Review.objects.filter(item=item)

    context = {
        'item': item,
        'reviews': reviews,
    }

    return render(request, 'items/item_page.html', context)
