from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Users)
admin.site.register(Courier)
admin.site.register(TruckDrivers)
admin.site.register(DeliveryBoy)
admin.site.register(CourierOrder)
admin.site.register(DeliveryOrder)
admin.site.register(TruckOrder)
