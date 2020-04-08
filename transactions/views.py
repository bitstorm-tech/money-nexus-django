from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View

from categories.models import Category
from tags.models import Tag
from transactions.models import Transaction


class TransactionView(View):
    template_name = "transactions/transactions.html"
    name = "transactions"

    def get(self, request: HttpRequest):
        tags = Tag.objects.all().order_by("name")
        all_transactions = Transaction.objects.all()
        categories = Category.objects.all().order_by("name")
        selected_category_id = 0 if len(categories) == 0 else categories[0].id
        context = {
            "tags": list(tags.values()),
            "categories": list(categories.values()),
            "active": "transactions",
            "selected_category_id": selected_category_id,
            "all_transactions": all_transactions,
        }
        return render(request, "transactions/transactions.html", context)

    def post(self, request: HttpRequest):
        post_data = request.POST
        transaction = Transaction.from_post_data(post_data)
        transaction.save()
        return redirect(self.name)


class TransactionDeleteView(View):
    name = "transactions_delete"

    def post(self, request: HttpRequest):
        transaction_id = request.POST["id"]
        Transaction.objects.get(id=transaction_id).delete()
        return redirect(TransactionView.name)
