from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from accounts.models import CustomUser
# Create your models here.

class Car(models.Model):
    car=models.CharField(max_length=255)
    owner=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    car_type=models.CharField(max_length=255)
    description=models.TextField(default='description')
    img_url=models.TextField(default='NO image available!')


    def __str__(self):
        return self.car
    
    def get_absolute_url(self):
        return reverse('car_detail', args=[self.id])