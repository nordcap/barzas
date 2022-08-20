from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import get_template


# Create your views here.
def index(request):
    context = {}

    return render(request, 'staff/index.html', context)
    # return HttpResponse("You're looking at question")
