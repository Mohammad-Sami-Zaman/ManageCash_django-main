

from django.urls import path
from ManageCash.views import *

urlpatterns = [
    
    path('', login_page, name='login'),
    path('signup/', signup, name='signup'),
    path('logout_view', logout_view, name='logout_view'),


    path('profile_view/', profile_view, name='profile_view'),
    path('cash_dashboard/', cash_dashboard, name='cash_dashboard'),
    path('expense/', expense, name='expense'),
    path('AddCash/', AddCash, name='AddCash'),
    
    path('Transaction/', Transaction, name='Transaction'),

]
