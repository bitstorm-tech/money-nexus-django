from django.db import models


class Transaction(models.Model):
    date = models.DateField()
    time = models.TimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True)
    tags = models.ManyToManyField("Tag")
