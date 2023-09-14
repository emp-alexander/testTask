from django.contrib.auth.models import User
from django.db import models

class Transaction(models.Model):
    summa = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)


    def __str__(self):
        return self.name

