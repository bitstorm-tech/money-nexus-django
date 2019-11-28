import datetime

from django.http import HttpRequest
from django.shortcuts import render

from tags.models import Tag
from transactions.models import Transaction


def transactions(request: HttpRequest):
    all_tags = Tag.objects.all().order_by("name")
    all_transactions = Transaction.objects.all()
    context = {"now": datetime.date.today().strftime("%Y-%m-%d"), "tags": all_tags, "active": "transactions"}

    return render(request, "transactions/transactions.html", context)
