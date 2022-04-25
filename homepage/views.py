from django.shortcuts import render

from django.http import HttpResponse


def index_page(request):
    return render(request, 'homepage/index.html')


def articles(request):
    return HttpResponse('<h1>Articles</h1>')
