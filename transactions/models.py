from django.db import models

from categories.models import Category
from tags.models import Tag


class Transaction(models.Model):
    date = models.DateField()
    time = models.TimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField(null=True)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    tax_relevant = models.BooleanField(default=False)
    bill_image = models.ImageField(null=True)
