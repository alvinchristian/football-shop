from django.db import models
import uuid
from django.contrib.auth.models import User
class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    Category_Choices = [
        ('topwear', 'Top Wear'),
        ('bottomwear', 'Bottom Wear'),
        ('shoes', 'Shoes'),
        ('gloves', 'Gloves'),
        ('accessories', 'Accessories'),
        ('socks', 'Socks'),
        ('trainingequipment', 'Training Equipment'),
        ('ball', 'Ball'),
        ('bag', 'Bag'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=Category_Choices)
    is_featured = models.BooleanField(default=False)
    brand = models.CharField(max_length=10,default='')
    sold = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    def add_sold(self, quantity):
        self.sold += quantity
        self.save()
# Create your models here.
