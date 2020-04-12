import json

from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View

from categories.models import Category
from money_nexus.json_utils import to_json
from tags.models import Tag
from transactions.models import Transaction


class TransactionView(View):
    template_name = "transactions/transactions.html"

    def get(self, request: HttpRequest):
        tags = Tag.objects.all().order_by("name")
        all_transactions = Transaction.objects.all().order_by("date").order_by("time")
        categories = Category.objects.all().order_by("name")
        selected_category_id = 0 if len(categories) == 0 else categories[0].id
        context = {
            "tags": list(tags.values()),
            "categories": list(categories.values()),
            "categories_json": to_json(categories),
            "active": "transactions",
            "selected_category_id": selected_category_id,
            "transactions": list(all_transactions),
            "transactions_json": to_json(all_transactions),
        }
        return render(request, "transactions/transactions.html", context)

    def post(self, request: HttpRequest):
        post_data = request.POST
        transaction = Transaction.from_post_data(post_data)
        if transaction.id >= 0:
            Transaction.objects.filter(id=transaction.id).update(
                amount=transaction.amount,
                date=transaction.date,
                time=transaction.time,
                note=transaction.note,
                category=transaction.category,
                outgoing=transaction.outgoing,
            )
        else:
            transaction.save()
        return redirect("/transactions")


def delete_transaction(request: HttpRequest):
    transaction_id = request.POST["id"]
    Transaction.objects.get(id=transaction_id).delete()
    return redirect("/transactions")
