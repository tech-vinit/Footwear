from django.contrib import admin

from .models import(
    Customer,
    Product,
    Cart,
    OrderPlaced,
    Profile
    
    
    )

@admin.register(Customer)

class CustomerAdmin(admin.ModelAdmin):
    list_display=('user','name','locality','city','zipcode','state')

@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','selling_price','discounted_price','description','category','brand','image')

@admin.register(Cart)

class CartAdmin(admin.ModelAdmin):
    list_display=('customer','product','quantity')


@admin.register(OrderPlaced)

class OrderPlacedAdmin(admin.ModelAdmin):
    list_display=('customer','product','cart','quantity','ordered_date','status')

@admin.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    list_display=('name','address','city','pincode','country','mobile_number')

