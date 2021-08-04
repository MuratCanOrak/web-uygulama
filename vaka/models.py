from django.db import models
from .utility import random_code_generator

class Blog (models.Model):
    title = models.CharField(max_length=150)
    description =  models.TextField()
    link = models.CharField(max_length=250)
    email = models.EmailField( max_length=200)
    image = models.ImageField(upload_to="uploaded_images")
    code = models.CharField(null=True, unique=True, max_length=100)

    def save(self, *args, **kwargs):
       if self.code is None:
            c = random_code_generator()
            while Blog.objects.filter(code=c).exists():
                c = random_code_generator()
            self.code = c
       super(Blog, self).save(*args, **kwargs) 

    def __str__(self):
        return self.title
        