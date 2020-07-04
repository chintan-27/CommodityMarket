from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=100)
    DELIVERYBOY = 'DB'
    COURIERCOMPANY = 'CC'
    TRUCKDRIVERS = 'TD'
    USER_CHOICES = (
        (DELIVERYBOY,'Delivery boy'),
        (COURIERCOMPANY,'Courier company'),
        (TRUCKDRIVERS,'Truck Drivers'),
    )
    usertype = models.CharField(max_length = 2, choices = USER_CHOICES,default='')

    def __str__(self):
        return self.usertype

class Courier(models.Model):
    username_id = models.ForeignKey(User,on_delete=models.CASCADE)
    SUPERFAST = 'SF'
    NORMAL = 'NL'
    DELIVERY_CHOICES = (
        (SUPERFAST,'SUPERFAST'),
        (NORMAL,'NORMAL'),
    )
    usertype = models.CharField(max_length = 2, choices = DELIVERY_CHOICES,default='')
    deliverychargeperkg = models.FloatField()


    def __str__(self):
        return self.username_id.username

class TruckDrivers(models.Model):
    username_id = models.ForeignKey(User,on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    TRUCK_TYPE = (
        ('AC','AIR CONDITIONED'),
        ('NL','NORMAL'),
    )
    trucktype = models.CharField(max_length = 2, choices = TRUCK_TYPE,default='')
    STATUS_TYPE = (
    ('Available','Available'),
    ('Unavailable','Unavailable'),
    ('Busy','Busy'),
    )
    status = models.CharField(max_length=15,choices=STATUS_TYPE)
    def __str__(self):
        return self.username_id.username

class DeliveryBoy(models.Model):
    username_id = models.ForeignKey(User,on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    STATUS_TYPE = (
    ('Available','Available'),
    ('Unavailable','Unavailable'),
    ('Busy','Busy'),
    )
    status = models.CharField(max_length=15,choices=STATUS_TYPE)
    orders = models.IntegerField(default=0)

    def __str__(self):
        return self.username_id.username

class CourierOrder(models.Model):
    username = models.CharField(max_length=100)
    ordercode = models.CharField(max_length=200)
    city1 = models.CharField(max_length=100)
    city2 = models.CharField(max_length=100)
    date = models.DateField()
    STATUS_CHOICES = (
    ('PENDING','PENDING'),
    ('DELIVERED','DELIVERED'),
    )
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default="PENDING")

    def __str__(self):
        return self.ordercode

class DeliveryOrder(models.Model):
    username = models.CharField(max_length=100)
    ordercode = models.CharField(max_length=200)
    date = models.DateField()
    STATUS_CHOICES = (
    ('PENDING','PENDING'),
    ('DELIVERED','DELIVERED'),
    )
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default="PENDING")

    def __str__(self):
        return self.ordercode

class TruckOrder(models.Model):
    username = models.CharField(max_length=100)
    ordercode = models.CharField(max_length=200)
    city1 = models.CharField(max_length=100)
    city2 = models.CharField(max_length=100)
    date = models.DateField()
    STATUS_CHOICES = (
    ('PENDING','PENDING'),
    ('DELIVERED','DELIVERED'),
    )
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default="PENDING")

    def __str__(self):
        return self.ordercode
