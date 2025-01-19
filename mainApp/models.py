from django.db import models

# Create your models here.
STATUS = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )

MOVEMNET = (
    ('In', 'In'),
    ('Out', 'Out'),
)

class Supplier(models.Model):
    name = models.CharField(max_length=511)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=1023, unique=True)
    descriprion = models.TextField()
    category = models.CharField(max_length=511)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    stock_quantity = models.IntegerField()
    supplier = models.ForeignKey(Supplier, related_name='supplier_products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SaleOrder(models.Model):
    product = models.ForeignKey(Product, related_name='sales', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=10)
    sale_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, default='Pending', max_length=32)
    def __str__(self):
        return f'{self.quantity} {self.product}'

class StockMovement(models.Model):
    product = models.ForeignKey(Product, related_name='stock_movements', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    movement_type = models.CharField(choices=MOVEMNET, max_length=32)
    movement_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.quantity} {self.product} {self.movement_type}'