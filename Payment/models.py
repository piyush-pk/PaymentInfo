from django.db import models
from django.forms import ChoiceField

# models start here.


class PaymentInfo(models.Model):

    payment_type = [
        ('DEBIT', 'DEBIT'),
        ('CREDIT', 'CREDIT'),

    ]

    username = models.CharField(max_length=150, blank=True)
    aadhar = models.CharField(max_length=12 , blank=True)
    mobile = models.CharField(max_length=10 , blank=True)
    address = models.CharField(max_length=250 , blank=True)
    payment = models.CharField(max_length=10 , blank=True)
    type = models.CharField(choices = payment_type, max_length=10, default = 'DEBIT') 
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class SimInfo(models.Model):

    sim = [
        ('JIO', 'JIO'),
        ('Airtel', 'Airtel'),
        ('VI', 'VI'),
        ('BSNL', 'BSNL'),

    ]
    name = models.CharField(max_length=150, blank=True)
    mobile = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=250, blank=True)
    company = models.CharField(choices = sim, max_length=10, default = 'JIO') 
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
