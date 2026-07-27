from django.contrib import admin

# Register your models here.
from ManageCash.models import *

admin.site.register([CustomUserModel, AddCash_Model, Expense_Model, Transaction_Model])