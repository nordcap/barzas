from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import LoadDataForm
from .lib import handle_upload_file


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = LoadDataForm(request.POST, request.FILES)
        if form.is_valid():
            # обработка загруженного файла
            dict_trip, dict_route, lst_distance = handle_upload_file(request.FILES['file'])
            # kwargs={'title': request.POST['title']}
            # url = reverse('transport:traffic')
            context = {
                'file': request.FILES['file'],
                'form_load': LoadDataForm(),
                'dict_trip': dict_trip,
                'dict_route': dict_route,
                'lst_distance': lst_distance,
            }

            return render(request, 'transport/index.html', context)
    else:
        context = {
            'form_load': LoadDataForm()
        }
        return render(request, 'transport/index.html', context)
