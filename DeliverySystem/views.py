from django.shortcuts import render,redirect
from .models import *
from datetime import date,datetime
from CommodityApp.models import *

# Create your views here.

def assignCourier(ordercode,perishable,city1,city2):
    if(perishable):
        a = Courier.objects.filter(usertype="SF")
        for i in a:
            datenew = date.today()
            b = CourierOrder(username=i.username_id.username,status="PENDING",ordercode=ordercode,city1=city1.capitalize(),city2=city2.capitalize(),date=datenew)
            b.save()
            c = Order.objects.filter(ordercode=ordercode)
            for j in c:
                j.orderstatus = "Yet to be shipped"
                j.couriername = i.username_id.username
                j.save()
    else:
        a = Courier.objects.filter(usertype="NL")
        for i in a:
            datenew = date.today()
            b = CourierOrder(username=i.username_id.username,status="PENDING",ordercode=ordercode,city1=city1.capitalize(),city2=city2.capitalize(),date=datenew)
            b.save()
            c = Order.objects.filter(ordercode=ordercode)
            for j in c:
                j.orderstatus = "Yet to be shipped"
                j.couriername = i.username_id.username
                j.save()

def assignDelivery(request,ordercode,city):
    a = DeliveryBoy.objects.filter(city=city.capitalize()).order_by('orders')
    j = a[0]
    c = CourierOrder.objects.filter(ordercode=ordercode)
    for i in c:
        i.status="DELIVERED"
        i.save()
    datenew = date.today()
    j.orders = j.orders +1
    j.save()
    b = DeliveryOrder(username=j.username_id.username,ordercode=ordercode,date=datenew,status="PENDING")
    b.save()
    b = Order.objects.filter(ordercode=ordercode)
    for k in b:
        k.orderstatus="Shipped"
        k.deliveryboy = j.username_id.username
        k.save()
    return redirect('CourierDashboard')

def assignDeliveryDirect(ordercode,city):
    a = DeliveryBoy.objects.filter(city=city.capitalize()).filter(status="Available").order_by('orders')
    c = CourierOrder.objects.filter(ordercode=ordercode)
    for i in c:
        i.status="DELIVERED"
        i.save()
    for j in a:
        datenew = date.today()
        j.orders = j.orders +1
        j.save()
        b = DeliveryOrder(username=j.username_id.username,ordercode=ordercode,date=datenew,status="PENDING")
        b.save()
        b = Order.objects.filter(ordercode=ordercode)
        for k in b:
            k.orderstatus="Shipped"
            k.deliveryboy = j.username_id.username
            k.save()

def CourierDashboard(request):
    hd = Courier.objects.filter(username_id=request.user)
    if(hd):
        a = CourierOrder.objects.filter(username=request.user.username)
        response = {'couriers':a}
        return render(request,'courierdashboard.html',response)
    else:
        form = CForm(request.POST)
        response = {'form':form}
        if request.method=="POST":
            if form.is_valid():
                city = form.cleaned_data['city']
                usertype = form.cleaned_data['usertype']
                deliverychargeperkg = form.cleaned_data['deliveryChargePerKg']
                gfh = Courier(username_id=request.user,city=city,usertype=usertype,deliverychargeperkg=deliverychargeperkg)
                gfh.save()
                return redirect('CourierDashboard')
            else:
                return render(request,'courierdashboard.html',response)
        else:
            return render(request,'courierdashboard.html',response)

def DeliveryDashboard(request):
    hd = DeliveryBoy.objects.filter(username_id=request.user)
    if(hd):
        a = DeliveryOrder.objects.filter(username=request.user.username)
        response = {'deliveries':a}
        return render(request,'deliverydashbord.html',response)
    else:
        form = DForm(request.POST)
        response = {'form':form}
        if request.method=="POST":
            if form.is_valid():
                city = form.cleaned_data['city']
                status = form.cleaned_data['status']
                gfh = DeliveryBoy(username_id=request.user,city=city,status=status)
                gfh.save()
                return redirect('DeliveryDashboard')
            else:
                return render(request,'deliverydashbord.html',response)
        else:
            return render(request,'deliverydashbord.html',response)

def Delivered(request,ordercode):
    a = DeliveryOrder.objects.filter(ordercode=ordercode)
    for i in a:
        i.status="DELIVERED"
        i.save()
    b = Order.objects.filter(ordercode=ordercode)
    for i in b:
        i.orderstatus="DELIVERED"
        i.save()
    c = DeliveryBoy.objects.filter(username_id=request.user)
    for i in c:
        i.orders = i.orders-1
        i.save()
    return redirect('DeliveryDashboard')

def AssignTruck(ordercode,city1,city2,perishable):
    m = Order.objects.filter(ordercode=ordercode)
    for i in m:
        i.status = "On the way"
        i.save()
    d = None
    if(perishable):
        e = TruckDrivers.objects.filter(city=city).filter(trucktype="AC")
        for i in e:
            c = TruckOrder.objects.filter(username=i.username_id.username).filter(date=date.today())
            if(c):
                pass
            else:
                a = i
                break
        if(d == None):
            a = TruckDrivers.objects.filter(city=city).filter(trucktype="AC")[0]
        b = TruckOrder(username=a.username_id.username,ordercode=ordercode,city1=city1,city2=city2,date=date.today())
        a.status="Busy"
        a.save()
        b.save()
    else:
        print(city1)
        a = TruckDrivers.objects.filter(city=city1).filter(trucktype="NL")[0]
        b = TruckOrder(username=a.username_id.username,ordercode=ordercode,city1=city1,city2=city2,date=date.today())
        a.status="Busy"
        a.save()
        b.save()

def TruckDashboard(request):
    hd = DeliveryBoy.objects.filter(username_id=request.user)
    if(hd):
        a = TruckOrder.objects.filter(username=request.user.username)
        response = {'TruckOrder':a}
        return render(request,'truckdashboard.html',response)
    else:
        form = TForm(request.POST)
        response = {'form':form}
        if request.method=="POST":
            if form.is_valid():
                city = form.cleaned_data['city']
                status = form.cleaned_data['status']
                trucktype = form.cleaned_data['trucktype']
                gfh = TruckDrivers(username_id=request.user,city=city,status=status,trucktype=trucktype)
                gfh.save()
                return redirect('TruckDashboard')
            else:
                return render(request,'truckdashboard.html',response)
        else:
            return render(request,'truckdashboard.html',response)


def TruckDelivered(request,ordercode):
    a = Order.objects.filter(ordercode=ordercode)
    for i in a:
        i.orderstatus = "DELIVERED"
        i.save()
    b = TruckOrder.objects.filter(ordercode=ordercode)
    for j in b:
        j.status="DELIVERED"
        j.save()
        c = TruckDrivers.objects.filter(username_id=request.user)
        for k in c:
            k.status = "Available"
            k.save()
    return redirect('TruckDashboard')
