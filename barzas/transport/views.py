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
            dict_trip = handle_upload_file(request.FILES['file'])
            # kwargs={'title': request.POST['title']}
            # url = reverse('transport:traffic')
            context = {
                'file': request.FILES['file'],
                'dict_trip': dict_trip
            }
            return render(request, 'transport/index.html', context)
    else:
        context = {
            'form_load': LoadDataForm()
        }
        return render(request, 'transport/index.html', context)



