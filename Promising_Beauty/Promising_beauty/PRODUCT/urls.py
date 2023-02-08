from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('product',views.product,name="shop"),
    path('<int:id>',views.prods_detail),
    path('Addtocart',views.add_to_cart,name='CART'),
    path('add',views.show_cart,name='add')
    
]