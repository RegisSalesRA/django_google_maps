from django.db import models

# Create your models here.
class Customers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    title=  models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

class Boleto(models.Model):
    nome = models.CharField(max_length=100)
    due_date = models.DateField()      

    def __str__(self):
        return self.nome