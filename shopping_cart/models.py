from django.db import models


# Database for items in user's current cart
class CartItem(models.Model):
    item_name = models.TextField()
    item_price = models.FloatField()


# Database for items in main inventory
class InventoryItem(models.Model):
    item_name = models.TextField()
    item_price = models.FloatField()
