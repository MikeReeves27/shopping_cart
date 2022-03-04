from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import CartItem, InventoryItem
from django.db.models import Sum


# Function for viewing shopping cart. It retrieves all data from the database and stores it in a dictionary
def shopping_cart_view(request):
    all_cart_items = CartItem.objects.all()
    return render(request, 'shopping_cart.html', {'all_items': all_cart_items})


# Function for searching. It loads the 'search' page
def search(request):
    return render(request, 'search.html')


# Function for display search results. It stores all string matches in a list and sends the results to
# the 'search results' page
def search_results(request):
    result = request.POST['search_bar']
    all_inventory_items = InventoryItem.objects.all()

    matches = []
    for item in all_inventory_items:
        if result in item.item_name:
            matches.append(item)

    return render(request, 'search_results.html', {'dictionary': matches})


# Function for adding to cart. It retrieves the current item_id from InventoryItem and stores its name and price
# in the CartItem database
def add_to_cart(request, item_id):
    get_item = InventoryItem.objects.get(id=item_id)
    new_item = CartItem(item_name=get_item.item_name, item_price=get_item.item_price)
    new_item.save()
    return HttpResponseRedirect('/')


# Function for removing an item from the cart. It deletes it from the CartItem database
def delete_item(request, item_id):
    CartItem.objects.get(id=item_id).delete()
    return HttpResponseRedirect('/')


# Function for checking out. It removes all items from the cart and reloads the root page
def check_out(request):
    all_inventory_items = CartItem.objects.all()
    for item in all_inventory_items:
        item.delete()
    return HttpResponseRedirect('/')
