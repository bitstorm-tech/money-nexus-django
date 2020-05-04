from django.urls import path

from bank_accounts.views import bank_accounts

urlpatterns = [
    path("", bank_accounts, name="bank_accounts"),
]
