from django.db import models
from datetime import date
#from django.core.validators import RegexValidator
#from datetime import date


class Register(models.Model):
    uname = models.CharField(max_length=15)
    pword = models.CharField(max_length=20)
    rights = models.CharField(max_length=25,default='User')

    def __str__(self):
        return self.uname+ "-"+ self.pword+ '-'+ self.rights

class Category(models.Model):
    addcategory = models.CharField(max_length=20)
    def __str__(self):
        return self.addcategory

class Addproduct(models.Model):
    productimg=models.ImageField(upload_to='images/')
    addcategory=models.CharField(max_length=15)
    productname=models.CharField(max_length=25)
    productprice=models.IntegerField()
    productquantity=models.IntegerField()

class tCart(models.Model):
    orderno=models.IntegerField()
    serialno=models.IntegerField()
    pid=models.IntegerField()
    pname=models.CharField(max_length=20)
    quantity=models.IntegerField()
    rate=models.IntegerField()
    total=models.IntegerField()
class sales(models.Model):
    salesno=models.IntegerField()
    sdate=models.DateField(default=date.today)
    custid=models.IntegerField()
    cname=models.CharField(max_length=25)
    total=models.IntegerField()
    cardno=models.IntegerField()
    expdate=models.CharField(max_length=20)
    ccv=models.IntegerField()
    carduser=models.CharField(max_length=25)
    status=models.CharField(max_length=20,default='o')
class salessub(models.Model):
    salesno=models.IntegerField()
    productid=models.IntegerField()
    pname=models.CharField(max_length=25)
    quantity=models.IntegerField()
    rate=models.IntegerField()
    total=models.IntegerField()
class address(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    staddress=models.CharField(max_length=100)
    town=models.CharField(max_length=25)
    state=models.CharField(max_length=20)
    pin=models.IntegerField()
    ph=models.IntegerField()
    email=models.EmailField(max_length=30)
