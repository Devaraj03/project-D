
from django.db import models

class Model(models.Model):

	# fields of the model
	name = models.CharField(max_length = 200,default="")
	age = models.IntegerField(default="")
	place= models.CharField(max_length=200,default="")

	def __str__(self):
		return self.name + " " + self.place
      
