from django.db import models


class Company(models.Model):
    NAME = models.CharField(max_length=255) 
    GST = models.CharField(max_length=255)

    def __str__(self):
        return self.NAME


class Product(models.Model):
    NAME = models.CharField(max_length=255,unique=True)
    COST = models.FloatField()
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return self.NAME


class Purchase(models.Model):
    purchage_order_number = models.CharField(max_length=255)
    quantity = models.IntegerField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    total_amount = models.FloatField()
    def __str__(self):
        return str(self.total_amount)

