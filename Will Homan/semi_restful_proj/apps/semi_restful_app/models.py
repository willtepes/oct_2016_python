from __future__ import unicode_literals
from django.db import models

class ProductManager(models.Manager):
    def add_product(self, product):
        self.create(name=product['name'], description=product['description'], price=product['price'])
        return

    def remove_product(self, id):
        self.get(id=id).delete()
        return

    def edit_product(self, product, id):
        self.filter(id=id).update(name=product['name'], description=product['description'], price=product['price'])
        return

class Product(models.Model):
     name = models.CharField(max_length=255)
     description = models.TextField()
     price = models.DecimalField(max_digits=5, decimal_places=2)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     objects = ProductManager()
