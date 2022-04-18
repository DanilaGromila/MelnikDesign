from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField(max_length=200)
    issued = models.DateTimeField()
    admin = models.ForeignKey('Admins', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content


class Admins(models.Model):
    name = models.CharField(max_length=100, primary_key=True, blank=True)
    
    def __str__(self) -> str:
        return self.name


class CV(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(primary_key=True)
    image = models.ImageField(upload_to = 'uploads/')
# Create your models here.
