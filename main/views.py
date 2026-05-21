from django.shortcuts import render
from .models import Article

def index(request):
    articles = Article.objects.all()[:5]  # Последние 5 статей
    context = {
        'articles': articles,
        'title': 'Главная | Городской портал'
    }
    return render(request, 'main/index.html', context)