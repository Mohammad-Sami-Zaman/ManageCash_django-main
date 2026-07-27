from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUserModel(AbstractUser):
    full_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.username

# user (many to one User), source, datetime, amount, description
class AddCash_Model(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    source = models.CharField(max_length=200, null=True)
    datetime = models.DateField(auto_now=True, null=True)
    amount = models.FloatField(null= True)
    description = models.TextField(null=True, blank=True)

# (user {many to one User}, description, amount, datetime)
class Expense_Model(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    amount = models.FloatField(null= True)
    datetime = models.DateField(auto_now=True, null=True)



class Transaction_Model(models.Model):

    TRANSACTION_TYPE = (
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    )

    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    transaction_type = models.CharField( max_length=20, choices=TRANSACTION_TYPE)
    amount = models.FloatField()
    description = models.TextField(null=True, blank=True)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.transaction_type} - {self.amount}"