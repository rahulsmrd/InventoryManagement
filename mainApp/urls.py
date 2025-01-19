from django.urls import path
from mainApp.views import (
    home,
    addSupplierView,
    listSuppliersView,
    addProductView,
    listProductsView,
    createSaleOrderView,
    updateSaleOrderView,
    listSaleOrderView,
    addStockMovementView,
    check_stock 
)

urlpatterns =[
    path('', home, name='home'),
    path('add/supplier/', addSupplierView.as_view(), name='add_supplier'),
    path('list/suppliers/', listSuppliersView.as_view(), name='list_suppliers'),
    path('add/product/', addProductView.as_view(), name='add_product'),
    path('list/products/', listProductsView.as_view(), name='list_products'),
    path('create/sale-order/', createSaleOrderView.as_view(), name='create_sale_order'),
    path('update/sale-order/<int:pk>/', updateSaleOrderView, name='update_sale_order'),
    path('list/sale-orders/', listSaleOrderView.as_view(), name='list_sale_orders'),
    path('add/stock-movement/', addStockMovementView.as_view(), name='add_stock_movement'),
    path('check/stock/', check_stock, name='check_stocks'),
]