from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.conf import settings
from .forms import *
from .models import *
from DeliverySystem.models import *
from datetime import date,datetime
import uuid
from DeliverySystem import views


def indexView(request):
    if(request.user.is_authenticated):
        a = UserType.objects.filter(username = request.user.username)
        response={}
        if(a):
            for i in a:
                if(i.usertype == "FR"):
                    f = {'type':i.usertype}
                    response = {**f}
                elif(i.usertype=="RB"):
                    f = {'type':i.usertype}
                    response = {**f}
                elif(i.usertype == "MR"):
                    f = {'type':i.usertype}
                    response = {**f}
            return render(request,"index.html",response)
        else:
            a = Users.objects.filter(username = request.user.username)[0]
            if(a.usertype == "CC"):
                return redirect('CourierDashboard')
            elif(a.usertype == "DB"):
                return redirect('DeliveryDashboard')
            elif(a.usertype == "TD"):
                return redirect('TruckDashboard')
    else:
        return render(request,"index.html")


def registerView(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        form1 = UserTypeForm(request.POST)
        if form.is_valid():
            form.save()
            if form1.is_valid():
                username = form.cleaned_data['username']
                type = form1.cleaned_data['usertype']
                if(type=='FR' or type == 'RB' or type == 'MR'):
                    a = UserType(username=username,usertype=type)
                    a.save()
                else :
                    a = Users(username=username,usertype=type)
                    a.save()
            return redirect('login_url')
    else:
            form=SignUpForm()
            form1 = UserTypeForm(request.POST)

            return render(request,'register.html',{'form': form,'form1':form1})
    return render(request,'register.html',{'form': form,'form1':form1})

@login_required
def Dashboard(request):
    a = UserType.objects.filter(username = request.user.username)
    response={}
    if(a):
        for i in a:
            if(i.usertype == "FR"):
                abc = Farmer.objects.filter(username_id=request.user)
                if(abc):
                    a = Commodities.objects.filter(username_id=request.user)
                    d = {'commodities':a}
                    b = Order.objects.filter(seller=request.user.username)
                    e = {'orderforyou':b}
                    c = Order.objects.filter(buyer=request.user.username)
                    f = {'yourorder':c}
                    response = {**d,**e,**f}
                    return render(request,'dashboard.html',response)
                else:
                    form = FarmerForm(request.POST)
                    response = {'form':form}
                    if request.method=="POST":
                        if form.is_valid():
                            address = form.cleaned_data['address']
                            city = form.cleaned_data['city']
                            state = form.cleaned_data['state']
                            gfh = Farmer(username_id=request.user,address=address,city=city,state=state)
                            gfh.save()
                            return redirect('dashboard')
                        else:
                            return render(request,'dashboard.html',response)
                    else:
                        print(response)
                        return render(request,'dashboard.html',response)
            elif(i.usertype=="RB"):
                abc = Customer.objects.filter(username_id=request.user)
                if(abc):
                    b = Order.objects.filter(buyer=request.user.username)
                    e = {'yourorder':b}
                    response = {**e}
                    return render(request,'dashboard.html',response)
                else:
                    form = CustomerForm(request.POST)
                    jhk = {'form':form}
                    response = {**jhk}
                    if request.method=="POST":
                        if form.is_valid():
                            address = form.cleaned_data['address']
                            city = form.cleaned_data['city']
                            state = form.cleaned_data['state']
                            gfh = Customer(username_id=request.user,address=address,city=city,state=state)
                            gfh.save()
                            return redirect('dashboard')
                        else:
                            return render(request,'dashboard.html',response)
                    else:
                        return render(request,'dashboard.html',response)
            elif(i.usertype == "MR"):
                abc = Manufacturer.objects.filter(username_id=request.user)
                if(abc):
                    b = Order.objects.filter(buyer=request.user.username)
                    e = {'yourorder':b}
                    response = {**e}
                    return render(request,'dashboard.html',response)
                else:
                    form = ManufacturerForm(request.POST)
                    response = {'form':form}
                    if request.method=="POST":
                        if form.is_valid():
                            address = form.cleaned_data['address']
                            company_name = form.cleaned_data['company_name']
                            company_add = form.cleaned_data['company_add']
                            licenceno = form.cleaned_data['licenceno']
                            address = form.cleaned_data['address']
                            address = form.cleaned_data['address']
                            city = form.cleaned_data['city']
                            state = form.cleaned_data['state']
                            gfh = Manufacturer(username_id=request.user,address=address,city=city,state=state,company_add=company_add,company_name=company_name,licenceno=licenceno)
                            gfh.save()
                            return redirect('dashboard')
                        else:
                            return render(request,'dashboard.html',response)
                    else:
                        return render(request,'dashboard.html',response)
    else:
        a = Users.objects.filter(username = request.user.username)
        for i in a:
            if(i.usertype == "CC"):
                return redirect('CourierDashboard')
            elif(i.usertype == "DB"):
                return redirect('DeliveryDashboard')
            elif(i.usertype == "TD"):
                return redirect('TruckDashboard')


def CommoditiesAdd(request):
    user = request.user
    form = CommodityForm(request.POST,request.FILES)
    if request.method=="POST" or request.method=="FILES":
        if form.is_valid():
            name = form.cleaned_data['name']
            amount = form.cleaned_data['amount']
            description = form.cleaned_data['description']
            breed=form.cleaned_data['breed']
            priceperkg = form.cleaned_data['priceperkg']
            priceperquintal = form.cleaned_data['priceperquintal']
            type = form.cleaned_data['type']
            perishable = form.cleaned_data['perishable']
            image = form.cleaned_data['image']
            rating = 0.0
            datenew = date.today()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            comcode = str(uuid.uuid4())
            a = Commodities(username_id=user,name=name,comcode=comcode,description=description,amount=amount,breed=breed,priceperkg=priceperkg,priceperquintal=priceperquintal,type=type,perishable=perishable,date=datenew,time=current_time,image=image)
            a.save()
            return redirect('dashboard')
        else:
            print(form.errors)
            return render(request,'commodity.html',{'form':form})
    else:
        return render(request,'commodity.html',{'form':form})

@login_required
def AllCommoditiesRetail(request):
    commodities = Commodities.objects.all()
    a = {'commodities':commodities}
    return render(request,'retailshop.html',a)

@login_required
def AllCommoditiesRetailType(request,type):
    commodities = Commodities.objects.filter(type=type)
    a = {'commodities':commodities}
    return render(request,'retailshop.html',a)

    return render(request,'retailshop.html',a)


@login_required
def AllCommoditiesRetailPriceLH(request):
    commodities = Commodities.objects.all().order_by('priceperkg')
    a = {'commodities':commodities}
    return render(request,'retailshop.html',a)


@login_required
def AllCommoditiesRetailPriceHL(request):
    commodities = Commodities.objects.all().order_by('priceperkg')
    a = {'commodities':commodities}
    return render(request,'retailshop.html',a)

@login_required
def AllCommoditiesRetailRating(request):
    commodities = reversed(Commodities.objects.all().order_by('rating'))
    a = {'commodities':commodities}
    return render(request,'retailshop.html',a)

def OneCommodity(request,comcode):
    commodity = Commodities.objects.filter(comcode = comcode)
    city1 =""
    city2 =""
    a = {'commodity':commodity}
    for i in commodity:
        b = Farmer.objects.filter(username_id=i.username_id)
    for i in b:
        city1=i.city
    c = Customer.objects.filter(username_id=request.user)
    if(c):
        pass
    else:
        c = Farmer.objects.filter(username_id=request.user)
    for i in c:
        city2 = i.city
    m = Distance.objects.filter(city1=city1.capitalize()).filter(city2=city2.capitalize())
    n={'distance':m}
    d = Courier.objects.filter(usertype="SF")
    e = {'charge':d}
    response = {**a,**n,**e}
    return render(request,'onecom.html',response)

def Confirm(request,comcode,weight):
    commodity = Commodities.objects.filter(comcode = comcode)
    deliveryprice = 0
    a = {'commodity':commodity}
    b = {'weight':weight}
    for i in commodity:
        price = i.priceperkg
        if i.perishable:
            d = Courier.objects.filter(usertype="SF")
            for j in d:
                deliveryprice = j.deliverychargeperkg*float(weight)
    if(float(weight)>10.0):
        price = price - price*0.01*weight
    bill = price * float(weight)
    c = {'bill':bill}
    tax = 0.08 * float(weight)
    d = {'tax':tax}
    total = bill+tax+deliveryprice
    e = {'total':total}
    f = {'deliveryprice':deliveryprice}
    response = {**a,**b,**c,**d,**e,**f}
    return render(request,'confirm.html',response)

def OrderPlace(request,comcode,weight,type):
    commodity = Commodities.objects.filter(comcode = comcode)
    deliveryprice = 0
    for i in commodity:
        ab = i.username_id
        seller=i.username_id.username
        price = i.priceperkg
        i.amount = i.amount - float(weight)
        i.save()
        name1 = i.name
        breed1 = i.breed
        type1 = i.type
        bc = i.perishable
        if i.perishable:
            d = Courier.objects.filter(usertype="SF")
            for j in d:
                deliveryprice = j.deliverychargeperkg*float(weight)
    buyer=request.user.username
    b = Farmer.objects.filter(username_id=ab)
    for i in b:
        city1=i.city
    c = Customer.objects.filter(username_id=request.user)
    if(c):
        pass
    else:
        c = Farmer.objects.filter(username_id=request.user)
    for i in c:
        city2 = i.city
    amount=weight
    if(float(weight)>10.0):
        price1 = price1 - price1*0.01*weight
    bill = price * float(weight)
    tax = 0.08 * float(weight)
    total = bill+tax+deliveryprice
    ordercode = str(uuid.uuid1())
    order = Order(seller=seller,buyer=buyer,amount=amount,price=price,ordercode=ordercode,comcode=comcode,ordertype=type,bill=bill,tax=tax,total=total,name=name1,breed=breed1,type=type1,deliveryprice=deliveryprice)
    order.save()
    if(city1.capitalize()==city2.capitalize()):
        views.assignDeliveryDirect(ordercode, city)
    else:
        views.assignCourier(ordercode, bc, city1, city2)
    return redirect('dashboard')

def AddToCart(request,comcode,weight):
    commodity = Commodities.objects.filter(comcode = comcode)
    for i in commodity:
        name1 =  i.name
        breed1 = i.breed
        type1 = i.type
    username = request.user.username
    a = Cart(comcode=comcode,name=name1,type=type1,breed=breed1,username=username,weight=weight)
    a.save()
    return redirect('retailshop')
@login_required
def CartView(request):
    one = request.user.username
    a = Cart.objects.filter(username = one)
    return render(request,'cart.html',{'cart':a})

def BuyCart(request):
    one = request.user.username
    price1 = 0
    a = Cart.objects.filter(username = one)
    for i in a:
        b = Commodities.objects.filter(comcode=i.comcode)
        deliveryprice=0
        for j in b:
            ab = j.username_id
            price1 = price1 + j.priceperkg
            seller=j.username_id.username
            price = j.priceperkg
            j.amount = j.amount - float(i.weight)
            j.save()
            name1 = j.name
            breed1 = j.breed
            type1 = j.type
            bc = j.perishable
            if j.perishable:
                d = Courier.objects.filter(usertype="SF")
                for k in d:
                    deliveryprice = k.deliverychargeperkg*float(i.weight)
        buyer=one
        bd = Farmer.objects.filter(username_id=ab)
        for l in bd:
            city1=l.city
        c = Customer.objects.filter(username_id=request.user)
        if(c):
            pass
        else:
            c = Farmer.objects.filter(username_id=request.user)
        for k in c:
            city2 = k.city
        amount=i.weight
        if(i.weight>10):
            price1 = price1 - price1*0.01*weight
        bill = price * float(i.weight)
        tax = 0.08 * float(i.weight)
        total = bill+tax+deliveryprice
        ordercode = str(uuid.uuid1())
        order = Order(seller=seller,buyer=buyer,amount=amount,price=price,ordercode=ordercode,comcode=i.comcode,ordertype=type,bill=bill,tax=tax,total=total,name=name1,breed=breed1,type=type1,deliveryprice=deliveryprice)
        order.save()
        if(city1.capitalize()==city2.capitalize()):
            views.assignDeliveryDirect(ordercode, city)
        else:
            views.assignCourier(ordercode, bc, city1, city2)
    tax1 = price*0.08
    total1 = price + tax
    a.delete()
    return redirect('dashboard')


def ManuFacturerShop(request):
    a = Commodities.objects.exclude(amount__lt=50.0)
    response = {'commodities':a}
    return render(request,'wholesaleshop.html',response)

def OneCommodityBulk(request,comcode):
    commodity = Commodities.objects.filter(comcode = comcode)
    city1 =""
    city2 =""
    a = {'commodity':commodity}
    for i in commodity:
        b = Farmer.objects.filter(username_id=i.username_id)
    for i in b:
        city1=i.city
    c = Manufacturer.objects.filter(username_id=request.user)
    for i in c:
        city2 = i.city
    m = Distance.objects.filter(city1=city1.capitalize()).filter(city2=city2.capitalize())
    n={'distance':m}
    response = {**a,**n}
    return render(request,'onecombulk.html',response)


def ConfirmBulk(request,comcode,weight):
    commodity = Commodities.objects.filter(comcode = comcode)
    a = {'commodity':commodity}
    b = {'weight':weight}
    for i in commodity:
        price = i.priceperquintal/100.0
        ab = i.perishable
        if(i.perishable):
            deliveryprice = 1000 * (float(weight)/100)
        else:
            deliveryprice = 200 * (float(weight)/100)
    bill = price * float(weight)
    c = {'bill':bill}
    tax = 0.18 * float(weight)
    d = {'tax':tax}
    f = {'deliveryprice':deliveryprice}
    total = bill+tax+deliveryprice
    e = {'total':total}
    response = {**a,**b,**c,**d,**e}
    return render(request,'confirmbulk.html',response)

def OrderPlaceBulk(request,comcode,weight,type):
    commodity = Commodities.objects.filter(comcode = comcode)
    for i in commodity:
        seller=i.username_id.username
        price = i.priceperquintal/100.0
        i.amount = i.amount - float(weight)
        i.save()
        name1 = i.name
        breed1 = i.breed
        type1 = i.type
        ab = i.perishable
        if(i.perishable):
            deliveryprice = 1000 * (float(weight)/100)
        else:
            deliveryprice = 200 * (float(weight)/100)
    buyer=request.user.username
    for i in commodity:
        b = Farmer.objects.filter(username_id=i.username_id)
    for i in b:
        city1=i.city
    c = Manufacturer.objects.filter(username_id=request.user)
    for i in c:
        city2 = i.city
    amount=weight
    bill = price * float(weight)
    tax = 0.18 * float(weight)
    total = bill+tax+deliveryprice
    ordercode = str(uuid.uuid1())
    order = Order(seller=seller,buyer=buyer,amount=amount,price=price,ordercode=ordercode,comcode=comcode,ordertype=type,bill=bill,tax=tax,total=total,name=name1,breed=breed1,type=type1,deliveryprice=deliveryprice,)
    order.save()
    views.AssignTruck(ordercode,city1,city2,ab)
    return redirect('dashboard')

def Feedback(request,comcode):
    form = FeedbackForm(request.POST)
    sum = 0.0
    a = {'form':form}
    if request.method == "POST":
        if form.is_valid():
            rating = form.cleaned_data['rating']
            desc = form.cleaned_data['desc']
            b = Ratings(comcode=comcode,rating=rating,desc=desc)
            b.save()
            c = Ratings.objects.filter(comcode=comcode)
            for i in c:
                sum = sum + i.rating
            rate = sum/len(a)
            d = Commodities.objects.filter(comcode=comcode)[0]
            d.rating = rate
            d.save()
            return redirect('dashboard')
        return render(request,'feedback.html',a)
    return render(request,'feedback.html',a)
