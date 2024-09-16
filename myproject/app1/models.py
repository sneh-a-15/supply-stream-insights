from django.db import models
from django.contrib.auth.models import User
import random
from inventory.models import Supplier
# Create your models here.

CATEGORY_CHOICES = [
    ('Clothing & Apparel', 'Clothing & Apparel'),
    ('Electronics & Gadgets', 'Electronics & Gadgets'),
    ('Food Items', 'Food Items'),
    ('Home & Kitchen', 'Home & Kitchen'),
    ('Books & Media', 'Books & Media'),
    ('Sports & Outdoor', 'Sports & Outdoor'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Other fields related to the user profile

class UserPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f'{self.user.username} - {self.category}'
    
class UserProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    price = models.FloatField()
    stock_level = models.IntegerField()
    image_url = models.URLField(max_length=500, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.product_name} - {self.user.username}'
    
    def is_out_of_stock(self):
        return self.stock_level <= 0
    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(UserProduct, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"