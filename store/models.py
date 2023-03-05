from django.db import models

# Create your models here.
# Product
# title, sku, description, price, inventory, last_update


class Product(models.Model):
    sku = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=255)
    sku = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)

# Customer
# first_name, last_name, email, phone, birth_date


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_lenth=20)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=50)
    birth_date = models.DateField(null=True)


# Oder
# placed_at, payment_status
payment_status_pending = "P"
payment_status_complete = "C"
payment_status_failed = "F"
payment_status_choice = [
    (payment_status_pending, "Pending"),
    (payment_status_pending, "Complete"),
    (payment_status_pending, "Failed"),
]

class Order(models.Model):
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=payment_status_choice, default=payment_status_pending)

# Relation ship of Customer address
class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length = 200)
    # show the relation ship with Customer class "one to one"
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)