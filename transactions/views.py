import datetime

from django.http import HttpRequest
from django.shortcuts import render

from categories.models import Category
from tags.models import Tag
from transactions.models import Transaction


def transactions(request: HttpRequest):
    all_tags = Tag.objects.all().order_by("name")
    all_transactions = Transaction.objects.all()
    categories = Category.objects.all().order_by("name")
    context = {"now": datetime.date.today().strftime("%Y-%m-%d"), "tags": all_tags, "active": "transactions",
               "categories": categories}

    return render(request, "transactions/transactions.html", context)
