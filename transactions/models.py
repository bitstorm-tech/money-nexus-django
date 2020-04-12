from django.db import models
from django.http import QueryDict

from categories.models import Category
from tags.models import Tag


class Transaction(models.Model):
    date = models.DateField()
    time = models.TimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    outgoing = models.BooleanField(default=True)
    note = models.TextField(null=True)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    tax_relevant = models.BooleanField(default=False)
    bill_image = models.ImageField(null=True)

    @staticmethod
    def from_post_data(post_data: QueryDict) -> "Transaction":
        transaction = Transaction()
        transaction.id = int(post_data["id"])
        transaction.date = post_data["date"]
        transaction.time = post_data["time"]
        transaction.amount = post_data["amount"]
        transaction.note = post_data["note"]
        transaction.outgoing = True if post_data["outgoing"] == "true" else False
        category_id = post_data["category"]
        transaction.category = Category.objects.get(id=category_id)
        return transaction
