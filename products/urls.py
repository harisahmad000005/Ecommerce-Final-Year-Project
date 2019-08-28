
from django.urls import path, re_path


from products.views import (
    ProductListView,  
    ProductDetailSlugView 
                              )

urlpatterns = [
    
    path('', ProductListView.as_view()),

    path('<slug>', ProductDetailSlugView.as_view()),

]
