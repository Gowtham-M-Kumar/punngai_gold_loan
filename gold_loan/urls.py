from django.urls import path
from . import views

app_name = "gold_loan"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("loan/", views.loan_entry, name="loan_entry"),
    path("payment/", views.payment, name="payment"),
    path("close/", views.loan_close, name="loan_close"),
]
