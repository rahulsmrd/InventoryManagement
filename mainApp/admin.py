from django.contrib import admin
from mainApp.models import Supplier, Product, SaleOrder, StockMovement

# Register your models here.
admin.site.register(Supplier)

admin.site.register(Product)

admin.site.register(SaleOrder)

admin.site.register(StockMovement)