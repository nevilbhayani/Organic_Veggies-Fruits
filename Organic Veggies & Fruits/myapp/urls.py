from django.urls import path
from .views import *

urlpatterns = [

    path('', index, name='index'),
    path('index/', index, name='index'),
    path('shop/', shop, name='shop'),
    path('shop-detail/',shopdetail,name='shop-detail'),
    path('cart/',cart,name='cart'),
    path('chackout/',chackout,name='chackout'),
    path('testimonial/',testimonial,name='testimonial'),
    path('err/',err,name='err'),
    path('contactt/', contact, name='contact'),
    path('login/',loginpage,name="login"),
    path('registration/',regpage,name="reg"),
    path("logout/",logoutpage,name="logout")

]

