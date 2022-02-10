from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(
        blank=False,
        null=False,
        max_length=50
    )
    country = models.CharField(
        blank=False,
        null=False,
        max_length=50
    )
    county = models.CharField(
        blank=False,
        null=False,
        max_length=50
    )
    location = models.CharField(
        blank=False,
        null=False,
        max_length=50
    )
    quantity = models.CharField(
        null=True,
        blank=True,
        default='Undefined Quantity',
        max_length=200
    )
    price = models.CharField(
        blank=False,
        null=False,
        max_length=50
    )
    pimage = models.ImageField(
        upload_to='images',
        null=True,
        blank = True,
        editable=True
    )

    class Meta:
        db_table = 'Food'

    def __str__(self) -> str:
        return self.product_name

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Delivered', 'Delivered'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Food, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True)
    time_ordered = models.TimeField(auto_now_add=True, null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=200, null=True, default='Pending')

    class Meta:
        db_table = 'Order'

    def __str__(self) -> str:
        return self.product.product_name
