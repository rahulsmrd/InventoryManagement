from django import forms
from mainApp.models import Supplier, Product, SaleOrder, StockMovement

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ('name', 'address', 'email', 'phone')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address', 'rows':3}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'descriprion', 'price', 'stock_quantity', 'supplier', 'category')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'descriprion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Product Description', 'rows':3}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'stock_quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Category'}),
            }
        
class SaleOrderForm(forms.ModelForm):
    class Meta:
        model = SaleOrder
        fields = ('product', 'quantity')
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),
        }
    
class StockMovementForm(forms.ModelForm):
    class Meta:
        model = StockMovement
        fields = ('product', 'quantity', 'movement_type', 'notes')
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),
            'movement_type': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Notes', 'rows':3}),
        }
