from django.shortcuts import render


def login(request):
    return render(request, 'login_page.html')


def signup(request):
    return render(request, 'signup_page.html')


def account_page(request):
    return render(request, 'account_page.html')
