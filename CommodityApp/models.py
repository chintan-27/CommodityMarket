from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class UserType(models.Model):
    username = models.CharField(max_length=100)
    FARMER = 'FR'
    RETAIL_BUYER = 'RB'
    MANUFACTURER = 'MR'
    USER_CHOICES = (
        (FARMER,'Farmer'),
        (RETAIL_BUYER,'Retail buyer'),
        (MANUFACTURER,'Manufacturer'),
    )
    usertype = models.CharField(max_length = 2, choices = USER_CHOICES,default='FARMER')

    def __str__(self):
        return self.usertype

class Commodities(models.Model):
    username_id = models.ForeignKey(User, on_delete= models.CASCADE)
    name = models.CharField(max_length=200)
    comcode = models.CharField(max_length=100)
    type_choices = (
    ('FRUIT','Fruit'),
    ('VEGIES','Vegetables'),
    ('PULSES','Pulses'),
    ('CEREAL','Cereal'),
    ('OTHERS','Others')
    )
    type = models.CharField(max_length=100,choices=type_choices)
    perishable = models.BooleanField(default=False)
    description = models.CharField(max_length=1000)
    rating = models.FloatField(default=0.0)
    amount = models.FloatField()
    breed=models.CharField(max_length=200,default=' ')
    priceperkg = models.FloatField()
    priceperquintal = models.FloatField()
    date = models.DateField()
    time = models.TimeField(auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to = 'img/')

    def __str__(self):
        return self.name

class Farmer(models.Model):
    username_id = models.ForeignKey(User, on_delete= models.CASCADE)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.username_id.username

class Customer(models.Model):
    username_id = models.ForeignKey(User, on_delete= models.CASCADE)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.username_id.username

class Manufacturer(models.Model):
    username_id = models.ForeignKey(User, on_delete= models.CASCADE)
    company_name = models.CharField(max_length=300)
    company_add = models.CharField(max_length=300)
    licenceno = models.CharField(max_length=30)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length=100)
    def __str__(self):
        return self.company_name

class Requirement(models.Model):
    username_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.ForeignKey(Commodities,on_delete=models.CASCADE)
    reqcode = models.CharField(max_length = 10)
    amount = models.FloatField(validators=[MinValueValidator(100.0)])
    date = models.DateField()

    def __str__(self):
        return self.name + self.amount

class Order(models.Model):
    seller = models.CharField(max_length=100)
    buyer = models.CharField(max_length=100)
    amount = models.FloatField(default=0.0)
    ordercode = models.CharField(max_length=100,default="")
    breed=models.CharField(max_length=200,default=' ')
    name = models.CharField(max_length=200)
    type_choices = (
        ('FRUIT','Fruit'),
        ('VEGIES','Vegetables'),
        ('PULSES','Pulses'),
        ('CEREAL','Cereal'),
        ('OTHERS','Others')
    )
    type = models.CharField(max_length=100,choices=type_choices)
    comcode = models.CharField(max_length=100,default="")
    price = models.FloatField(default=0.0)
    RETAIL = 'RT'
    BULK = 'BL'
    ORDERTYPE_CHOICES = (
    (RETAIL,'Retail'),
    (BULK,'Bulk'),
    )
    bill = models.FloatField(default=0.0)
    tax = models.FloatField(default=0.0)
    deliveryprice = models.FloatField(default=0.0)
    total = models.FloatField(default=0.0)
    ordertype = models.CharField(max_length=2 ,choices=ORDERTYPE_CHOICES)
    couriername = models.CharField(max_length=100,default="")
    deliveryboy = models.CharField(max_length=100,default="")
    truckname = models.CharField(max_length=100,default="")
    orderstatus = models.CharField(max_length=20,choices=(
    ("Yet to be shipped",'Yet to be shipped'),
    ("On the way",'On the way'),
    ("Shipped",'Shipped'),
    ("Delivered",'Delivered'),
    ),default="")
    expecteddate = models.DateField(auto_now=True)

    def __str__(self):
        return self.buyer

class Cart(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    comcode = models.CharField(max_length=100)
    breed=models.CharField(max_length=200,default=' ')
    weight = models.FloatField()
    type_choices = (
        ('FRUIT','Fruit'),
        ('VEGIES','Vegetables'),
        ('PULSES','Pulses'),
        ('CEREAL','Cereal'),
        ('OTHERS','Others')
    )
    type = models.CharField(max_length=100,choices=type_choices)

    def __str__(self):
        return self.name

class Distance(models.Model):
    city1 = models.CharField(max_length=100)
    city2 = models.CharField(max_length=100)
    distance = models.FloatField()
    timeindays = models.IntegerField()

    def __str__(self):
        return self.city1
class Ratings(models.Model):
    comcode=models.CharField(max_length=100)
    rating = models.FloatField()
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.comcode
