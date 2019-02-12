from django.db import models
from django.urls import reverse
# Create your models here.
class Page(models.Model):
	title= models.CharField(max_length=40)
	conttent= models.TextField()
	last_update= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('detail', args=[str(self.id)])


 