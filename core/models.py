from django.db import models
import requests


# Create your models here.
class Customer(models.Model):

    female = "Female"
    male = "Male"

    gender_choice = [
        (female, 'Female'),
        (male, 'Male'),
    ]

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100, unique=True)
    gender = models.CharField(max_length=25,choices=gender_choice)
    company = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    title=  models.CharField(max_length=100)
    latitude = models.FloatField(max_length=100,blank=True,null=True)
    longitude = models.FloatField(max_length=100,blank=True,null=True)


    def __str__(self):
        return self.first_name

    def __repr__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = "Customer"