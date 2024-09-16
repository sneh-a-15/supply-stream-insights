from django.db import models
from django.contrib.auth.models import User

# Create yourfrom django.db import models

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()
    inventory_level = models.IntegerField(default=0)  # Ensure this line is present

    def __str__(self):
        return self.name

class Supplier(models.Model):
    id = models.AutoField(primary_key=True)  # Match the ID field from the API
    name = models.CharField(max_length=255)
    contact_info = models.TextField()
    category = models.CharField(max_length=255, default='abc')
    # Add other fields if necessary

    def __str__(self):
        return self.name

