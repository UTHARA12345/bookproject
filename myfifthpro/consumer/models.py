from django.db import models

# Create your models here.
class Consumer(models.Model):
    c_name=models.CharField(max_length=125)
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    username=models.CharField(max_length=125,unique=True)
    password=models.CharField(max_length=125)
    def __str__(self):
        return self.username