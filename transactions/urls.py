from django.urls import path

from transactions.views import transactions

urlpatterns = [path("", transactions, name="transactions")]
