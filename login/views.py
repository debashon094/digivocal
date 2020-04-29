from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import Login
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def home(request):
    #Love = "World"
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ("One item added"))
            logged_info = Login.objects.all()
            return render(request, 'home.html', {'a1': logged_info})

    else:
        logged_info = Login.objects.all()
        return render(request, 'home.html', {'a1': logged_info})

def edit(request, login_id):
    #print(login_id)
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ("One item edited"))
            logged_info = Login.objects.all()
            return render(request, 'home.html', {'a1': logged_info})
    else:
        edit_item = Login.objects.get(pk = login_id)
        return render(request, 'edit.html', {'test': edit_item})


def delete(request, login_id):
    delete_item = Login.objects.get(pk = login_id)
    delete_item.delete()
    messages.success(request,('One item deleted!!!'))
    return redirect('home')


def fb(request):
    facebook = OpenFacebook(access_token)
    logged_info = Login.objects.all()
    return render(request, 'home.html', {'a1': logged_info})


def acc(request):
    logged_info = Login.objects.all()
    return render(request, 'home.html', {'a1': logged_info})
