from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


STATE_CHOICES = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Delhi', 'Delhi'),
    ('Goa', 'Goa'),
    ('Gujrat', 'Gujrat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhan', 'Jharkhan'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Maharashtra', 'Maharashtra'),
    ('Madhaya Pradesh', 'Madhaya Pradesh'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Tripura', 'Tripura'),
    ('Telangana', 'Telangana'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
    ('Andaman & Nicobar (UT)', 'Andaman & Nicobar (UT)'),
    ('Chandigarh', 'Chandigarh'),
    ('Dadra & Nagar Haveli and Daman & Diu (UT)', 'Dadra & Nagar Haveli and Daman & Diu (UT)'),
    ('Jammu & Kashmir', 'Jammu & Kashmir'),
    ('Ladakh', 'Ladakh'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Puducherry', 'Puducherry'),
)

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    zipcode=models.IntegerField(blank=True,null=True)
    state=models.CharField(choices=STATE_CHOICES,max_length=50)

    def __str__(self):
        return str(self.user)
    
CATEGORY_CHOICES=(
    ('Men Casual','Men Casual'),
    ('Men Formal','Men Formal'),
    ('Men Sport','Men Sport'),
    ('Women Casual','Women Casual'),
    ('Women Formal','Women Formal'),
    ('Women Sport','Women Sport'),
)

class Product(models.Model):
    product_name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="product-img")
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=50)
    brand=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return str(self.id)
    

class Cart(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)


    def __str__(self):
        return str(self.id)
    

STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancelled','Cancelled')
)


class OrderPlaced(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    ordered_date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100,choices=STATE_CHOICES,default="Pending")


    def __str__(self):
        return str(self.id)


class Profile(models.Model):
    name=models.CharField(max_length=100)
    address=models.TextField()
    state=models.CharField(max_length=100,blank=True,null=True)
    city=models.CharField(max_length=100)
    pincode=models.IntegerField(blank=True,null=True)
    country=models.CharField(max_length=100)
    mobile_number = models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return self.name



