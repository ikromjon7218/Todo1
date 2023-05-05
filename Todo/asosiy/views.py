from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
# def asosiy(request):
#     return render(request, "asosiy.html")

def talabalar(request):
    data = {"talabalar": Talaba.objects.all()}
    return render(request, "talabalar.html", data)