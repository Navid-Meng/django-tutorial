from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)

'''
    CREATE TABLE myapp_item (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" VARCHAR(200) NOT NULL,
    "price" DECIMAL(10, 2) NOT NULL
    );
'''