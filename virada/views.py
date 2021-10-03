from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def home(request):
	contents=Content.objects.all()

	try:
		logo=Picture.objects.get(title="logo")
	except:
		logo=""

	return render(request,'Virada/home.html',{'contents':contents,'logo':logo})

def orderPage(request):
	form=OrderForm
	try:
		logo=Picture.objects.get(title="logo")
	except:
		logo=""
	return render(request,'Virada/order.html',{'form':form,'logo':logo})