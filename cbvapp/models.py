from django.db import models
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=100)
    ceo=models.CharField(max_length=100)
    origin=models.CharField(max_length=100)
    est_year=models.IntegerField()
    logo=models.ImageField(upload_to="logo/",blank=True,null=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
class Products(models.Model):
    Product_name=models.CharField(max_length=100)
    color=models.CharField(max_length=500)
    price=models.BigIntegerField()
    seat_capacity=models.IntegerField()
    fuel_type=models.CharField(max_length=100)
    Mileage=models.IntegerField()
    company=models.ForeignKey(Company,related_name='company',on_delete=models.CASCADE)

