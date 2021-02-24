from django.shortcuts import render


def account_page(request):
    context = {}
    return render(request, 'userprofiles/account_page.html', context)
