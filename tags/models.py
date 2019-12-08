from django.db import models

from categories.models import Category


class Tag(models.Model):
    name = models.TextField(unique=True)
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
