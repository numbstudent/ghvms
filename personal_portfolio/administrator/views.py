from django.shortcuts import render
from vendor import models as vm
# Create your views here.


def mainmenu(request):
    #data = vm.
    data = "<h1>ayam</h1>"
    return render(request, 'mainpage.html', {'hai': data})
