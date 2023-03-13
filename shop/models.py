from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=250)
    billing_address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)

    def __str__(self):
        return self.user.username

