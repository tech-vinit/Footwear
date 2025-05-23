from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Customer,Cart,Profile
from django.views import View
from django.contrib import messages
from.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout

 

def home(request):
    product = Product.objects.all()
    context={
        
        'product':product
    }
    return render(request,'index.html',context)

def allproducts(request):
    allproducts=Product.objects.all()
    context={
        'allproducts':allproducts
    }
    return render(request,'allproducts.html',context)

def about(request):
    return render(request,'about.html')

def status(request):
    return render(request,'status.html')

def contact(request):
    return render(request,'contact.html')

def productdetail(request,id):
    detail=Product.objects.get(pk=id)
    allproduct=Product.objects.all()
    
    context={
        'detail':detail,
        'allproduct':allproduct
    }
    return render(request,'productdetail.html',context)

def mencasual(request):
    mc= Product.objects.filter(category='Men Casual')
    context = {
        'mc':mc,
    }
    return render(request,'mencasual.html',context)

def menformal(request):
    mf=Product.objects.filter(category='Men Formal')
    context={
        'mf':mf,
    }
    return render(request,"menformal.html",context)



def mensport(request):
    ms= Product.objects.filter(category='Men Sport')
    context = {
        'ms':ms,
    }
    return render(request,'mensport.html',context)

def men(request, data=None):
    products= mc = mf = ms = None
    if data == 'None':
        mc=Product.objects.filter(category='Men Casual')
        mf=Product.objects.filter(category='Men Formal')
        ms=Product.objects.filter(category='Men Sport')
    elif data == 'Addidas':
        products = Product.objects.filter(category='Men Sport').filter(brand = 'Addidas')
        
    elif data == 'Nike':
        products = Product.objects.filter(category='Men Sport').filter(brand = 'Nike')
        
    elif data == 'Campus':
        products = Product.objects.filter(category='Men Sport').filter(brand = 'Campus')
        
    elif data == 'Puma':
        products = Product.objects.filter(category='Men Sport').filter(brand = 'Puma')
    elif data=='Red Tape':
        products=Product.objects.filter(category='Men Formal').filter(brand='Red Tape')
    elif data=='Hush Puppies':
        products=Product.objects.filter(category='Men Formal').filter(brand='Hush Puppies')
    elif data=='Lee Cooper':
        products=Product.objects.filter(category='Men Formal').filter(brand='Lee Cooper')
    elif data=='Bata':
        products=Product.objects.filter(category='Men Formal').filter(brand='Bata')
    
    context = {
        
        'mf':mf,
        'mc':mc,
        'ms':ms,
        'products':products

    }
    return render(request,'menshoes.html', context)

def women(request,data=None):
    wc=wf=ws=products=None
    if data== 'None':
        wc = Product.objects.filter(category='Women Casual')
        wf = Product.objects.filter(category='Women Formal')
        ws = Product.objects.filter(category='Women Sport')
    elif data == 'Nike':
        products = Product.objects.filter(category='Women Sport').filter(brand = 'Nike')
    elif data == 'Gucci':
        products = Product.objects.filter(category='Women Sport').filter(brand = 'Gucci')
    elif data == 'Clarks':
        products = Product.objects.filter(category='Women Sport').filter(brand = 'Clarks')
    elif data == 'Catwalk':
        products = Product.objects.filter(category='Women Sport').filter(brand = 'Catwalk')
    elif data == 'Bata':
        products = Product.objects.filter(category='Women Casual').filter(brand = 'Bata')
    elif data == 'Red Tape':
        products = Product.objects.filter(category='Women Formal').filter(brand = 'Red Tape')
    elif data == 'Mochi':
        products = Product.objects.filter(category='Women Formal').filter(brand = 'Mochi')
    elif data == "Khadim's Cleo":
        products = Product.objects.filter(category='Women Sport').filter(brand = "Khadim's Cleo")
   
    context = {
        'wc':wc,
        'wf':wf,
        'ws':ws,
        'products':products
    }
    return render(request,'womenshoes.html', context)


def womencasual(request):
    wc=Product.objects.filter(category='Women Casual')
    context = { 
        'wc':wc,
    }
    return render(request,'womencasual.html',context)
def womenformal(request):
    wf=Product.objects.filter(category='Women Formal')
    context = { 
        'wf':wf,
    }
    return render(request,'womenformal.html',context)
def womensport(request):
    ws=Product.objects.filter(category='Women Sport')
    context = { 
        'ws':ws,
    }
    return render(request,'womensport.html',context)


class RegistrationView(View):
    def get(self,request):
        form=RegistrationForm()
        return render(request,'registration.html',{'form':form})
    
    def post(self,request):
        form=RegistrationForm(request.POST)
        if  form.is_valid():
            messages.success(request,"Congatulation Registration Successfully")
            form.save()
        return render(request,"login.html",{'form':form}
        )

def logoutview(request):
    logout(request)
    return redirect(home)

def search(request):
    q=request.GET.get('query')
    data=Product.objects.filter(product_name__icontains = q)

    context={
        'q':q,
        'data':data
    }
    return render(request,"search.html",context)


def cart(request,product_id):
    product= get_object_or_404(Product,pk=product_id)
    customer,created=Customer.objects.get_or_create(user=request.user)
    
    cart_item, created = Cart.objects.get_or_create(customer=customer, product=product)

    if not created:
        cart_item.quantity+=1
    cart_item.save()
    return redirect('addtocart')

def addtocart(request):
    customer=Customer.objects.get(user=request.user)
    carts=Cart.objects.filter(customer=customer)
    total_price=0
    total_quantity=0
    for item in carts:
        total_price += item.product.discounted_price*item.quantity
        total_quantity += item.quantity

    context={
        "carts":carts,
        "total_price":total_price,
        "total_quantity":total_quantity,
        
    }
    return render(request,"addtocart.html",context)

def deletecart_item(request, id):
    customer = Customer.objects.get(user=request.user)
    cart_item = get_object_or_404(Cart, id=id, customer=customer)
    cart_item.delete()
    return redirect('addtocart')

def checkout(request):
    if request.method=="POST":
        nm=request.POST.get('full_name')
        add=request.POST.get('address')
        ci=request.POST.get('city')
        pin=request.POST.get('pincode')
        con=request.POST.get('country')
        mobile=request.POST.get('phone') 
        record=Profile(name=nm,address=add,city=ci,pincode=pin,country=con,mobile_number=mobile)
        record.save()
        return redirect(orderplace)
    
    return render(request,'checkout.html')

def orderplace(request):
    customer=Customer.objects.get(user=request.user)
    carts=Cart.objects.filter(customer=customer)
    total_price=0
    total_quantity=0
    for item in carts:
        total_price += item.product.discounted_price*item.quantity
        total_quantity += item.quantity

    context={
        "carts":carts,
        "total_price":total_price,
        "total_quantity":total_quantity,
        
    }
    return render(request,'orderplace.html',context)

def order_successfull(request):
    return render(request, 'order_successfull.html')


