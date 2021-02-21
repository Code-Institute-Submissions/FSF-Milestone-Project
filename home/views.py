from django.shortcuts import render
from items.models import Item, Sale


def index(request):
    most_viewed = Item.objects.all()
    sales = Sale.objects.all()

    context = {
        'popular_items': most_viewed,
        'sales': sales,
    }

    return render(request, 'home/index.html', context)
