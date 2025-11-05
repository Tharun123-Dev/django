from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
a=5
b=2
def addition(request):
 return  HttpResponse(f" the addition of numbers is {a+b}")
def substraction(request):
 return  HttpResponse(f" the substraction of numbers is {a-b}")
def multiplication(request):
 return  HttpResponse(f" the multiplication of numbers is {a*b}")
def division(request):
 return  HttpResponse(f" the division of numbers is {a/b}")
def fdivision(request):
 return  HttpResponse(f" the fdivision of numbers is {a//b}")

    