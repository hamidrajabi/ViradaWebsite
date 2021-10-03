from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Customer(models.Model):
	name=models.CharField(max_length=200)
	phone_number = PhoneNumberField()
	email=models.EmailField(null=True,blank=True)

	def __str__(self):
		return str(self.name)

class Content(models.Model):
	priority=models.IntegerField(null=True)
	title=models.CharField(max_length=200)
	image=models.ImageField()
	text=models.TextField()

	def imageURL(self):
		try:
			url=self.image.url
		except:
			url=''
		return url

	def __str__(self):
		return str(self.title)

class Picture(models.Model):
	title=models.CharField(max_length=200,null=True,blank=True)
	image=models.ImageField()
	text=models.TextField(null=True,blank=True)

	def imageURL(self):
		try:
			url=self.image.url
		except:
			url=''
		return url

	def __str__(self):
		return str(self.title)

class order(models.Model):
	customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
	address=models.CharField(max_length=1000)
	date_added=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.customer)
		


