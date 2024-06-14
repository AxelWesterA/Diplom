from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories



def index(request):



    context = {
        'title' : 'BG - Главная',
        'content' : 'Магазин настольных игр BGame',


    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'О нас',
        'content': 'О нас',
        'text_on_page': 'Добро пожаловать в наш интернет-магазин настольных игр! Мы рады предложить вам увлекательный мир настольных развлечений, где каждая игра становится дверью в новые приключения, стратегические сражения и веселые вечера с друзьями и семьей.',

    }

    return render(request, 'main/about.html', context)
