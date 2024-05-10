from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories



def index(request):

    categories = Categories.objects.all()

    context = {
        'title' : 'BG - Главная',
        'content' : 'Магазин настольных игр BGame',
        'categories': categories,

    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'О нас',
        'content': 'О нас',
        'text_on_page': 'о нас',

    }

    return render(request, 'main/about.html', context)
