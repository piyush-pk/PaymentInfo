from django.db import models

# models start here.


class PaymentInfo(models.Model):
    username = models.CharField(max_length=150)
    aadhar = models.CharField(max_length=12)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=250)
    payment = models.CharField(max_length=10)
    time = models.DateTimeField(auto_now_add=True)

    def __str(self):
        return self.username
