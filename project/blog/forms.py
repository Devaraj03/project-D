from django import forms
from .models import *


# creating a form
class Modelform(forms.ModelForm):

	# create meta class
	class Meta:
		model = Model
		fields = [
			"name",
			"age",
			"place"
		]



