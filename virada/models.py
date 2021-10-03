from django.db import models

# Create your models here.

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
	

