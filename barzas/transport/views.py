from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'title': 'Модуль Транспорта'
    }
    return render(request, 'transport/index.html', context)

