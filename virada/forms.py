from django import forms
from .models import *

class OrderForm(forms.ModelForm):
	class Meta:
		model=Customer
		fields='__all__'

		labels={
		'name':('نام و نام خانوادگی'),
		'email':('پست الکترونیک'),
		'phone_number':('شماره تلفن'),
		}
		widgets={
		'address':forms.HiddenInput(),
		}
		fields_required=['name','email','phone_number']