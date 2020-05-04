from django.http import HttpRequest
from django.shortcuts import render


def bank_accounts(request: HttpRequest):
    context = {"active": "bank_accounts"}
    return render(request, "bank_accounts/bank_accounts.html", context)
