from django.db import models


class Category(models.Model):
    name = models.TextField()
    description = models.TextField(null=True)


class SubCategory(models.Model):
    name = models.TextField()
    description = models.TextField(null=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
