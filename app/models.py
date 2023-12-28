from django.db import models
from django.contrib.auth.models import User

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Blogs/%Y/%m/%d')
    text = models.TextField()
    
    user = models.ForeignKey(
        to=User, 
        on_delete=models.CASCADE, 
        related_name='blogs',
        related_query_name='blogs')
    