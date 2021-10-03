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
	form=OrderForm()
	if request.method=='POST':
		form=OrderForm(request.POST)
		if form.is_valid():
			print('its valid')
			customer=form.save()
			customer.save()

			# print('order',order.address)
			print('posts',request.POST.get('cityName'))
			address=Address.objects.create(customer=customer,city=request.POST.get('cityName'),state=request.POST.get('stateName'))
			address.save()

			order=Order.objects.create(customer=customer,address=address)
			order.address.city=request.POST.get('cityName')
			order.address.state=request.POST.get('stateName')
			order.save()
		else:
			form=OrderForm()
	try:
		logo=Picture.objects.get(title="logo")
	except:
		logo=""
	try:
		order_header=Picture.objects.get(title="order_header")
	except:
		order_header=''

	return render(request,'Virada/order.html',{'form':form,'logo':logo,'order_header':order_header})

