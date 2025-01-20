from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from mainApp.models import Supplier, Product, SaleOrder, StockMovement
from mainApp.form import SupplierForm, ProductForm, SaleOrderForm, StockMovementForm

# Create your views here.
def home(request):
    return render(request, 'mainApp/home.html')
class addSupplierView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'mainApp/addSupplier.html'
    success_url = reverse_lazy('list_suppliers')

class listSuppliersView(ListView):
    model = Supplier
    template_name = 'mainApp/listSuppliers.html'
    context_object_name = 'suppliers'


class addProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'mainApp/addProduct.html'
    success_url = reverse_lazy('list_products')
    
class listProductsView(ListView):
    model = Product
    template_name = 'mainApp/listProducts.html'
    context_object_name = 'products'


class createSaleOrderView(CreateView):
    model = SaleOrder
    form_class = SaleOrderForm
    template_name = 'mainApp/addSaleOrder.html'
    success_url = reverse_lazy('list_sale_orders')

    
    def form_valid(self, form):
        sale_order = form.save(commit=False)
        qunatity = form.cleaned_data.get('quantity')
        product = form.cleaned_data.get('product')
        print(product)
        if product.stock_quantity >= qunatity:
            product.stock_quantity -= qunatity
            product.save()
            sale_order.total_price = int(qunatity) * int(product.price)
            StockMovement.objects.create(
                product=product,
                movement_type='Out',
                quantity=qunatity,
                notes='Sales order'
                )
            sale_order.save()
            return super().form_valid(form)
        else:
            return render(self.request, 'mainApp/addSaleOrder.html', {'form':form, 'errors':'Insufficient Stock'})
    
def updateSaleOrderView(request, pk):
    status = request.GET.get('status')
    sale_order = SaleOrder.objects.get(id=pk)
    sale_order.status = status
    sale_order.save()
    return redirect(reverse('list_sale_orders'))
    
class listSaleOrderView(ListView):
    model = SaleOrder
    template_name = 'mainApp/listSaleOrders.html'
    context_object_name ='sale_orders'


class addStockMovementView(CreateView):
    model = StockMovement
    form_class = StockMovementForm
    template_name = 'mainApp/addStockMovement.html'
    success_url = reverse_lazy('check_stocks')

    
    def form_valid(self, form):
        stock_movement = form.save(commit=False)
        product = form.cleaned_data.get('product')
        if stock_movement.movement_type == 'In':
            product.stock_quantity += stock_movement.quantity
            product.save()
        else:
            product.stock_quantity -= stock_movement.quantity
            if product.stock_quantity < 0:
                return render(self.request, 'mainApp/addStockMovement.html', {'form':form, 'errors':'Insufficient Stock'})
            product.save()
        stock_movement.product = product
        product.quantity = form.cleaned_data.get('quantity')
        stock_movement.save()
        return super().form_valid(form)
    
class listStockMovement(ListView):
    model = StockMovement
    template_name = 'mainApp/listStockMovement.html'
    context_object_name ='stock_movements'
    
def check_stock(request):
    all_products = Product.objects.all()
    pro = {}
    for product in all_products:
        pro[product.name] = product.stock_quantity
    return render(request, 'mainApp/checkStock.html', context = {'products':pro})