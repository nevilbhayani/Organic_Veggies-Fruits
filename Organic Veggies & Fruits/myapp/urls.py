from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

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
    path("logout/",logoutpage,name="logout"),
    path("addtocart/<id>",addtocart,name="addtocart")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)