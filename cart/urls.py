from django.contrib import admin
from django.urls import path
from shopping_cart.views import shopping_cart_view, search, search_results, add_to_cart, delete_item, check_out

# Store each URL and their respective function in a list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shopping_cart_view),
    path('search/', search),
    path('search_results/', search_results),
    path('addtocart/<int:item_id>/', add_to_cart),
    path('delete/<int:item_id>/', delete_item),
    path('checkout/', check_out)
]