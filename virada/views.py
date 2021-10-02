from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
	contents=Content.objects.all()

	return render(request,'Virada/home.html',{'contents':contents})
