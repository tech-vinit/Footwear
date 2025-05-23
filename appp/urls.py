from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm

urlpatterns = [
    path('',views.home,name='home'),
    path('status',views.status,name='status'),
    path('allproducts/',views.allproducts,name='allproducts'),
    path('about/',views.about,name='about'),
    path('orderplace/',views.orderplace,name='orderplace'),
    path('search/',views.search,name='search'),
    path('contact/',views.contact,name='contact'),
    path('checkout/',views.checkout,name='checkout'),
    path('productdetail/<int:id>',views.productdetail,name='productdetail'),
    path('addtocart/',views.addtocart,name='addtocart'),
    path('cart/<product_id>',views.cart,name='cart'),
    path('deletecart_item/<int:id>',views.deletecart_item,name='deletecart_item'),
    path('women/<data>',views.women,name='women'),
    path('womencasual/',views.womencasual,name='womencasual'),
    path('womenformal/',views.womenformal,name='womenformal'),
    path('womensport/',views.womensport,name='womensport'),
    path('men/<data>',views.men,name='men'),
    path('mencasual/',views.mencasual,name='mencasual'),
    path('menformal/',views.menformal,name='menformal'),
    path('mensport/',views.mensport,name='mensport'),
    path('registration/',views.RegistrationView.as_view(),name='registration'),
    path('logout/',views.logoutview,name='logout'),
    path('order_successfull/',views.order_successfull,name='order_successfull'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
