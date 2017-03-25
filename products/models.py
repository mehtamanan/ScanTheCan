from django.db import models
from companies.models import Company
# Create your models here.


class Product(models.Model):
    company = models.ForeignKey(Company, related_name="products")
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    price = models.IntegerField(default=0)
    barcode = models.IntegerField(unique=True)
    quantity = models.IntegerField(default=0)