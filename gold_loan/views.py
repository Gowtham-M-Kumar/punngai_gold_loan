from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "gold_loan/home.html")


def dashboard(request):
    return render(request, "gold_loan/dashboard/dashboard.html")


def loan_entry(request):
    return render(request, "gold_loan/loan/loan_entry.html")

def payment(request):
    return render(request, "gold_loan/payment/payment.html")

def loan_close(request):
    return render(request, "gold_loan/closure/loan_close.html")
