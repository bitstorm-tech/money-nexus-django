from django.urls import path

from transactions.views import TransactionView, delete_transaction

urlpatterns = [
    path("", TransactionView.as_view(), name="transactions"),
    path("delete", delete_transaction, name="transactions_delete"),
]
