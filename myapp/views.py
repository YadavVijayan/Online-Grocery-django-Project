from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Register,Category,Addproduct,tCart,sales,salessub,address
from django.db.models.functions import Coalesce
from django.db.models import Max, Value
from django.db.models import F
from datetime import date
import pyttsx3
class View(TemplateView):
    template_name = "index.html"

def userreg(request):
    if request.method=="POST":
        a = request.POST.get('t1')
        b = request.POST.get('t2')
        su=Register(uname=a,pword=b)
        su.save()
    return render(request,"index.html")

def userlogin(request):
    if request.method=="POST":
        c = request.POST.get('t3')
        d = request.POST.get('t4')
        lu=Register.objects.filter(uname=c,pword=d)
        for i in lu:
            ids = i.id
            name = i.uname
            pas = i.pword
            rts = i.rights
            request.session['ids'] = ids
            request.session['uname'] = name
            request.session['pword'] = pas
            request.session['rights'] = rts
        if lu.filter(uname=c,pword=d).exists():
            for j in lu:
                r=j.rights
            if r=='User':
                brec = Category.objects.all()
                return render(request,"user.html",{"brec":brec,"ids":ids})
            else:
                brec = Category.objects.all()
                return render(request,"admint/index.html",{"brec":brec})
        else:
            engine = pyttsx3.init()
            msg = "Invalid Username or Password"
            engine.say(msg)
            emgine.runAndWait()
    return render(request,"user.html")

def View2(request,addcategory):
   # prec = Addproduct.objects.filter(id=id)
    #for j in prec:
     #   p=j.productname
      #  pr=j.productprice
    prec = Addproduct.objects.filter(addcategory=addcategory)
    return render(request,"products.html",{"prec":prec})

def View3(request):
    return render(request,"wishlist.html")
def cadd(request):
    brec = Category.objects.all()
    return render(request,"admint/Addcategory.html",{"brec":brec})

def Addcat(request):
    brec=Category.objects.all()
    if request.method=="POST":
       br = request.POST.get('t5')
       lu = Category.objects.filter(addcategory=br)
       if lu.filter(addcategory=br).exists():
           return render(request,"admint/Addcategory.html",{"brec":brec})
       else:
           m = Category(addcategory=br)
           m.save()
    return render(request,"admint/Addcategory.html",{"brec":brec})

def Addgrocery(request,addcategory):
    prec = Addproduct.objects.filter(addcategory=addcategory)
    if request.method=="POST":
        u=request.FILES['t6']
        y=request.POST.get('t8')
        x = request.POST.get('t9')
        z1 = request.POST.get('t10')
        sav=Addproduct(productimg=u,addcategory=addcategory,productname=y,productprice=x,productquantity=z1)
        sav.save()
    return render(request,"admint/ProAdd.html",{"addcategory":addcategory,"prec":prec})

def Prodetail(request,id):
    prec = Addproduct.objects.filter(id=id)
    for j in prec:
        p=j.productname
        pr=j.productprice
    sav = sales.objects.aggregate(sav=Coalesce(Max('salesno'),Value(0)))['sav']
    orderno=int(sav)+1
    st=tCart.objects.aggregate(st=Coalesce(Max('serialno'),Value(0)))['st']
    cartno=int(st)+1
    if request.method=="POST":
        o=request.POST.get('qty1')
        total=pr*int(o)
        ins=tCart(orderno=orderno,serialno=cartno,pid=id,pname=p,quantity=o,rate=pr,total=total)
        ins.save()
        brec = Category.objects.all()
        return render(request, "user.html",{"brec":brec})
    return render(request, "productdetail.html",{"prec":prec})
def cart(request):
    trec=tCart.objects.all()
    total=0
    for n in trec:
        total=total+n.total
    return render(request, "cart.html",{"trec":trec,"total":total})

def Checkout(request):
    return render(request,"checkout.html")
def useraddress(request):
    if request.method=="POST":
        a1 = request.POST.get('c1')
        b1 = request.POST.get('c2')
        a2 = request.POST.get('c3')
        b2 = request.POST.get('c4')
        a3 = request.POST.get('c5')
        b3 = request.POST.get('c6')
        a4 = request.POST.get('c7')
        b4 = request.POST.get('c8')
        a5 = request.POST.get('c9')
        sub=address(fname=a1,lname=b1,country=a2,staddress=b2,town=a3,state=b3,pin=a4,ph=b4,email=a5)
        sub.save()
        if request.method=="POST":
            trec = tCart.objects.all()
            sav = sales.objects.aggregate(sav=Coalesce(Max('salesno'), Value(0)))['sav']
            orderno = int(sav) + 1
            total = 0

            for n in trec:
                total = total + n.total

                today=date.today()
                d1=today.strftime(("%b-%d-%y"))
                ids=request.session['ids']
                uname= request.session['uname']
            return render(request,"payment.html",{"orderno":orderno,"total":total,"d1":d1,"ids":ids,"uname":uname})
    return render(request,"user.html")
def stockupdation(request):
    if request.method == "POST":
        p1 = request.POST.get('q1')
        p2 = request.POST.get('q2')
        p3 = request.POST.get('q3')
        p4 = request.POST.get('q4')
        trec = tCart.objects.all()
        sav = sales.objects.aggregate(sav=Coalesce(Max('salesno'), Value(0)))['sav']
        orderno = int(sav) + 1
        total = 0

        for n in trec:
            total = total + n.total

        sto = sales(salesno=orderno,custid=request.session['ids'],cname=request.session['uname'],total=total,cardno=p1, expdate=p2, ccv=p3, carduser=p4)

        sto.save()
        trec = tCart.objects.all()
        for j in trec:
            pid=j.pid
            pname=j.pname
            quantity=j.quantity
            rate=j.rate
            total=j.total
            ap=salessub(salesno=orderno,productid=pid,pname=pname,quantity=quantity,rate=rate,total=total)
            ap.save()
            Addproduct.objects.filter(id=pid).update(productquantity=F('productquantity')-quantity)
        tCart.objects.all().delete()
    return render(request, "user.html")



