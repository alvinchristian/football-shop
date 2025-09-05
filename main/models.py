from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=15)
    is_featured = models.BooleanField(default=False)
# Create your models here.
