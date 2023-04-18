from django.db import models

# Create your models here
# .
class signup(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password=models.CharField(max_length=50)

class login(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

class login3(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class signup2(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)

class payment2(models.Model):
    cardholder_name=models.CharField(max_length=100)
    card_number = models.BigIntegerField()
    Expiry_date = models.CharField(max_length=10)
    cvv = models.CharField(max_length=10)
    checkbox = models.BooleanField(default=False)

class payment3(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    Address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code =models.BigIntegerField()
    cardnumber = models.BigIntegerField()
    Expiry_month = models.IntegerField()
    cvv = models.CharField(max_length=10)
    