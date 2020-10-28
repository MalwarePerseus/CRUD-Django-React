from django.db import models

# Create your models here.
class Post(models.Model) :
	title = models.TextField(max_length =120, help_text='title of message.')
	message = models.TextField(help_text="Message Body")

	def __str__(self):
		return self.title