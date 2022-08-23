from django.shortcuts import render
from .models import Aboutus

# Create your views here.
def home(request):
    context = {'aboutus' : Aboutus.objects.first}
    return render(request, 'bansoft/index.html', context)
