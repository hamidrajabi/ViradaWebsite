from django.shortcuts import render
from .models import *
from .forms import *
import ghasedak

sms = ghasedak.Ghasedak("ca3850956834bf4445dff3f9c6e08cba6b22b84d763814abcfb4488a1f35d0e0")
# Create your views here.



def home(request):
	# Author.objects.order_by('-score')
	contents=Content.objects.order_by('priority')

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
			sms.send({'message':'ویرادا: یک سفارش جدید ثبت گردید!', 'receptor' : '09153626468','linenumber': "10008566"})
			return render(request,'Virada/success-page.html')
		else:
			form=OrderForm()
	try:
		logo=Picture.objects.get(title="logo")
	except:
		logo=""
	try:
		order_header=Picture.objects.get(title="order_header")
		order_header_mobile=Picture.objects.get(title="order_header_mobile")
		favicon=Picture.objects.get(title="favicon")
	except:
		order_header=''
		order_header_mobile=''
		favicon=''

	return render(request,'Virada/order.html',{'form':form,'logo':logo,
		'order_header':order_header,
		'order_header_mobile':order_header_mobile,
		'favicon':favicon})

