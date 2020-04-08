from django.urls import path

from transactions.views import TransactionView, TransactionDeleteView

urlpatterns = [path("", TransactionView.as_view(), name=TransactionView.name),
               path("delete", TransactionDeleteView.as_view(), name=TransactionDeleteView.name)]
