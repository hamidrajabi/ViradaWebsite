from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
	contents=Content.objects.all()
	logo=Picture.objects.get(title='logo')
	return render(request,'Virada/home.html',{'contents':contents,'logo':logo})
