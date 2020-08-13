from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    gender = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    def __str__(self):
        return self.email

