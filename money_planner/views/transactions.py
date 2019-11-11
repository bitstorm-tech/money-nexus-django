import datetime

from django.http import HttpRequest
from django.shortcuts import render

from money_planner.models.tag import Tag
from money_planner.models.transaction import Transaction


def transactions(request: HttpRequest):
    all_tags = Tag.objects.all().order_by("name")
    all_transactions = Transaction.objects.all()
    context = {"now": datetime.date.today().strftime("%Y-%m-%d"), "tags": all_tags}

    return render(request, "money_planner/transactions.html", context)
