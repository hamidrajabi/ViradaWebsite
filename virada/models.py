from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.



class Content(models.Model):
	priority=models.IntegerField(null=True)
	title=models.CharField(max_length=200)
	image=models.ImageField()
	text=models.TextField()
	link_title=models.CharField(max_length=500,null=True,blank=True)
	link=models.CharField(max_length=500,null=True,blank=True)


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

class File(models.Model):
	title=models.CharField(max_length=200,null=True,blank=True)
	file=models.FileField()

	def fileURL(self):
		try:
			url=self.file.url
		except:
			url=''
		return url

	def __str__(self):
		return str(self.title)


class Customer(models.Model):
	name=models.CharField(max_length=200)
	phone_number = models.CharField(max_length=12)
	email=models.EmailField(null=True,blank=True)
	# address=models.ForeignKey(Address,on_delete=models.CASCADE,null=True,blank=True)


	def __str__(self):
		return str(self.name)

class Address(models.Model):
	customer=models.OneToOneField(Customer,on_delete=models.CASCADE,null=True,blank=True)
	city=models.CharField(max_length=200)
	state=models.CharField(max_length=200)

	def __str__(self):
		return str(self.city)+str(self.state)

class Order(models.Model):
	customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
	address=models.ForeignKey(Address,on_delete=models.CASCADE)
	date_added=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.customer)
		


