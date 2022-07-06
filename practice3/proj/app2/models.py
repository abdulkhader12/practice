from django.db import models

class form_models(models.Model):
    username=models.CharField(max_length=100)
    rollno=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=100)
# Create your models here.
