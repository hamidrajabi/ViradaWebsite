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
	name=models.CharField(max_length=200)