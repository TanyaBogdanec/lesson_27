from django.shortcuts import render, redirect
from .models import Account
from .forms import UserForm


def product_list(request):
    accounts = Account.objects.all()
    return render(request, 'product_list.html', accounts)


def view_user_input(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserForm()

    return render(request, 'view_user_input.html', form)


def view_success(request):
    return render(request, 'success.html')


def view_index(request):
    return render(request, 'yourhtml/home_tema.html')


def view_contacts(request):
    return render(request, 'yourhtml/contacts.html')