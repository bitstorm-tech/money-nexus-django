from django.http import HttpRequest
from django.shortcuts import render

from categories.models import Category
from tags.models import Tag
from transactions.models import Transaction


def transactions(request: HttpRequest):
    if request.method == "POST":
        print(f"Save transaction: {request.POST}")
        save_transaction(request.POST)

    tags = Tag.objects.all().order_by("name")
    all_transactions = Transaction.objects.all()
    categories = Category.objects.all().order_by("name")
    selected_category_id = 0 if len(categories) == 0 else categories[0].id
    context = {
        "tags": list(tags.values()),
        "categories": list(categories.values()),
        "active": "transactions",
        "selected_category_id": selected_category_id,
    }

    return render(request, "transactions/transactions.html", context)


def save_transaction(post_data):
    transaction = Transaction.from_post_data(post_data)
    transaction.save()
