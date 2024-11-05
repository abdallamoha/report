from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.
def index(request):
    trips= models.Trip.objects.all()
    context={
        "trip":trips
    }
    return render(request,'report/index.html',context)




