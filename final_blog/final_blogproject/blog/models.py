from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    writer = models.TextField(max_length=100)
    title  = models.CharField(max_length=200)
    image  = models.ImageField(upload_to='images/', null=True, blank=True)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title
        
    def summary(self):
        return self.body[:20]

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content