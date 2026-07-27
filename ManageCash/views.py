from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from ManageCash.models import *
from ManageCash.form import *



def signup(req):
    form_data = SignUp_Form()
    if req.method == 'POST':
        form_data = SignUp_Form(req.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(req, 'Account Creation Success')
            return redirect('login')
        else:
            messages.warning(req, 'Account Creation Failed')
            return redirect('signup')
    context = {
        'form_data' : form_data
    }

    return render(req, 'auth/signup.html', context)


def login_page(req):
    form_data = AuthenticationForm()
    if req.method == 'POST':
        form_data = AuthenticationForm(req, data = req.POST)
        if form_data.is_valid():
            user = form_data.get_user()
            login(req, user)
            messages.success(req, 'Login success')
            return redirect('profile_view')

    context = {
        'form_data' : form_data
    }
    return render(req, 'auth/login_page.html', context)



@login_required
def logout_view(req):

    logout(req)

    messages.success(req, 'LogOut Success')

    return redirect('login')




@login_required
def profile_view(req):

    return render(req, 'M_Cash/profile_view.html')

@login_required
def cash_dashboard(req):
    cash = AddCash_Model.objects.filter(user=req.user)
    expense = Expense_Model.objects.filter(user=req.user)

    income = sum(i.amount for i in cash)
    spend = sum(i.amount for i in expense)

    context = {
        'income': income,
        'expense': spend,
        'balance': income - spend,
    }


    return render(req, 'M_Cash/cash_dashboard.html', context)


@login_required
def expense(req):
    if req.method == 'POST':
        form = Expense_Form(req.POST)

        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = req.user
            expense.save()

            Transaction_Model.objects.create(
                user=req.user,
                transaction_type='Expense',
                amount=expense.amount,
                description=expense.description,
            )

            messages.success(req, 'Expense Added')
            return redirect('cash_dashboard')

    
    form = Expense_Form()

    context = {
        'form_data': form,
    }

    return render(req, 'M_Cash/expense.html', context)



@login_required
def AddCash(req):
    if req.method == 'POST':
        form = AddCash_Form(req.POST)

        if form.is_valid():
            cash = form.save(commit=False)
            cash.user = req.user
            cash.save()

            Transaction_Model.objects.create(
                user=req.user,
                transaction_type='Income',
                amount=cash.amount,
                description=cash.description,
            )

            messages.success(req, 'Cash Added')
            return redirect('cash_dashboard')

    
    form = AddCash_Form()

    context = {
        'form_data': form,
    }

    return render(req, 'M_Cash/AddCash_Model.html', context)


@login_required
def Transaction(req):

    transactions = Transaction_Model.objects.filter(user=req.user).order_by('-transaction_date')

    total_income = sum(
        transaction.amount
        for transaction in transactions
        if transaction.transaction_type == "Income"
    )

    total_expense = sum(
        transaction.amount
        for transaction in transactions
        if transaction.transaction_type == "Expense"
    )

    balance = total_income - total_expense

    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
    }

    return render(req, 'M_Cash/Transaction.html', context)




