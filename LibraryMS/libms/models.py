from django.db import models

# Create your models here.
class Book(models.Model):
    bookn = models.CharField(max_length=30)
    authorn = models.CharField(max_length=30)
    price = models.IntegerField()
    type = models.CharField(max_length=30)
    is_deleted = models.CharField(max_length=2,default='n')
