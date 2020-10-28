from django.contrib import admin

# Register your models here.
from .models import Post  #Here we're importing the Post Model
admin.site.register(Post) #Here, we're registering the Post Model
