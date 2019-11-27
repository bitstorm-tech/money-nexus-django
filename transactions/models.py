from django.db import models

from tags.models import Tag


class Transaction(models.Model):
    date = models.DateField()
    time = models.TimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField(null=True)
    tags = models.ManyToManyField(Tag)
    bill_image = models.ImageField(null=True)
