from django.shortcuts import render

# Create your views here.


def search(request):
    
    return render(request, 'items/itemlist.html')


def item_page(request):
    return render(request, 'items/itempage.html')
