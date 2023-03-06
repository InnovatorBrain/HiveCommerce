from django.db import models

# manytomany relationships between Promotion and Product


class Promotion(models.Model):
    description = models.CharField(max_length=250)
    discount = models.FloatField()
    # products

    # Create your models here.
    # Collection


class Collection(models.Model):
    title = models.CharField(max_length=50)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null = True, related_name = '+')


# Product
# title, sku, description, price, inventory, last_update


class Product(models.Model):
    sku = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(default='-')
    sku = models.IntegerField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(
        Promotion, related_name='products')  # it shows the reverse relation


# Customer
# first_name, last_name, email, phone, birth_date


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
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


# OrderItem items

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


# Relation ship of Customer address

class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zip = models.CharField(max_length=25, default=0)
    # show the relation ship with Customer class "one to one"
    # customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    # but we want to allow for many addresses
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

# Cart


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

# CartItem


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()

